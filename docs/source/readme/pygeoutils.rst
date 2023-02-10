
PyGeoUtils: Utilities for (Geo)JSON and (Geo)TIFF Conversion
------------------------------------------------------------

.. image:: https://img.shields.io/pypi/v/pygeoutils.svg
    :target: https://pypi.python.org/pypi/pygeoutils
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pygeoutils.svg
    :target: https://anaconda.org/conda-forge/pygeoutils
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/pygeoutils/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/pygeoutils
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pygeoutils.svg
    :target: https://pypi.python.org/pypi/pygeoutils
    :alt: Python Versions

.. image:: https://pepy.tech/badge/pygeoutils
    :target: https://pepy.tech/project/pygeoutils
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/hyriver/pygeoutils/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pygeoutils
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

PyGeoUtils is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
utilities for manipulating (Geo)JSON and (Geo)TIFF responses from web services.
These utilities are:

- ``Coordinates``: Generate validated and normalized coordinates in WGS84.
- ``GeoBSpline``: Create B-spline from a ``geopandas.GeoDataFrame`` of points.
- ``arcgis2geojson``: Convert ESRIGeoJSON format to GeoJSON.
- ``break_lines``: Break lines at specified points in a given direction.
- ``gtiff2xarray``: Convert (Geo)Tiff byte responses to ``xarray.Dataset``.
- ``json2geodf``: Create ``geopandas.GeoDataFrame`` from (Geo)JSON responses
- ``snap2nearest``: Find the nearest points on a line to a set of points.
- ``xarray2geodf``: Vectorize a ``xarray.DataArray`` to a ``geopandas.GeoDataFrame``.
- ``geodf2xarray``: Rasterize a ``geopandas.GeoDataFrame`` to a ``xarray.DataArray``.
- ``xarray_geomask``: Mask a ``xarray.Dataset`` based on a geometry.
- ``query_indices``: a wrapper around
  ``geopandas.sindex.query_bulk``. However, instead of returning an array of
  positional indices, it returns a dictionary of indices where keys are the
  indices of the input geometry and values are a list of indices of the
  tree geometries that intersect with the input geometry.
- ``nested_polygons``: Determining nested (multi)polygons in a ``geopandas.GeoDataFrame``.

All these functions handle all necessary CRS transformations.

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

You can also try using PyGeoUtils without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pygeoutils/issues>`__.

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

You can install PyGeoUtils using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``).

.. code-block:: console

    $ pip install pygeoutils

Alternatively, PyGeoUtils can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pygeoutils

Quick start
-----------

To demonstrate the capabilities of PyGeoUtils let's use
`PyGeoOGC <https://github.com/hyriver/pygeoogc>`__ to access
`National Wetlands Inventory <https://www.fws.gov/wetlands/>`__ from WMS, and
`FEMA National Flood Hazard <https://www.fema.gov/national-flood-hazard-layer-nfhl>`__
via WFS, then convert the output to ``xarray.Dataset`` and ``GeoDataFrame``, respectively.

.. code-block:: python

    import pygeoutils as geoutils
    from pygeoogc import WFS, WMS, ServiceURL
    from shapely.geometry import Polygon


    geometry = Polygon(
        [
            [-118.72, 34.118],
            [-118.31, 34.118],
            [-118.31, 34.518],
            [-118.72, 34.518],
            [-118.72, 34.118],
        ]
    )
    crs = "epsg:4326"

    wms = WMS(
        ServiceURL().wms.mrlc,
        layers="NLCD_2011_Tree_Canopy_L48",
        outformat="image/geotiff",
        crs=crs,
    )
    r_dict = wms.getmap_bybox(
        geometry.bounds,
        1e3,
        box_crs=crs,
    )
    canopy = geoutils.gtiff2xarray(r_dict, geometry, crs)

    mask = canopy > 60
    canopy_gdf = geoutils.xarray2geodf(canopy, "float32", mask)

    url_wfs = "https://hazards.fema.gov/gis/nfhl/services/public/NFHL/MapServer/WFSServer"
    wfs = WFS(
        url_wfs,
        layer="public_NFHL:Base_Flood_Elevations",
        outformat="esrigeojson",
        crs="epsg:4269",
    )
    r = wfs.getfeature_bybox(geometry.bounds, box_crs=crs)
    flood = geoutils.json2geodf(r.json(), "epsg:4269", crs)
