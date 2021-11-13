:py:mod:`pygeoogc.utils`
========================

.. py:module:: pygeoogc.utils

.. autoapi-nested-parse::

   Some utilities for PyGeoOGC.



Module Contents
---------------

.. py:class:: ESRIGeomQuery

   Generate input geometry query for ArcGIS RESTful services.

   :Parameters: * **geometry** (:class:`tuple` or :class:`sgeom.Polygon` or :class:`sgeom.Point` or :class:`sgeom.LineString`) -- The input geometry which can be a point (x, y), a list of points [(x, y), ...],
                  bbox (xmin, ymin, xmax, ymax), or a Shapely's sgeom.Polygon.
                * **wkid** (:class:`int`) -- The Well-known ID (WKID) of the geometry's spatial reference e.g., for EPSG:4326,
                  4326 should be passed. Check
                  `ArcGIS <https://developers.arcgis.com/rest/services-reference/geographic-coordinate-systems.htm>`__
                  for reference.

   .. py:method:: bbox(self)

      Query for a bbox.


   .. py:method:: multipoint(self)

      Query for a multi-point.


   .. py:method:: point(self)

      Query for a point.


   .. py:method:: polygon(self)

      Query for a polygon.


   .. py:method:: polyline(self)

      Query for a polyline.



.. py:class:: RetrySession(retries = 3, backoff_factor = 0.3, status_to_retry = (500, 502, 504), prefixes = ('https://', ), cache_name = None)

   Configures the passed-in session to retry on failed requests.

   The fails can be due to connection errors, specific HTTP response
   codes and 30X redirections. The code is was originally based on:
   https://github.com/bustawin/retry-requests

   :Parameters: * **retries** (:class:`int`, *optional*) -- The number of maximum retries before raising an exception, defaults to 5.
                * **backoff_factor** (:class:`float`, *optional*) -- A factor used to compute the waiting time between retries, defaults to 0.5.
                * **status_to_retry** (:class:`tuple`, *optional*) -- A tuple of status codes that trigger the reply behaviour, defaults to (500, 502, 504).
                * **prefixes** (:class:`tuple`, *optional*) -- The prefixes to consider, defaults to ("http://", "https://")
                * **cache_name** (:class:`str`, *optional*) -- Path to a folder for caching the session, default to None which uses
                  system's temp directory.

   .. py:method:: get(self, url, payload = None, headers = None)

      Retrieve data from a url by GET and return the Response.


   .. py:method:: post(self, url, payload = None, headers = None)

      Retrieve data from a url by POST and return the Response.



.. py:function:: bbox_decompose(bbox, resolution, box_crs = DEF_CRS, max_px = 8000000)

   Split the bounding box vertically for WMS requests.

   :Parameters: * **bbox** (:class:`tuple`) -- A bounding box; (west, south, east, north)
                * **resolution** (:class:`float`) -- The target resolution for a WMS request in meters.
                * **box_crs** (:class:`str`, *optional*) -- The spatial reference of the input bbox, default to EPSG:4326.
                * **max_px** (:class:`int`, :class:`opitonal`) -- The maximum allowable number of pixels (width x height) for a WMS requests,
                  defaults to 8 million based on some trial-and-error.

   :returns: :class:`list` of :class:`tuples` -- Each tuple includes the following elements:

             * Tuple of length 4 that represents a bounding box (west, south, east, north) of a cell,
             * A label that represents cell ID starting from bottom-left to top-right, for example a
               2x2 decomposition has the following labels::

               |---------|---------|
               |         |         |
               |   0_1   |   1_1   |
               |         |         |
               |---------|---------|
               |         |         |
               |   0_0   |   1_0   |
               |         |         |
               |---------|---------|

             * Raster width of a cell,
             * Raster height of a cell.


.. py:function:: bbox_resolution(bbox, resolution, bbox_crs = DEF_CRS)

   Image size of a bounding box WGS84 for a given resolution in meters.

   :Parameters: * **bbox** (:class:`tuple`) -- A bounding box in WGS84 (west, south, east, north)
                * **resolution** (:class:`float`) -- The resolution in meters
                * **bbox_crs** (:class:`str`, *optional*) -- The spatial reference of the input bbox, default to EPSG:4326.

   :returns: :class:`tuple` -- The width and height of the image


.. py:function:: check_bbox(bbox)

   Check if an input inbox is a tuple of length 4.


.. py:function:: check_response(resp)

   Extract error message from a response, if any.


.. py:function:: match_crs(geom, in_crs, out_crs)

   Reproject a geometry to another CRS.

   :Parameters: * **geom** (:class:`list` or :class:`tuple` or :class:`geometry`) -- Input geometry which could be a list of coordinates such as ``[(x1, y1), ...]``,
                  a bounding box like so ``(xmin, ymin, xmax, ymax)``, or any valid ``shapely``'s
                  geometry such as sgeom.Polygon, sgeom.MultiPolygon, etc..
                * **in_crs** (:class:`str`) -- Spatial reference of the input geometry
                * **out_crs** (:class:`str`) -- Target spatial reference

   :returns: :class:`sgeom.LineString`, :class:`sgeom.MultiLineString`, :class:`sgeom.Polygon`, :class:`sgeom.MultiPolygon`, :class:`sgeom.Point`, or :class:`sgeom.MultiPoint` -- Input geometry in the specified CRS.

   .. rubric:: Examples

   >>> from pygeoogc.utils import match_crs
   >>> from shapely.geometry import Point
   >>> point = Point(-7766049.665, 5691929.739)
   >>> match_crs(point, "epsg:3857", "epsg:4326").xy
   (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))
   >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
   >>> match_crs(bbox, "epsg:3857", "epsg:4326")
   (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)
   >>> coords = [(-7766049.665, 5691929.739)]
   >>> match_crs(coords, "epsg:3857", "epsg:4326")
   [(-69.7636111130079, 45.44549114818127)]


.. py:function:: traverse_json(obj, path)

   Extract an element from a JSON file along a specified path.

   This function is based on `bcmullins <https://bcmullins.github.io/parsing-json-python/>`__.

   :Parameters: * **obj** (:class:`dict`) -- The input json dictionary
                * **path** (:class:`list`) -- The path to the requested element

   :returns: :class:`list` -- The items founds in the JSON

   .. rubric:: Examples

   >>> from pygeoogc.utils import traverse_json
   >>> data = [{
   ...     "employees": [
   ...         {"name": "Alice", "role": "dev", "nbr": 1},
   ...         {"name": "Bob", "role": "dev", "nbr": 2}],
   ...     "firm": {"name": "Charlie's Waffle Emporium", "location": "CA"},
   ... },]
   >>> traverse_json(data, ["employees", "name"])
   [['Alice', 'Bob']]


