
PyGeoOGC: Retrieve Data from RESTful, WMS, and WFS Services
-----------------------------------------------------------

.. image:: https://img.shields.io/pypi/v/pygeoogc.svg
    :target: https://pypi.python.org/pypi/pygeoogc
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pygeoogc.svg
    :target: https://anaconda.org/conda-forge/pygeoogc
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/pygeoogc/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/pygeoogc
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pygeoogc.svg
    :target: https://pypi.python.org/pypi/pygeoogc
    :alt: Python Versions

.. image:: https://pepy.tech/badge/pygeoogc
    :target: https://pepy.tech/project/pygeoogc
    :alt: Downloads

|

.. image:: https://img.shields.io/badge/security-bandit-green.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. image:: https://www.codefactor.io/repository/github/hyriver/pygeoogc/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pygeoogc
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

PyGeoOGC is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package provides
general interfaces to web services that are based on
`ArcGIS RESTful <https://en.wikipedia.org/wiki/Representational_state_transfer>`__,
`WMS <https://en.wikipedia.org/wiki/Web_Map_Service>`__, and
`WFS <https://en.wikipedia.org/wiki/Web_Feature_Service>`__. Although
all these web services have limits on the number of features per request (e.g., 1000
object IDs for a RESTful request or 8 million pixels for a WMS request), PyGeoOGC, first, divides
the large requests into smaller chunks, and then returns the merged results.

Moreover, under the hood, PyGeoOGC uses
`AsyncRetriever <https://github.com/hyriver/async-retriever>`__
for making requests asynchronously with persistent caching. This improves the
reliability and speed of data retrieval significantly. AsyncRetriever caches all request/response
pairs and upon making an already cached request, it will retrieve the responses from the cache
if the server's response is unchanged.

You can control the request/response caching behavior and verbosity of the package
by setting the following environment variables:

* ``HYRIVER_CACHE_NAME``: Path to the caching SQLite database. It defaults to
  ``./cache/aiohttp_cache.sqlite``
* ``HYRIVER_CACHE_EXPIRE``: Expiration time for cached requests in seconds. It defaults to
  -1 (never expire).
* ``HYRIVER_CACHE_DISABLE``: Disable reading/writing from/to the cache. The default is false.
* ``HYRIVER_VERBOSE``: Enable verbose mode. The default is false.

For example, in your code before making any requests you can do:

.. code-block:: python

    import os

    os.environ["HYRIVER_CACHE_NAME"] = "path/to/aiohttp_cache.sqlite"
    os.environ["HYRIVER_CACHE_NAME_HTTP"] = "path/to/http_cache.sqlite"
    os.environ["HYRIVER_CACHE_EXPIRE"] = "3600"
    os.environ["HYRIVER_CACHE_DISABLE"] = "true"

There is also an inventory of URLs for some of these web services in form of a class called
``ServiceURL``. These URLs are in four categories: ``ServiceURL().restful``,
``ServiceURL().wms``, ``ServiceURL().wfs``, and ``ServiceURL().http``. These URLs provide you
with some examples of the services that PyGeoOGC supports. If you have success using PyGeoOGC with a web
service please consider submitting a request to be added to this URL inventory. You can get all
the URLs in the ``ServiceURL`` class by just printing it ``print(ServiceURL())``.

PyGeoOGC has three main classes:

* ``ArcGISRESTful``: This class can be instantiated by providing the target layer URL.
  For example, for getting Watershed Boundary Data we can use ``ServiceURL().restful.wbd``.
  By looking at the web service's
  `website <https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer>`_
  we see that there are nine layers. For example, 1 for 2-digit HU (Region), 6 for 12-digit HU
  (Subregion), and so on. We can pass the URL to the target layer directly, like this
  ``f"{ServiceURL().restful.wbd}/6"`` or as a separate argument via ``layer``.

  Afterward, we request for the data in two steps. First, we need to get
  the target object IDs using ``oids_bygeom`` (within a geometry), ``oids_byfield`` (specific
  field IDs), or ``oids_bysql`` (any valid SQL 92 WHERE clause) class methods. Then, we can get
  the target features using ``get_features`` class method. The returned response can be converted
  into a ``geopandas.GeoDataFrame`` using ``json2geodf`` function from
  `PyGeoUtils <https://github.com/hyriver/pygeoutils>`__.

* ``WMS``: Instantiation of this class requires at least 3 arguments: service URL, layer
  name(s), and output format. Additionally, target CRS and the web service version can be provided.
  Upon instantiation, we can use ``getmap_bybox`` method class to get the target raster data
  within a bounding box. The box can be in any valid CRS and if it is different from the default
  CRS, ``EPSG:4326``, it should be passed using ``box_crs`` argument. The service response can be
  converted into a ``xarray.Dataset`` using ``gtiff2xarray`` function from PyGeoUtils.

* ``WFS``: Instantiation of this class is similar to ``WMS``. The only difference is that
  only one layer name can be passed. Upon instantiation there are three ways to get the data:

  - ``getfeature_bybox``: Get all the target features within a bounding box in any valid CRS.
  - ``getfeature_byid``: Get all the target features based on the IDs. Note that two arguments
    should be provided: ``featurename``, and ``featureids``. You can get a list of valid feature
    names using ``get_validnames`` class method.
  - ``getfeature_byfilter``: Get the data based on any valid
    `CQL <https://docs.geoserver.org/latest/en/user/tutorials/cql/cql_tutorial.html>`__ filter.

  You can convert the returned response of this function to a ``GeoDataFrame`` using ``json2geodf``
  function from PyGeoUtils package.

PyGeoOGC also includes several utilities:

- ``streaming_download`` for downloading large files in parallel and in chunks, efficiently.
- ``traverse_json`` for traversing a nested JSON object.
- ``match_crs`` for reprojecting a geometry or bounding box to any valid CRS.

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

Furthermore, you can also try using PyGeoOGC without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pygeoogc/issues>`__.

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

You can install PyGeoOGC using ``pip``:

.. code-block:: console

    $ pip install pygeoogc

Alternatively, PyGeoOGC can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__
or `Mamba <https://github.com/conda-forge/miniforge>`__:

.. code-block:: console

    $ conda install -c conda-forge pygeoogc

Quick start
-----------

We can access
`NHDPlus HR <https://edits.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/NHDPlus_HR/MapServer>`__
via RESTful service,
`National Wetlands Inventory <https://www.fws.gov/wetlands/>`__ from WMS, and
`FEMA National Flood Hazard <https://www.fema.gov/national-flood-hazard-layer-nfhl>`__
via WFS. The output for these functions are of type ``requests.Response`` that
can be converted to ``GeoDataFrame`` or ``xarray.Dataset`` using
`PyGeoUtils <https://github.com/hyriver/pygeoutils>`__.

Let's start the National Map's NHDPlus HR web service. We can query the flowlines that are
within a geometry as follows:

.. code-block:: python

    from pygeoogc import ArcGISRESTful, WFS, WMS, ServiceURL
    import pygeoutils as geoutils
    from pynhd import NLDI

    basin_geom = NLDI().get_basins("01031500").geometry[0]

    hr = ArcGISRESTful(ServiceURL().restful.nhdplushr, 2, outformat="json")

    resp = hr.get_features(hr.oids_bygeom(basin_geom, "epsg:4326"))
    flowlines = geoutils.json2geodf(resp)

Note ``oids_bygeom`` has three additional arguments: ``sql_clause``, ``spatial_relation``,
and ``distance``. We can use ``sql_clause`` for passing any valid SQL WHERE clauses and
``spatial_relation`` for specifying the target predicate such as
intersect, contain, cross, etc. The default predicate is intersect
(``esriSpatialRelIntersects``). Additionally, we can use ``distance`` for specifying the buffer
distance from the input geometry for getting features.

We can also submit a query based on IDs of any valid field in the database. If the measure
property is desired you can pass ``return_m`` as ``True`` to the ``get_features`` class method:

.. code-block:: python

    oids = hr.oids_byfield("PERMANENT_IDENTIFIER", ["103455178", "103454362", "103453218"])
    resp = hr.get_features(oids, return_m=True)
    flowlines = geoutils.json2geodf(resp)

Additionally, any valid SQL 92 WHERE clause can be used. For more details look
`here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__.
For example, let's limit our first request to only include catchments with
areas larger than 0.5 sqkm.

.. code-block:: python

    oids = hr.oids_bygeom(basin_geom, geo_crs="epsg:4326", sql_clause="AREASQKM > 0.5")
    resp = hr.get_features(oids)
    catchments = geoutils.json2geodf(resp)

A WMS-based example is shown below:

.. code-block:: python

    wms = WMS(
        ServiceURL().wms.fws,
        layers="0",
        outformat="image/tiff",
        crs="epsg:3857",
    )
    r_dict = wms.getmap_bybox(
        basin_geom.bounds,
        1e3,
        box_crs="epsg:4326",
    )
    wetlands = geoutils.gtiff2xarray(r_dict, basin_geom, "epsg:4326")

Query from a WFS-based web service can be done either within a bounding box or using
any valid `CQL filter <https://docs.geoserver.org/stable/en/user/tutorials/cql/cql_tutorial.html>`__.

.. code-block:: python

    wfs = WFS(
        ServiceURL().wfs.fema,
        layer="public_NFHL:Base_Flood_Elevations",
        outformat="esrigeojson",
        crs="epsg:4269",
    )
    r = wfs.getfeature_bybox(basin_geom.bounds, box_crs="epsg:4326")
    flood = geoutils.json2geodf(r.json(), "epsg:4269", "epsg:4326")

    layer = "wmadata:huc08"
    wfs = WFS(
        ServiceURL().wfs.waterdata,
        layer=layer,
        outformat="application/json",
        version="2.0.0",
        crs="epsg:4269",
    )
    r = wfs.getfeature_byfilter(f"huc8 LIKE '13030%'")
    huc8 = geoutils.json2geodf(r.json(), "epsg:4269", "epsg:4326")

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/sql_clause.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/webservices.ipynb

