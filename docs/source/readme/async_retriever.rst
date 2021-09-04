AsyncRetriever: Asynchronous requests with persistent caching
-------------------------------------------------------------

.. image:: https://img.shields.io/pypi/v/async_retriever.svg
    :target: https://pypi.python.org/pypi/async_retriever
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/async_retriever.svg
    :target: https://anaconda.org/conda-forge/async_retriever
    :alt: Conda Version

.. image:: https://codecov.io/gh/cheginit/async_retriever/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/cheginit/async_retriever
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/async_retriever.svg
    :target: https://pypi.python.org/pypi/async_retriever
    :alt: Python Versions

.. image:: https://github.com/cheginit/async_retriever/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/async_retriever/actions/workflows/test.yml
    :alt: Github Actions

|

.. image:: https://img.shields.io/badge/security-bandit-green.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. image:: https://www.codefactor.io/repository/github/cheginit/async_retriever/badge
   :target: https://www.codefactor.io/repository/github/cheginit/async_retriever
   :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

|

Features
--------

AsyncRetriever is a part of `HyRiver <https://github.com/cheginit/HyRiver>`__ software stack that
is designed to aid in watershed analysis through web services. This package has only one purpose;
asynchronously sending requests and retrieving responses as ``text``, ``binary``, or ``json``
objects. It uses persistent caching to speedup the retrieval even further. Moreover, thanks
to `nest_asyncio <https://github.com/erdewit/nest_asyncio>`__ you can use this function in
Jupyter notebooks as well. Although this package is in the HyRiver software stack, it's
applicable to any HTTP requests.

Please note that since this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/cheginit/async_retriever/issues>`__.

Installation
------------

You can install ``async_retriever`` using ``pip``:

.. code-block:: console

    $ pip install async_retriever

Alternatively, ``async_retriever`` can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge async_retriever

Quick start
-----------

AsyncRetriever has one public function: ``retrieve``. By default, this function uses
``./cache/aiohttp_cache.sqlite`` as the cache file. You can use ``cache_name`` argument
to customize it. Now, let's see it in action!

As an example for retrieving a ``binary`` response, let's use the DAAC server to get
`NDVI <https://daac.ornl.gov/VEGETATION/guides/US_MODIS_NDVI.html>`_.
The function can be directly passed to ``xarray.open_mfdataset`` to get the data as
an ``xarray`` Dataset.

.. code-block:: python

    import io
    import xarray as xr
    import async_retriever as ar
    from datetime import datetime

    west, south, east, north = (-69.77, 45.07, -69.31, 45.45)
    base_url = "https://thredds.daac.ornl.gov/thredds/ncss/ornldaac/1299"
    dates_itr = ((datetime(y, 1, 1), datetime(y, 1, 31)) for y in range(2000, 2005))
    urls, kwds = zip(
        *[
            (
                f"{base_url}/MCD13.A{s.year}.unaccum.nc4",
                {
                    "params": {
                        "var": "NDVI",
                        "north": f"{north}",
                        "west": f"{west}",
                        "east": f"{east}",
                        "south": f"{south}",
                        "disableProjSubset": "on",
                        "horizStride": "1",
                        "time_start": s.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "time_end": e.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "timeStride": "1",
                        "addLatLon": "true",
                        "accept": "netcdf",
                    }
                },
            )
            for s, e in dates_itr
        ]
    )
    resp = ar.retrieve(urls, "binary", request_kwds=kwds, max_workers=8)
    data = xr.open_mfdataset(io.BytesIO(r) for r in resp)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/ndvi.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/async.ipunb

For a ``json`` response example, let's get water level recordings of a NOAA's water level station,
8534720 (Atlantic City, NJ), during 2012, using CO-OPS API. Note that this CO-OPS product has a 31-day
limit for a single request, so we have to break the request down accordingly.

.. code-block:: python

    import pandas as pd

    station_id = "8534720"
    start = pd.to_datetime("2012-01-01")
    end = pd.to_datetime("2012-12-31")

    s = start
    dates = []
    for e in pd.date_range(start, end, freq="m"):
        dates.append((s.date(), e.date()))
        s = e + pd.offsets.MonthBegin()

    url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"

    urls, kwds = zip(
        *[
            (
                url,
                {
                    "params": {
                        "product": "water_level",
                        "application": "web_services",
                        "begin_date": f'{s.strftime("%Y%m%d")}',
                        "end_date": f'{e.strftime("%Y%m%d")}',
                        "datum": "MSL",
                        "station": f"{station_id}",
                        "time_zone": "GMT",
                        "units": "metric",
                        "format": "json",
                    }
                },
            )
            for s, e in dates
        ]
    )

    resp = ar.retrieve(urls, read="json", request_kwds=kwds, cache_name="~/.cache/async.sqlite")
    wl_list = []
    for rjson in resp:
        wl = pd.DataFrame.from_dict(rjson["data"])
        wl["t"] = pd.to_datetime(wl.t)
        wl = wl.set_index(wl.t).drop(columns="t")
        wl["v"] = pd.to_numeric(wl.v, errors="coerce")
        wl_list.append(wl)
    water_level = pd.concat(wl_list).sort_index()
    water_level.attrs = rjson["metadata"]

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/water_level.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/async.ipunb

Now, let's see an example without any payload or headers. Here's how we can retrieve
harmonic constituents of several NOAA stations from CO-OPS:

.. code-block:: python

    stations = [
        "8410140",
        "8411060",
        "8413320",
        "8418150",
        "8419317",
        "8419870",
        "8443970",
        "8447386",
    ]

    base_url = "https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations"
    urls = [f"{base_url}/{i}/harcon.json?units=metric" for i in stations]
    resp = ar.retrieve(urls, "json")

    amp_list = []
    phs_list = []
    for rjson in resp:
        sid = rjson["self"].rsplit("/", 2)[1]
        const = pd.DataFrame.from_dict(rjson["HarmonicConstituents"]).set_index("name")
        amp = const.rename(columns={"amplitude": sid})[sid]
        phase = const.rename(columns={"phase_GMT": sid})[sid]
        amp_list.append(amp)
        phs_list.append(phase)

    amp = pd.concat(amp_list, axis=1)
    phs = pd.concat(phs_list, axis=1)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/tides.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/async.ipunb
