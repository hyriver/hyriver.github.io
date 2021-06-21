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

    $ pip install py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can use ``conda`` or ``mamba`` (recommended) to install these packages from
the ``conda-forge`` repository:

.. code-block:: console

    $ conda install -c conda-forge py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever

or:

.. code-block:: console

    $ mamba install -c conda-forge --strict-channel-priority py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever

Dependencies
------------

.. panels::
    :column: col-lg-12 col-md-12 col-sm-12 col-xs-12 p-2

    .. tabbed:: PyNHD

        - ``cytoolz``
        - ``geopandas``
        - ``networkx``
        - ``numpy``
        - ``pandas``
        - ``pyarrow``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``requests``
        - ``shapely``
        - ``simplejson``

    .. tabbed:: PyGeoHydro

        - ``defusedxml``
        - ``folium``
        - ``geopandas``
        - ``lxml``
        - ``matplotlib``
        - ``numpy``
        - ``openpyxl``
        - ``pandas``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``pynhd``
        - ``rasterio``
        - ``shapely``

    .. tabbed:: Py3DEP

        - ``click``
        - ``cytoolz``
        - ``numpy``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``rasterio``
        - ``shapely``
        - ``xarray``

    .. tabbed:: PyDaymet

        - ``async_retriever``
        - ``click``
        - ``dask[complete]``
        - ``lxml``
        - ``numpy``
        - ``pandas``
        - ``py3dep``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``rasterio``
        - ``scipy``
        - ``shapely``
        - ``xarray``

.. panels::
    :column: col-lg-12 col-md-12 col-sm-12 col-xs-12 p-2

    .. tabbed:: PyGeoOGC

        - ``cytoolz``
        - ``defusedxml``
        - ``owslib``
        - ``pyproj``
        - ``pyyaml``
        - ``requests``
        - ``shapely``
        - ``simplejson``
        - ``urllib3``

    .. tabbed:: PyGeoUtils

        - ``affine``
        - ``geopandas``
        - ``netcdf4``
        - ``numpy``
        - ``orjson``
        - ``pygeoogc``
        - ``pyproj``
        - ``rasterio``
        - ``shapely``
        - ``xarray``

    .. tabbed:: AsyncRetriever

        - ``aiohttp-client-cache``
        - ``aiohttp[speedups]``
        - ``aiosqlite``
        - ``cytoolz``
        - ``nest-asyncio``
        - ``orjson``

Additionally, you can also install ``bottleneck``, ``pygeos``, and ``rtree`` to improve
performance of ``xarray`` and ``geopandas``. For handling vector and
raster data projections, ``cartopy`` and ``rioxarray`` are useful.
