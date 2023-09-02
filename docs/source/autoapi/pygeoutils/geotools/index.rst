:py:mod:`pygeoutils.geotools`
=============================

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

   >>> from pygeoutils import Coordinates
   >>> c = Coordinates([460, 20, -30], [80, 200, 10])
   >>> c.points.x.tolist()
   [100.0, -30.0]

   .. py:property:: points
      :type: geopandas.GeoSeries

      Get validate coordinate as a ``geopandas.GeoSeries``.


.. py:class:: GeoBSpline(points, npts_sp, degree = 3)


   Create B-spline from a geo-dataframe of points.

   :Parameters: * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Input points as a ``GeoDataFrame`` or ``GeoSeries`` in a projected CRS.
                * **npts_sp** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the spline. Should be less than the number of points and
                  greater than 1. Default is 3.

   .. rubric:: Examples

   >>> from pygeoutils import GeoBSpline
   >>> import geopandas as gpd
   >>> xl, yl = zip(
   ...     *[
   ...         (-97.06138, 32.837),
   ...         (-97.06133, 32.836),
   ...         (-97.06124, 32.834),
   ...         (-97.06127, 32.832),
   ...     ]
   ... )
   >>> pts = gpd.GeoSeries(gpd.points_from_xy(xl, yl, crs=4326))
   >>> sp = GeoBSpline(pts.to_crs("epsg:3857"), 5).spline
   >>> pts_sp = gpd.GeoSeries(gpd.points_from_xy(sp.x, sp.y, crs="epsg:3857"))
   >>> pts_sp = pts_sp.to_crs(4326)
   >>> list(zip(pts_sp.x, pts_sp.y))
   [(-97.06138, 32.837),
   (-97.06135, 32.83629),
   (-97.06131, 32.83538),
   (-97.06128, 32.83434),
   (-97.06127, 32.83319)]

   .. py:property:: spline
      :type: Spline

      Get the spline as a ``Spline`` object.


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

   Get a list of polygons, points, and lines from a geometry.


.. py:function:: multi2poly(gdf)

   Convert multipolygons to polygon and fill holes, if any.

   .. rubric:: Notes

   This function tries to convert multipolygons to polygons by
   first checking if multiploygons can be directly converted using
   their exterior boundaries. If not, will try to remove those small
   sub-polygons that their area is less than 1% of the total area
   of the multipolygon. If this fails, the original multipolygon will
   be returned.

   :Parameters: **gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with (multi)polygons in a projected
                coordinate system.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- A GeoDataFrame or GeoSeries with polygons.


.. py:function:: nested_polygons(gdf)

   Get nested polygons in a GeoDataFrame.

   :Parameters: **gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with (multi)polygons.

   :returns: :class:`dict` -- A dictionary where keys are indices of larger ploygons and
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


.. py:function:: snap2nearest(lines, points, tol)

   Find the nearest points on a line to a set of points.

   :Parameters: * **lines** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Lines.
                * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Points to snap to lines.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  It must be greater than 0.0.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- Points snapped to lines.


