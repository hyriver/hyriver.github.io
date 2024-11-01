pygeoutils.geotools
===================

.. py:module:: pygeoutils.geotools

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.







Module Contents
---------------

.. py:class:: Coordinates

   Generate validated and normalized coordinates in WGS84.

   :Parameters: * **lon** (:class:`float` or :class:`list` of :class:`floats`) -- Longitude(s) in decimal degrees.
                * **lat** (:class:`float` or :class:`list` of :class:`floats`) -- Latitude(s) in decimal degrees.
                * **bounds** (:class:`tuple` of :class:`length 4`, *optional*) -- The bounding box to check of the input coordinates fall within.
                  Defaults to WGS84 bounds.

   .. rubric:: Examples

   >>> c = Coordinates([460, 20, -30], [80, 200, 10])
   >>> c.points.x.tolist()
   [100.0, -30.0]


   .. py:property:: points
      :type: geopandas.GeoSeries


      Get validate coordinate as a ``geopandas.GeoSeries``.


.. py:function:: break_lines(lines, points, tol = 0.0)

   Break lines at specified points at given direction.

   :Parameters: * **lines** (:class:`geopandas.GeoDataFrame`) -- Lines to break at intersection points.
                * **points** (:class:`geopandas.GeoDataFrame`) -- Points to break lines at. It must contain a column named ``direction``
                  with values ``up`` or ``down``. This column is used to determine which
                  part of the lines to keep, i.e., upstream or downstream of points.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  The default is 0.0.

   :returns: :class:`geopandas.GeoDataFrame` -- Original lines except for the parts that have been broken at the specified
             points.


.. py:function:: coords_list(coords)

   Convert a single coordinate or list of coordinates to a list of coordinates.

   :Parameters: **coords** (:class:`tuple` of :class:`list` of :class:`tuple`) -- Input coordinates

   :returns: :class:`list` of :class:`tuple` -- List of coordinates as ``[(x1, y1), ...]``.


.. py:function:: geo2polygon(geometry, geo_crs = None, crs = None)

   Convert a geometry to a Shapely's Polygon and transform to any CRS.

   :Parameters: * **geometry** (:class:`Polygon` or :class:`tuple` of :class:`length 4`) -- Polygon or bounding box (west, south, east, north).
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- Spatial reference of the input geometry, defaults to ``None``.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- Target spatial reference, defaults to ``None``.

   :returns: :class:`shapely.Polygon` or :class:`shapely.MultiPolygon` -- A (Multi)Polygon in the target CRS, if different from the input CRS.


.. py:function:: geometry_list(geometry)

   Convert input geometry to a list of Polygons, Points, or LineStrings.

   :Parameters: **geometry** (:class:`Polygon` or :class:`MultiPolygon` or :class:`tuple` of :class:`length 4` or :class:`list` of :class:`tuples` of :class:`length 2` or ``3``) -- Input geometry could be a ``(Multi)Polygon``, ``(Multi)LineString``,
                ``(Multi)Point``, a tuple/list of length 4 (west, south, east, north),
                or a list of tuples of length 2 or 3.

   :returns: :class:`list` -- A list of Polygons, Points, or LineStrings.


.. py:function:: geometry_reproject(geom, in_crs, out_crs)

   Reproject a geometry to another CRS.

   :Parameters: * **geom** (:class:`list` or :class:`tuple` or :class:`any shapely.GeometryType`) -- Input geometry could be a list of coordinates such as ``[(x1, y1), ...]``,
                  a bounding box like so ``(xmin, ymin, xmax, ymax)``, or any valid ``shapely``'s
                  geometry such as ``Polygon``, ``MultiPolygon``, etc..
                * **in_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Spatial reference of the input geometry
                * **out_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Target spatial reference

   :returns: :class:`same type as the input geometry` -- Transformed geometry in the target CRS.

   .. rubric:: Examples

   >>> from shapely import Point
   >>> point = Point(-7766049.665, 5691929.739)
   >>> geometry_reproject(point, 3857, 4326).xy
   (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))
   >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
   >>> geometry_reproject(bbox, 3857, 4326)
   (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)
   >>> coords = [(-7766049.665, 5691929.739)]
   >>> geometry_reproject(coords, 3857, 4326)
   [(-69.7636111130079, 45.44549114818127)]


.. py:function:: multi2poly(gdf)

   Convert multipolygons to polygon and fill holes, if any.

   .. rubric:: Notes

   This function tries to convert multipolygons to polygons by
   first checking if multiploygons can be directly converted using
   their exterior boundaries. If not, will try to remove very small
   sub-polygons that their area is less than 1% of the total area
   of the multipolygon. If this fails, the original multipolygon will
   be returned.

   :Parameters: **gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with (multi)polygons. This will be
                more accurate if the CRS is projected.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- A GeoDataFrame or GeoSeries with polygons (and multipolygons).


.. py:function:: nested_polygons(gdf)

   Get nested polygons in a GeoDataFrame.

   :Parameters: **gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with (multi)polygons.

   :returns: :class:`dict` -- A dictionary where keys are indices of larger polygons and
             values are a list of indices of smaller polygons that are
             contained within the larger polygons.


.. py:function:: query_indices(tree_gdf, input_gdf, predicate = 'intersects')

   Find the indices of the input_geo that intersect with the tree_geo.

   :Parameters: * **tree_gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- The tree geodataframe.
                * **input_gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- The input geodataframe.
                * **predicate** (:class:`str`, *optional*) -- The predicate to use for the query operation, defaults to ``intesects``.

   :returns: :class:`dict` -- A dictionary of the indices of the ``input_gdf`` that intersect with the
             ``tree_gdf``. Keys are the index of ``input_gdf`` and values are a list
             of indices of the intersecting ``tree_gdf``.


.. py:function:: snap2nearest(lines_gdf, points_gdf, tol)

   Find the nearest points on a line to a set of points.

   :Parameters: * **lines_gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Lines.
                * **points_gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Points to snap to lines.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  It must be greater than 0.0.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- Points snapped to lines.


