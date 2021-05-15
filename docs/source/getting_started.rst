.. highlight:: bash

===============
Getting Started
===============

Why HyRiver?
------------

Some of the major capabilities of HyRiver are as follows:

* Easy access to many web services for subsetting data on server-side and returning the requests
  as masked Datasets or GeoDataFrames.
* Splitting large requests into smaller chunks, under-the-hood, since web services often limit
  the number of features per request. So the only bottleneck for subsetting the data
  is your local machine memory.
* Navigating and subsetting NHDPlus database (both medium- and high-resolution) using web services.
* Cleaning up the vector NHDPlus data, fixing some common issues, and computing vector-based
  accumulation through a river network.
* A URL inventory for some of the popular (and tested) web services.
* Some utilities for manipulating the obtained data and their visualization.

Installation
------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install pygeoogc pygeoutils py3dep pynhd pygeohydro pydaymet

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can use ``conda`` or ``mamba`` (recommended) to install these packages from
the ``conda-forge`` repository:

.. code-block:: console

    $ conda install -c conda-forge pygeoogc pygeoutils py3de pynhd pygeohydro pydaymet

or:

.. code-block:: console

    $ mamba install -c conda-forge --strict-channel-priority pygeoogc pygeoutils py3de pynhd pygeohydro pydaymet

Dependencies
------------

.. panels::
    :column: col-lg-12 p-2

    .. tabbed:: PyNHD

        - ``pygeoutils``
        - ``networkx``
        - ``pyarrow``

    .. tabbed:: PyGeoHydro

        - ``pynhd``
        - ``folium``
        - ``lxml``
        - ``matplotlib``
        - ``openpyxl``

    .. tabbed:: Py3DEP

        - ``pygeoutils``

    .. tabbed:: PyDaymet

        - ``py3dep``
        - ``aiohttp-client-cache`` (optional)
        - ``aiosqlite`` (optional)
        - ``async_retriever``
        - ``dask``
        - ``lxml``
        - ``scipy``

.. panels::
    :column: col-lg-12 p-2

    .. tabbed:: PyGeoOGC

        - ``cytoolz``
        - ``defusedxml``
        - ``owslib``
        - ``pyproj``
        - ``requests``
        - ``requests_cache`` (optional)
        - ``setuptools``

    .. tabbed:: PyGeoUtils

        - ``pygeoogc``
        - ``geopandas``
        - ``netcdf4``
        - ``rasterio``
        - ``xarray``

    .. tabbed:: AsyncRetriever

        - ``aiodns``
        - ``aiohttp``
        - ``aiohttp-client-cache`` (optional)
        - ``aiosqlite`` (optional)
        - ``brotlipy``
        - ``chardet``
        - ``cytoolz``
        - ``nest-asyncio``
        - ``orjson``
        - ``setuptools``


Additionally, you can also install ``bottleneck``, ``pygeos``, and ``rtree`` to improve
performance of ``xarray`` and ``geopandas``. For handling vector and
raster data projections, ``cartopy`` and ``rioxarray`` are useful.
