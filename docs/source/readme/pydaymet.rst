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

.. image:: https://pepy.tech/badge/pydaymet
    :target: https://pepy.tech/project/pydaymet
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/hyriver/pydaymet/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pydaymet
   :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

|

Features
--------

PyDaymet is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
access to climate data from
`Daymet V4 <https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html>`__ database using NetCDF
Subset Service (NCSS). Both single pixel (using ``get_bycoords`` function) and gridded data (using
``get_bygeom``) are supported which are returned as
``pandas.DataFrame`` and ``xarray.Dataset``, respectively. Climate data is available for North
America, Hawaii from 1980, and Puerto Rico from 1950 at three time scales: daily, monthly,
and annual. Additionally, PyDaymet can compute Potential EvapoTranspiration (PET)
using three methods: ``penman_monteith``, ``priestley_taylor``, and ``hargreaves_samani`` for
both single pixel and gridded data.

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

Moreover, under the hood, PyDaymet uses
`AsyncRetriever <https://github.com/hyriver/async_retriever>`__
for making requests asynchronously with persistent caching. This improves the
reliability and speed of data retrieval significantly. AsyncRetriever caches all request/response
pairs and upon making an already cached request, it will retrieve the responses from the cache
if the server's response is unchanged.

You can control the request/response caching behavior by setting the following
environment variables:

* ``HYRIVER_CACHE_NAME``: Path to the caching SQLite database. It defaults to
  ``./cache/aiohttp_cache.sqlite``
* ``HYRIVER_CACHE_EXPIRE``: Expiration time for cached requests in seconds. It defaults to
  -1 (never expire).
* ``HYRIVER_CACHE_DISABLE``: Disable reading/writing from/to the cache. The default is false.

For example, in your code before making any requests you can do:

.. code-block:: python

    import os

    os.environ["HYRIVER_CACHE_NAME"] = "path/to/file.sqlite"
    os.environ["HYRIVER_CACHE_EXPIRE"] = "3600"
    os.environ["HYRIVER_CACHE_DISABLE"] = "true"

You can also try using PyDaymet without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Please note that since this project is in the early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pydaymet/issues>`__.

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
        - ``pet``: (optional) Method to compute PET. Suppoerted methods are:
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
        - ``pet``: (optional) Method to compute PET. Suppoerted methods are:
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

    daily = daymet.get_bygeom(
        geometry, dates, variables=var, pet="priestley_taylor", snow=True
    )
    monthly = daymet.get_bygeom(geometry, dates, variables=var, time_scale="monthly")

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/daymet_grid.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb

If the input geometry (or coordinate) is in a CRS other than ``EPSG:4326``, we should pass
it to the functions.

.. code-block:: python

    coords = (-1431147.7928, 318483.4618)
    crs = "epsg:3542"
    dates = ("2000-01-01", "2006-12-31")
    annual = daymet.get_bycoords(
        coords, dates, variables=var, loc_crs=crs, time_scale="annual"
    )

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/daymet_loc.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/daymet.ipynb

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
