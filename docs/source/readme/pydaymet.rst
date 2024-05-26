
PyDaymet: Daily climate data through Daymet
-------------------------------------------

.. image:: https://img.shields.io/pypi/v/pydaymet.svg
    :target: https://pypi.python.org/pypi/pydaymet
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pydaymet.svg
    :target: https://anaconda.org/conda-forge/pydaymet
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/pydaymet/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/pydaymet
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pydaymet.svg
    :target: https://pypi.python.org/pypi/pydaymet
    :alt: Python Versions

.. image:: https://static.pepy.tech/badge/pydaymet
    :target: https://pepy.tech/project/pydaymet
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/hyriver/pydaymet/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pydaymet
   :alt: CodeFactor

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

|

.. warning::

    Since the release of Daymet v4 R1 on November 2022, the URL of
    Daymet's server has been changed. Therefore, only PyDaymet v0.13.7+
    is going to work, and previous versions will not work anymore.

Features
--------

PyDaymet is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
access to climate data from
`Daymet V4 R1 <https://daymet.ornl.gov/overview>`__ database using NetCDF
Subset Service (NCSS). Both single pixel (using ``get_bycoords`` function) and gridded data (using
``get_bygeom``) are supported which are returned as
``pandas.DataFrame`` and ``xarray.Dataset``, respectively. Climate data is available for North
America, Hawaii from 1980, and Puerto Rico from 1950 at three time scales: daily, monthly,
and annual. Additionally, PyDaymet can compute Potential EvapoTranspiration (PET)
using three methods: ``penman_monteith``, ``priestley_taylor``, and ``hargreaves_samani`` for
both single pixel and gridded data.

For PET computations, PyDaymet accepts four additional user-defined parameters:

* ``penman_monteith``: ``soil_heat_flux``, ``albedo``, ``alpha``,
    and ``arid_correction``.
* ``priestley_taylor``: ``soil_heat_flux``, ``albedo``, and ``arid_correction``.
* ``hargreaves_samani``: None.

Default values for the parameters are: ``soil_heat_flux`` = 0, ``albedo`` = 0.23,
``alpha`` = 1.26, and ``arid_correction`` = False.
An important parameter for ``priestley_taylor`` and ``penman_monteith`` methods
is ``arid_correction`` which is used to correct the actual vapor pressure
for arid regions. Since relative humidity is not provided by Daymet, the actual
vapor pressure is computed assuming that the dew point temperature is equal to
the minimum temperature. However, for arid regions, FAO 56 suggests subtracting
minimum temperature by 2-3 °C to account for the fact that in arid regions,
the air might not be saturated when its temperature is at its minimum. For such
areas, you can pass ``{"arid_correction": True, ...}`` to subtract 2 °C from the
minimum temperature for computing the actual vapor pressure.

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

Moreover, under the hood, PyDaymet uses
`PyGeoOGC <https://github.com/hyriver/pygeoogc>`__ and
`AsyncRetriever <https://github.com/hyriver/async-retriever>`__ packages
for making requests in parallel and storing responses in chunks. This improves the
reliability and speed of data retrieval significantly.

You can control the request/response caching behavior and verbosity of the package
by setting the following environment variables:

* ``HYRIVER_CACHE_NAME``: Path to the caching SQLite database for asynchronous HTTP
  requests. It defaults to ``./cache/aiohttp_cache.sqlite``
* ``HYRIVER_CACHE_NAME_HTTP``: Path to the caching SQLite database for HTTP requests.
  It defaults to ``./cache/http_cache.sqlite``
* ``HYRIVER_CACHE_EXPIRE``: Expiration time for cached requests in seconds. It defaults to
  one week.
* ``HYRIVER_CACHE_DISABLE``: Disable reading/writing from/to the cache. The default is false.
* ``HYRIVER_SSL_CERT``: Path to a SSL certificate file.

For example, in your code before making any requests you can do:

.. code-block:: python

    import os

    os.environ["HYRIVER_CACHE_NAME"] = "path/to/aiohttp_cache.sqlite"
    os.environ["HYRIVER_CACHE_NAME_HTTP"] = "path/to/http_cache.sqlite"
    os.environ["HYRIVER_CACHE_EXPIRE"] = "3600"
    os.environ["HYRIVER_CACHE_DISABLE"] = "true"
    os.environ["HYRIVER_SSL_CERT"] = "path/to/cert.pem"

You can also try using PyDaymet without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pydaymet/issues>`__.

Citation
--------
If you use any of HyRiver packages in your research, we appreciate citations:

.. code-block:: bibtex

    @article{Chegini_2021,
        author = {Chegini, Taher and Li, Hong-Yi and Leung, L. Ruby},
        doi = {10.21105/joss.03175},
        journal = {Journal of Open Source Software},
        month = {10},
        number = {66},
        pages = {1--3},
        title = {{HyRiver: Hydroclimate Data Retriever}},
        volume = {6},
        year = {2021}
    }

Installation
------------

You can install PyDaymet using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``):

.. code-block:: console

    $ pip install pydaymet

Alternatively, PyDaymet can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pydaymet

Quick start
-----------

You can use PyDaymet using command-line or as a Python library. The commanda-line
provides access to two functionality:

- Getting gridded climate data: You must create a ``geopandas.GeoDataFrame`` that contains
  the geometries of the target locations. This dataframe must have four columns:
  ``id``, ``start``, ``end``, ``geometry``. The ``id`` column is used as
  filenames for saving the obtained climate data to a NetCDF (``.nc``) file. The ``start``
  and ``end`` columns are starting and ending dates of the target period. Then,
  you must save the dataframe as a shapefile (``.shp``) or geopackage (``.gpkg``) with
  CRS attribute.
- Getting single pixel climate data: You must create a CSV file that
  contains coordinates of the target locations. This file must have at four columns:
  ``id``, ``start``, ``end``, ``lon``, and ``lat``. The ``id`` column is used as filenames
  for saving the obtained climate data to a CSV (``.csv``) file. The ``start`` and ``end``
  columns are the same as the ``geometry`` command. The ``lon`` and ``lat`` columns are
  the longitude and latitude coordinates of the target locations.

.. code-block:: console

    $ pydaymet -h
    Usage: pydaymet [OPTIONS] COMMAND [ARGS]...

    Command-line interface for PyDaymet.

    Options:
    -h, --help  Show this message and exit.

    Commands:
    coords    Retrieve climate data for a list of coordinates.
    geometry  Retrieve climate data for a dataframe of geometries.

The ``coords`` sub-command is as follows:

.. code-block:: console

    $ pydaymet coords -h
    Usage: pydaymet coords [OPTIONS] FPATH

    Retrieve climate data for a list of coordinates.

    FPATH: Path to a csv file with four columns:
        - ``id``: Feature identifiers that daymet uses as the output netcdf filenames.
        - ``start``: Start time.
        - ``end``: End time.
        - ``lon``: Longitude of the points of interest.
        - ``lat``: Latitude of the points of interest.
        - ``time_scale``: (optional) Time scale, either ``daily`` (default), ``monthly`` or ``annual``.
        - ``pet``: (optional) Method to compute PET. Supported methods are:
                    ``penman_monteith``, ``hargreaves_samani``, ``priestley_taylor``, and ``none`` (default).
        - ``snow``: (optional) Separate snowfall from precipitation, default is ``False``.

    Examples:
        $ cat coords.csv
        id,lon,lat,start,end,pet
        california,-122.2493328,37.8122894,2012-01-01,2014-12-31,hargreaves_samani
        $ pydaymet coords coords.csv -v prcp -v tmin

    Options:
    -v, --variables TEXT  Target variables. You can pass this flag multiple
                            times for multiple variables.
    -s, --save_dir PATH   Path to a directory to save the requested files.
                            Extension for the outputs is .nc for geometry and .csv
                            for coords.
    --disable_ssl         Pass to disable SSL certification verification.
    -h, --help            Show this message and exit.

And, the ``geometry`` sub-command is as follows:

.. code-block:: console

    $ pydaymet geometry -h
    Usage: pydaymet geometry [OPTIONS] FPATH

    Retrieve climate data for a dataframe of geometries.

    FPATH: Path to a shapefile (.shp) or geopackage (.gpkg) file.
    This file must have four columns and contain a ``crs`` attribute:
        - ``id``: Feature identifiers that daymet uses as the output netcdf filenames.
        - ``start``: Start time.
        - ``end``: End time.
        - ``geometry``: Target geometries.
        - ``time_scale``: (optional) Time scale, either ``daily`` (default), ``monthly`` or ``annual``.
        - ``pet``: (optional) Method to compute PET. Supported methods are:
                    ``penman_monteith``, ``hargreaves_samani``, ``priestley_taylor``, and ``none`` (default).
        - ``snow``: (optional) Separate snowfall from precipitation, default is ``False``.

    Examples:
        $ pydaymet geometry geo.gpkg -v prcp -v tmin

    Options:
    -v, --variables TEXT  Target variables. You can pass this flag multiple
                            times for multiple variables.
    -s, --save_dir PATH   Path to a directory to save the requested files.
                            Extension for the outputs is .nc for geometry and .csv
                            for coords.
    --disable_ssl         Pass to disable SSL certification verification.
    -h, --help            Show this message and exit.

Now, let's see how we can use PyDaymet as a library.

PyDaymet offers two functions for getting climate data; ``get_bycoords`` and ``get_bygeom``.
The arguments of these functions are identical except the first argument where the latter
should be polygon and the former should be a coordinate (a tuple of length two as in (x, y)).
The input geometry or coordinate can be in any valid CRS (defaults to ``EPSG:4326``). The
``dates`` argument can be either a tuple of length two like ``(start_str, end_str)`` or a list of
years like ``[2000, 2005]``. It is noted that both functions have a ``pet`` flag for computing PET
and a ``snow`` flag for separating snow from precipitation using
`Martinez and Gupta (2010) <https://doi.org/10.1029/2009WR008294>`__ method.
Additionally, we can pass ``time_scale`` to get daily, monthly or annual summaries. This flag
by default is set to daily.

.. code-block:: python

    from pynhd import NLDI
    import pydaymet as daymet

    geometry = NLDI().get_basins("01031500").geometry[0]

    var = ["prcp", "tmin"]
    dates = ("2000-01-01", "2000-06-30")

    daily = daymet.get_bygeom(geometry, dates, variables=var, pet="priestley_taylor", snow=True)
    monthly = daymet.get_bygeom(geometry, dates, variables=var, time_scale="monthly")

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/daymet_grid.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb

If the input geometry (or coordinate) is in a CRS other than ``EPSG:4326``, we should pass
it to the functions.

.. code-block:: python

    coords = (-1431147.7928, 318483.4618)
    crs = 3542
    dates = ("2000-01-01", "2006-12-31")
    annual = daymet.get_bycoords(coords, dates, variables=var, loc_crs=crs, time_scale="annual")

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/daymet_loc.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb

Additionally, the ``get_bycoords`` function accepts a list of coordinates and by setting the
``to_xarray`` flag to ``True`` it can return the results as a ``xarray.Dataset`` instead of
a ``pandas.DataFrame``:

.. code-block:: python

    coords = [(-94.986, 29.973), (-95.478, 30.134)]
    idx = ["P1", "P2"]
    clm_ds = daymet.get_bycoords(coords, range(2000, 2021), coords_id=idx, to_xarray=True)

Also, we can use the ``potential_et`` function to compute PET by passing the daily climate data.
We can either pass a ``pandas.DataFrame`` or a ``xarray.Dataset``. Note that, ``penman_monteith``
and ``priestley_taylor`` methods have parameters that can be passed via the ``params`` argument,
if any value other than the default values are needed. For example, default value of ``alpha``
for ``priestley_taylor`` method is 1.26 (humid regions), we can set it to 1.74 (arid regions)
as follows:

.. code-block:: python

    pet_hs = daymet.potential_et(daily, methods="priestley_taylor", params={"alpha": 1.74})

Next, let's get annual total precipitation for Hawaii and Puerto Rico for 2010.

.. code-block:: python

    hi_ext = (-160.3055, 17.9539, -154.7715, 23.5186)
    pr_ext = (-67.9927, 16.8443, -64.1195, 19.9381)
    hi = daymet.get_bygeom(hi_ext, 2010, variables="prcp", region="hi", time_scale="annual")
    pr = daymet.get_bygeom(pr_ext, 2010, variables="prcp", region="pr", time_scale="annual")

Some example plots are shown below:

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/hi.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/pr.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb
