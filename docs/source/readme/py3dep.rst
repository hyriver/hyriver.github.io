
Py3DEP: Topographic data through 3DEP
-------------------------------------

.. image:: https://img.shields.io/pypi/v/py3dep.svg
    :target: https://pypi.python.org/pypi/py3dep
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/py3dep.svg
    :target: https://anaconda.org/conda-forge/py3dep
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/py3dep/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/py3dep
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/py3dep.svg
    :target: https://pypi.python.org/pypi/py3dep
    :alt: Python Versions

.. image:: https://static.pepy.tech/badge/py3dep
    :target: https://pepy.tech/project/py3dep
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/hyriver/py3dep/badge
   :target: https://www.codefactor.io/repository/github/hyriver/py3dep
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

Note
----

Users are encouraged to using the new HyRiver package called Seamless3DEP
which is a lightweight and efficient package providing access to both static
DEMs and dynamic 3DEP service. This package is a part of the HyRiver software
stack and is the recommended package for accessing 3DEP data. For more information
please visit its `documentation <https://seamless-3dep.readthedocs.io/en/latest/>`__.
For the time being, Py3DEP will be maintained for bug fixes and minor updates.

Also, from version 0.19, the default CRS for ``get_map`` was changed from
``EPSG:4326`` to ``EPSG:5070``. This is due to a recent issue with the 3DEP service
where the it returns invalid results when the requested CRS in not in a projected
coordinate system.

Features
--------

Py3DEP is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
access to the `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`__
database which is a part of the
`National Map services <https://viewer.nationalmap.gov/services/>`__.
The 3DEP service has multi-resolution sources and depending on the user-provided resolution,
the data is resampled on the server-side based on all the available data sources. Py3DEP returns
the requests as `xarray <https://xarray.pydata.org/en/stable>`__ dataset.

The following functionalities are currently available:

- ``get_map``: Get topographic data the dynamic 3DEP service that supports the following
  layers:

    - DEM
    - Hillshade Gray
    - Aspect Degrees
    - Aspect Map
    - GreyHillshade Elevation Fill
    - Hillshade Multidirectional
    - Slope Degrees
    - Slope Map
    - Hillshade Elevation Tinted
    - Height Ellipsoidal
    - Contour 25
    - Contour Smoothed 25
- ``static_3dep_dem``: Get DEM data at 10 m, 30 m, or 60 m resolution from the staged 3DEP
  data. Since this function only returns DEM, for computing other terrain attributes you
  can use `xarray-spatial <https://xarray-spatial.org/>`__. Just note that you should
  reproject the output ``DataArray`` to a projected CRS like 5070 before passing it to
  ``xarray-spatial`` like so: ``dem = dem.rio.reproject(5070)``.
- ``get_dem``: Get DEM data from either the dynamic or static 3DEP service. Considering
  that the static service is much faster, if the target DEM resolution is 10 m, 30 m, or
  60 m, then the static service is used (``static_3dep_dem``). Otherwise, the dynamic
  service is used (``get_map`` using ``DEM`` layer).
- ``get_map_vrt``: Get DEM data and store it as a GDAL VRT file from the dynamic 3DEP
  service. This function is mainly provided for large requests due to its low memory
  footprint. Moreover, due to lazy loading of the data this function can be much
  faster than ``get_map`` or ``get_dem``, even for small requests at the cost of
  higher disk usage.
- ``elevation_bygrid``: For retrieving elevations of all the grid points in a 2D grid.
- ``add_elevation``: For adding elevation data as a new variable to an input
  ``xarray.DataArray`` or ``xarray.Dataset``.
- ``elevation_bycoords``: For retrieving elevation of a list of ``x`` and ``y`` coordinates.
- ``elevation_profile``: For retrieving elevation profile along a line at a given spacing.
  This function converts the line to a B-spline and then calculates the elevation along
  the spline at a given uniform spacing.
- ``deg2mpm``: For converting slope dataset from degree to meter per meter.
- ``query_3dep_sources``: For querying bounds of 3DEP's data sources within a bounding box.
- ``check_3dep_availability``: For querying 3DEP's resolution availability within a bounding box.

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

Moreover, under the hood, Py3DEP uses
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

You can also try using Py3DEP without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/py3dep/issues>`__.

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

You can install Py3DEP using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``). Moreover, Py3DEP has an optional
dependency for using persistent caching, ``requests-cache``. We highly recommend installing
this package as it can significantly speed up send/receive queries. You don't have to change
anything in your code, since Py3DEP under-the-hood looks for ``requests-cache`` and if available,
it will automatically use persistent caching:

.. code-block:: console

    $ pip install py3dep

Alternatively, Py3DEP can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge py3dep

Quick start
-----------

You can use Py3DEP using command-line or as a Python library. The command-line interface
provides access to two functionality:

- Getting topographic data: You must create a ``geopandas.GeoDataFrame`` that contains
  the geometries of the target locations. This dataframe must have at least three columns:
  ``id``, ``res``, and ``geometry``. The ``id`` column is used as filenames for saving
  the obtained topographic data to a NetCDF (``.nc``) file. The ``res`` column must be
  the target resolution in meter. Then, you must save the dataframe to a file with extensions
  such as ``.shp`` or ``.gpkg`` (whatever that ``geopandas.read_file`` can read).
- Getting elevation: You must create a ``pandas.DataFrame`` that contains coordinates of the
  target locations. This dataframe must have at least two columns: ``x`` and ``y``. The elevations
  are obtained using ``airmap`` service in meters. The data are saved as a ``csv`` file with the
  same filename as the input file with an ``_elevation`` appended, e.g., ``coords_elevation.csv``.

.. code-block:: console

    $ py3dep --help
    Usage: py3dep [OPTIONS] COMMAND [ARGS]...

    Command-line interface for Py3DEP.

    Options:
    -h, --help  Show this message and exit.

    Commands:
    coords    Retrieve topographic data for a list of coordinates.
    geometry  Retrieve topographic data within geometries.

The ``coords`` sub-command is as follows:

.. code-block:: console

    $ py3dep coords -h
    Usage: py3dep coords [OPTIONS] FPATH

    Retrieve topographic data for a list of coordinates.

    FPATH: Path to a csv file with two columns named ``lon`` and ``lat``.

    Examples:
        $ cat coords.csv
        lon,lat
        -122.2493328,37.8122894
        $ py3dep coords coords.csv -q airmap -s topo_dir

    Options:
    -q, --query_source [airmap|tnm|tep]
                                    Source of the elevation data.
    -s, --save_dir PATH             Path to a directory to save the requested
                                    files. Extension for the outputs is either
                                    `.nc` for geometry or `.csv` for coords.

    -h, --help                      Show this message and exit.

And, the ``geometry`` sub-command is as follows:

.. code-block:: console

    $ py3dep geometry -h
    Usage: py3dep geometry [OPTIONS] FPATH

    Retrieve topographic data within geometries.

    FPATH: Path to a shapefile (.shp) or geopackage (.gpkg) file.
    This file must have three columns and contain a ``crs`` attribute:
        - ``id``: Feature identifiers that py3dep uses as the output netcdf/csv filenames.
        - ``res``: Target resolution in meters.
        - ``geometry``: A Polygon or MultiPloygon.

    Examples:
        $ py3dep geometry ny_geom.gpkg -l "Slope Map" -l DEM -s topo_dir

    Options:
    -l, --layers [DEM|Hillshade Gray|Aspect Degrees|Aspect Map|GreyHillshade_elevationFill|Hillshade Multidirectional|Slope Map|Slope Degrees|Hillshade Elevation Tinted|Height Ellipsoidal|Contour 25|Contour Smoothed 25]
                                    Target topographic data layers
    -s, --save_dir PATH             Path to a directory to save the requested
                                    files.Extension for the outputs is either
                                    `.nc` for geometry or `.csv` for coords.

    -h, --help                      Show this message and exit.


Now, let's see how we can use Py3DEP as a library.

Py3DEP accepts `Shapely <https://shapely.readthedocs.io/en/latest/manual.html>`__'s
Polygon or a bounding box (a tuple of length four) as an input geometry.
We can use PyNHD to get a watershed's geometry, then use it to get the DEM and slope
in meters/meters from Py3DEP using ``get_map`` function.

The ``get_map`` has a ``resolution`` argument that sets the target resolution
in meters. Note that the highest available resolution throughout the CONUS is about 10 m,
though higher resolutions are available in limited parts of the US. Note that the input
geometry can be in any valid spatial reference (``geo_crs`` argument). The ``crs`` argument,
however, is limited to ``CRS:84``, ``EPSG:4326``, and ``EPSG:3857`` since 3DEP only supports
these spatial references.

.. code-block:: python

    import py3dep
    from pynhd import NLDI

    geom = NLDI().get_basins("01031500").geometry[0]
    dem = py3dep.get_map("DEM", geom, resolution=30, geo_crs=4326, crs=3857)
    slope = py3dep.get_map("Slope Degrees", geom, resolution=30)
    slope = py3dep.deg2mpm(slope)

We can also use ``static_dem`` function to get the same DEM:

.. code-block:: python

    import xrspatial

    dem = py3dep.get_dem(geom, 30)
    slope = xrspatial.slope(dem.rio.reproject(5070))
    slope = py3dep.deg2mpm(slope)

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/dem_slope.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/3dep.ipynb
    :align: center

We can use `rioxarray <https://github.com/corteva/rioxarray>`__ package to save the obtained
dataset as a raster file:

.. code-block:: python

    import rioxarray

    dem.rio.to_raster("dem_01031500.tif")

Moreover, we can get the elevations of a set of x- and y- coordinates on a grid. For example,
let's get the minimum temperature data within this watershed from Daymet using PyDaymet then
add the elevation as a new variable to the dataset:

.. code-block:: python

    import pydaymet as daymet
    import xarray as xr
    import numpy as np

    clm = daymet.get_bygeom(geometry, ("2005-01-01", "2005-01-31"), variables="tmin")
    elev = py3dep.elevation_bygrid(clm.x.values, clm.y.values, clm.crs, clm.res[0] * 1000)
    attrs = clm.attrs
    clm = xr.merge([clm, elev])
    clm["elevation"] = clm.elevation.where(~np.isnan(clm.isel(time=0).tmin), drop=True)
    clm.attrs.update(attrs)

Now, let's get street network data using `osmnx <https://github.com/gboeing/osmnx>`__ package
and add elevation data for its nodes using ``elevation_bycoords`` function.

.. code-block:: python

    import osmnx as ox

    G = ox.graph_from_place("Piedmont, California, USA", network_type="drive")
    x, y = nx.get_node_attributes(G, "x").values(), nx.get_node_attributes(G, "y").values()
    elevation = py3dep.elevation_bycoords(zip(x, y), crs=4326)
    nx.set_node_attributes(G, dict(zip(G.nodes(), elevation)), "elevation")

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/street_elev.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/3dep.ipynb
    :align: center

We can get the elevation profile along a line at a given spacing using ``elevation_profile``
function. For example, let's get the elevation profile at 10-m spacing along the main flowline
of the upstream drainage area of a USGS station with ID ``01031500``:

.. code-block:: python

    import py3dep
    from pynhd import NLDI

    flw_main = NLDI().navigate_byid(
        fsource="nwissite",
        fid="USGS-01031500",
        navigation="upstreamMain",
        source="flowlines",
        distance=1000,
    )
    line = flw_main.geometry.unary_union
    elevation = py3dep.elevation_profile(line, 10)
