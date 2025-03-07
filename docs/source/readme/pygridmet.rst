
PyGridMET: Daily climate data through GridMET
---------------------------------------------

.. image:: https://img.shields.io/pypi/v/pygridmet.svg
    :target: https://pypi.python.org/pypi/pygridmet
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pygridmet.svg
    :target: https://anaconda.org/conda-forge/pygridmet
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/pygridmet/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/pygridmet
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pygridmet.svg
    :target: https://pypi.python.org/pypi/pygridmet
    :alt: Python Versions

.. image:: https://static.pepy.tech/badge/pygridmet
    :target: https://pepy.tech/project/pygridmet
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/hyriver/pygridmet/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pygridmet
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

Features
--------

PyGridMET is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
access to daily climate data over contermonious US (CONUS) from
`GridMET <https://www.climatologylab.org/gridmet.html>`__ database using NetCDF
Subset Service (NCSS). Both single pixel (using ``get_bycoords`` function) and gridded data (using
``get_bygeom``) are supported which are returned as
``pandas.DataFrame`` and ``xarray.Dataset``, respectively.

Both ``get_bygeom`` and ``get_bycoords`` functions save the intermediate files
returned by the web service in a local cache folder (``./cache`` in the current
directory). The cache folder is created automatically when the functions are
called for the first time. The cache folder is used to store the intermediate
files to avoid re-downloading them. These two functions allow modifying the
web service calls via two options:

- ``conn_timeout``: Sets the connection timeout in seconds. The default value
  is 5 minutes. This can be increaseed for larger requests. If running these
  functions fails with a connection timeout error, try increasing this value.
- ``validate_filesize``: If ``True``, the functions compares the file size
  of the previously cached files in the ``./cache`` folder, if they exist, with
  their size on the remote server. If the sizes do not match, the cached files are
  removed and they will be re-download. By default this is set to ``False`` since
  the files on the server rarely change. So, if a request has already been cached
  there shouldn't be a need for re-donwloading them from scratch. However, if you
  suspect that the files on the server have changed or the functions fails to process
  the cached files, you can set this to ``True`` or manually delete the cached
  files in the ``./cache`` folder.

You can find some example notebooks
`here <https://github.com/hyriver/HyRiver-examples>`__.
You can also try using PyGridMET without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pygridmet/issues>`__.

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

You can install PyGridMET using ``pip`` as follows:

.. code-block:: console

    $ pip install pygridmet

Alternatively, PyGridMET can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pygridmet

Quick start
-----------

You can use PyGridMET using command-line or as a Python library. The commanda-line
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

    $ pygridmet -h
    Usage: pygridmet [OPTIONS] COMMAND [ARGS]...

    Command-line interface for PyGridMET.

    Options:
    -h, --help  Show this message and exit.

    Commands:
    coords    Retrieve climate data for a list of coordinates.
    geometry  Retrieve climate data for a dataframe of geometries.

The ``coords`` sub-command is as follows:

.. code-block:: console

    $ pygridmet coords -h
    Usage: pygridmet coords [OPTIONS] FPATH

    Retrieve climate data for a list of coordinates.

    FPATH: Path to a csv file with four columns:
        - ``id``: Feature identifiers that gridmet uses as the output netcdf filenames.
        - ``start``: Start time.
        - ``end``: End time.
        - ``lon``: Longitude of the points of interest.
        - ``lat``: Latitude of the points of interest.
        - ``snow``: (optional) Separate snowfall from precipitation, default is ``False``.

    Examples:
        $ cat coords.csv
        id,lon,lat,start,end
        california,-122.2493328,37.8122894,2012-01-01,2014-12-31
        $ pygridmet coords coords.csv -v pr -v tmmn

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

    $ pygridmet geometry -h
    Usage: pygridmet geometry [OPTIONS] FPATH

    Retrieve climate data for a dataframe of geometries.

    FPATH: Path to a shapefile (.shp) or geopackage (.gpkg) file.
    This file must have four columns and contain a ``crs`` attribute:
        - ``id``: Feature identifiers that gridmet uses as the output netcdf filenames.
        - ``start``: Start time.
        - ``end``: End time.
        - ``geometry``: Target geometries.
        - ``snow``: (optional) Separate snowfall from precipitation, default is ``False``.

    Examples:
        $ pygridmet geometry geo.gpkg -v pr -v tmmn

    Options:
    -v, --variables TEXT  Target variables. You can pass this flag multiple
                            times for multiple variables.
    -s, --save_dir PATH   Path to a directory to save the requested files.
                            Extension for the outputs is .nc for geometry and .csv
                            for coords.
    --disable_ssl         Pass to disable SSL certification verification.
    -h, --help            Show this message and exit.

Now, let's see how we can use PyGridMET as a library.

PyGridMET offers two functions for getting climate data; ``get_bycoords`` and ``get_bygeom``.
The arguments of these functions are identical except the first argument where the latter
should be polygon and the former should be a coordinate (a tuple of length two as in (x, y)).
The input geometry or coordinate can be in any valid CRS (defaults to ``EPSG:4326``). The
``dates`` argument can be either a tuple of length two like ``(start_str, end_str)`` or a list of
years like ``[2000, 2005]``. It is noted that both functions have a ``snow`` flag for separating
snow from precipitation using
`Martinez and Gupta (2010) <https://doi.org/10.1029/2009WR008294>`__ method.

We can get a dataframe of available variables and their info by calling
``GridMET().gridmet_table``:

+----------------------------------------+------------+------------------------------+
| Variable                               | Abbr       | Unit                         |
+========================================+============+==============================+
| Precipitation                          | ``pr``     | mm                           |
+----------------------------------------+------------+------------------------------+
| Maximum Relative Humidity              | ``rmax``   | %                            |
+----------------------------------------+------------+------------------------------+
| Minimum Relative Humidity              | ``rmin``   | %                            |
+----------------------------------------+------------+------------------------------+
| Specific Humidity                      | ``sph``    | kg/kg                        |
+----------------------------------------+------------+------------------------------+
| Surface Radiation                      | ``srad``   | W/m2                         |
+----------------------------------------+------------+------------------------------+
| Wind Direction                         | ``th``     | Degrees Clockwise from north |
+----------------------------------------+------------+------------------------------+
| Minimum Air Temperature                | ``tmmn``   | K                            |
+----------------------------------------+------------+------------------------------+
| Maximum Air Temperature                | ``tmmx``   | K                            |
+----------------------------------------+------------+------------------------------+
| Wind Speed                             | ``vs``     | m/s                          |
+----------------------------------------+------------+------------------------------+
| Burning Index                          | ``bi``     | Dimensionless                |
+----------------------------------------+------------+------------------------------+
| Fuel Moisture (100-hr)                 | ``fm100``  | %                            |
+----------------------------------------+------------+------------------------------+
| Fuel Moisture (1000-hr)                | ``fm1000`` | %                            |
+----------------------------------------+------------+------------------------------+
| Energy Release Component               | ``erc``    | Dimensionless                |
+----------------------------------------+------------+------------------------------+
| Reference Evapotranspiration (Alfalfa) | ``etr``    | mm                           |
+----------------------------------------+------------+------------------------------+
| Reference Evapotranspiration (Grass)   | ``pet``    | mm                           |
+----------------------------------------+------------+------------------------------+
| Vapor Pressure Deficit                 | ``vpd``    | kPa                          |
+----------------------------------------+------------+------------------------------+

.. code-block:: python

    from pynhd import NLDI
    import pygridmet as gridmet

    geometry = NLDI().get_basins("01031500").geometry[0]

    var = ["pr", "tmmn"]
    dates = ("2000-01-01", "2000-06-30")

    daily = gridmet.get_bygeom(geometry, dates, variables=var, snow=True)

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/gridmet_grid.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/gridmet.ipynb

If the input geometry (or coordinate) is in a CRS other than ``EPSG:4326``, we should pass
it to the functions.

.. code-block:: python

    coords = (-1431147.7928, 318483.4618)
    crs = 3542
    dates = ("2000-01-01", "2006-12-31")
    data = gridmet.get_bycoords(coords, dates, variables=var, loc_crs=crs)

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/gridmet_loc.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/gridmet.ipynb

Additionally, the ``get_bycoords`` function accepts a list of coordinates and by setting the
``to_xarray`` flag to ``True`` it can return the results as a ``xarray.Dataset`` instead of
a ``pandas.DataFrame``:

.. code-block:: python

    coords = [(-94.986, 29.973), (-95.478, 30.134)]
    idx = ["P1", "P2"]
    clm_ds = gridmet.get_bycoords(coords, range(2000, 2021), coords_id=idx, to_xarray=True)
