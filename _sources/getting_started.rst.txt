.. highlight:: bash

===============
Getting Started
===============

Why HyRiver?
------------

Some major capabilities of HyRiver are as follows:

* Easy access to many web services for subsetting data on server-side and returning the requests
  as masked Datasets or GeoDataFrames.
* Splitting large requests into smaller chunks, under-the-hood, since web services often limit
  the number of features per request. So the only bottleneck for subsetting the data
  is your local machine memory.
* Navigating and subsetting NHDPlus database (both medium- and high-resolution) using web services.
* Cleaning up the vector NHDPlus data, fixing some common issues, and computing vector-based
  accumulation through a river network.
* A URL inventory for some popular (and tested) web services.
* Some utilities for manipulating the obtained data and their visualization.

Installation
------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async-retriever

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can use ``conda`` or ``mamba`` (recommended) to install these packages from
the ``conda-forge`` repository:

.. code-block:: console

    $ conda install -c conda-forge py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async-retriever

or:

.. code-block:: console

    $ mamba install -c conda-forge --strict-channel-priority py3dep pynhd pygeohydro pydaymet pygeoogc pygeoutils async-retriever

Dependencies
------------

.. tab-set::

    .. tab-item:: PyNHD

        - ``async-retriever``
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

    .. tab-item:: PyGeoHydro

        - ``async-retriever``
        - ``cytoolz``
        - ``defusedxml``
        - ``folium``
        - ``geopandas``
        - ``h5netcdf``
        - ``lxml``
        - ``numpy``
        - ``pandas``
        - ``proplot``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``pynhd``
        - ``rasterio``
        - ``scipy``
        - ``shapely``

    .. tab-item:: Py3DEP

        - ``async-retriever``
        - ``click``
        - ``cytoolz``
        - ``numpy``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``rasterio``
        - ``rioxarray``
        - ``scipy``
        - ``shapely``
        - ``xarray``

    .. tab-item:: PyDaymet

        - ``async-retriever``
        - ``click``
        - ``dask``
        - ``lxml``
        - ``numpy``
        - ``pandas``
        - ``py3dep``
        - ``pydantic``
        - ``pygeoogc``
        - ``pygeoutils``
        - ``rasterio``
        - ``scipy``
        - ``shapely``
        - ``xarray``

.. tab-set::

    .. tab-item:: PyGeoOGC

        - ``async-retriever``
        - ``cytoolz``
        - ``defusedxml``
        - ``owslib``
        - ``pydantic``
        - ``pyproj``
        - ``pyyaml``
        - ``requests``
        - ``requests-cache``
        - ``shapely``
        - ``urllib3``

    .. tab-item:: PyGeoUtils

        - ``dask``
        - ``geopandas``
        - ``netcdf4``
        - ``numpy``
        - ``pygeos``
        - ``pyproj``
        - ``rasterio``
        - ``rioxarray``
        - ``scipy``
        - ``shapely``
        - ``ujson``
        - ``xarray``

    .. tab-item:: AsyncRetriever

        - ``aiohttp-client-cache``
        - ``aiohttp[speedups]``
        - ``aiosqlite``
        - ``cytoolz``
        - ``nest-asyncio``
        - ``ujson``

Additionally, you can also install ``bottleneck`` to improve performance of
``xarray``. For handling vector and raster data projections, ``cartopy`` are useful.
