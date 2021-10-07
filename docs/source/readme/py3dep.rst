Py3DEP: Topographic data through 3DEP
-------------------------------------

.. image:: https://img.shields.io/pypi/v/py3dep.svg
    :target: https://pypi.python.org/pypi/py3dep
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/py3dep.svg
    :target: https://anaconda.org/conda-forge/py3dep
    :alt: Conda Version

.. image:: https://codecov.io/gh/cheginit/py3dep/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/cheginit/py3dep
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/py3dep.svg
    :target: https://pypi.python.org/pypi/py3dep
    :alt: Python Versions

.. image:: https://pepy.tech/badge/py3dep
    :target: https://pepy.tech/project/py3dep
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/cheginit/py3dep/badge
   :target: https://www.codefactor.io/repository/github/cheginit/py3dep
   :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

|

Features
--------

Py3DEP is a part of `HyRiver <https://github.com/cheginit/HyRiver>`__ software stack that
is designed to aid in watershed analysis through web services. This package provides
access to the `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`__
database which is a part of the
`National Map services <https://viewer.nationalmap.gov/services/>`__.
The 3DEP service has multi-resolution sources and depending on the user provided resolution,
the data is resampled on the server-side based on all the available data sources. Py3DEP returns
the requests as `xarray <https://xarray.pydata.org/en/stable>`__ dataset. Moreover,
under-the-hood, this package uses ``requests-cache`` for persistent caching that can improve
the performance significantly. The 3DEP web service includes the following layers:

- DEM
- Hillshade Gray
- Aspect Degrees
- Aspect Map
- GreyHillshade Elevation Fill
- Hillshade Multidirectional
- Slope Map
- Slope Degrees
- Hillshade Elevation Tinted
- Height Ellipsoidal
- Contour 25
- Contour Smoothed 25

Moreover, Py3DEP offers some additional utilities:

- ``elevation_bygrid``: For getting elevations of all the grid points in a 2D grid.
- ``elevation_bycoords``: For getting elevation of a list of ``x`` and ``y`` coordinates.
- ``deg2mpm``: For converting slope dataset from degree to meter per meter.

You can try using Py3DEP without installing it on you system by clicking on the binder badge
below the Py3DEP banner. A Jupyter notebook instance with the stack
pre-installed will be launched in your web browser and you can start coding!

Please note that since this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/cheginit/py3dep/issues>`__.


Installation
------------

You can install Py3DEP using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``). Moreover, Py3DEP has an optional
dependency for using persistent caching, ``requests-cache``. We highly recommend to install
this package as it can significantly speedup send/receive queries. You don't have to change
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

You can use Py3DEP using command-line or as a Python library. The commanda-line
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
    -q, --query_source [airmap|tnm]
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
    dem = py3dep.get_map("DEM", geom, resolution=30, geo_crs="epsg:4326", crs="epsg:3857")
    slope = py3dep.get_map("Slope Degrees", geom, resolution=30)
    slope = py3dep.deg2mpm(slope)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/dem_slope.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/3dep.ipynb
    :align: center

We can use `rioxarray <https://github.com/corteva/rioxarray>`__ package to save the obtained
dataset as a raster file:

.. code-block:: python

    import rioxarray

    dem.rio.to_raster("dem_01031500.tif")

Moreover, we can get the elevations of set of x- and y- coordinates on a grid. For example,
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

Now, let's get street network data using `osmnx <https://github.com/gboeing/osmnx>`_ package
and add elevation data for its nodes using ``elevation_bycoords`` function.

.. code-block:: python

    import osmnx as ox

    G = ox.graph_from_place("Piedmont, California, USA", network_type="drive")
    x, y = nx.get_node_attributes(G, "x").values(), nx.get_node_attributes(G, "y").values()
    elevation = py3dep.elevation_bycoords(zip(x, y), crs="epsg:4326")
    nx.set_node_attributes(G, dict(zip(G.nodes(), elevation)), "elevation")

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/street_elev.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/3dep.ipynb
    :align: center
