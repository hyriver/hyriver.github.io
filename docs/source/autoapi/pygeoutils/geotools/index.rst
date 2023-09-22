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

   >>> c = Coordinates([460, 20, -30], [80, 200, 10])
   >>> c.points.x.tolist()
   [100.0, -30.0]

   .. py:property:: points
      :type: geopandas.GeoSeries

      Get validate coordinate as a ``geopandas.GeoSeries``.


.. py:class:: GeoBSpline(points, n_pts, degree = 3)


   Create B-spline from a GeoDataFrame of points.

   :Parameters: * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Input points as a ``GeoDataFrame`` or ``GeoSeries``. The results
                  will be more accurate if the CRS is projected.
                * **npts_sp** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the spline. Should be less than the number of points and
                  greater than 1. Default is 3.

   .. rubric:: Examples

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
   >>> sp = GeoBSpline(pts.to_crs(3857), 5).spline
   >>> pts_sp = gpd.GeoSeries(gpd.points_from_xy(sp.x, sp.y, crs=3857))
   >>> pts_sp = pts_sp.to_crs(4326)
   >>> list(zip(pts_sp.x, pts_sp.y))
   [(-97.06138, 32.837),
   (-97.06132, 32.83575),
   (-97.06126, 32.83450),
   (-97.06123, 32.83325),
   (-97.06127, 32.83200)]

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


.. py:function:: bspline_curvature(bspline, konts)

   Compute the curvature of a B-spline curve.

   .. rubric:: Notes

   The formula for the curvature of a B-spline curve is:

   .. math::

       \kappa = \frac{\dot{x}\ddot{y} - \ddot{x}\dot{y}}{(\dot{x}^2 + \dot{y}^2)^{3/2}}

   where :math:`\dot{x}` and :math:`\dot{y}` are the first derivatives of the
   B-spline curve and :math:`\ddot{x}` and :math:`\ddot{y}` are the second
   derivatives of the B-spline curve. Also, the radius of curvature is:

   .. math::

       \rho = \frac{1}{|\kappa|}

   :Parameters: * **bspline** (:class:`scipy.interpolate.BSpline`) -- B-spline curve.
                * **konts** (:class:`float`) -- Knots of the B-spline curve to compute the curvature at.

   :returns: * **phi** (:class:`numpy.ndarray`) -- Angle of the tangent of the B-spline curve.
             * **curvature** (:class:`numpy.ndarray`) -- Curvature of the B-spline curve.
             * **radius** (:class:`numpy.ndarray`) -- Radius of curvature of the B-spline curve.


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

   Convert input geometry to a list of polygons, points, or lines.


.. py:function:: geometry_reproject(geom, in_crs, out_crs)

   Reproject a geometry to another CRS.

   :Parameters: * **geom** (:class:`list` or :class:`tuple` or :class:`any shapely.geometry`) -- Input geometry could be a list of coordinates such as ``[(x1, y1), ...]``,
                  a bounding box like so ``(xmin, ymin, xmax, ymax)``, or any valid ``shapely``'s
                  geometry such as ``Polygon``, ``MultiPolygon``, etc..
                * **in_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Spatial reference of the input geometry
                * **out_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`) -- Target spatial reference

   :returns: :class:`same type as the input geometry` -- Transformed geometry in the target CRS.

   .. rubric:: Examples

   >>> from shapely.geometry import Point
   >>> point = Point(-7766049.665, 5691929.739)
   >>> geometry_reproject(point, 3857, 4326).xy
   (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))
   >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
   >>> geometry_reproject(bbox, 3857, 4326)
   (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)
   >>> coords = [(-7766049.665, 5691929.739)]
   >>> geometry_reproject(coords, 3857, 4326)
   [(-69.7636111130079, 45.44549114818127)]


.. py:function:: make_bspline(x, y, n_pts, k = 3)

   Create a B-spline curve from a set of points.

   :Parameters: * **x** (:class:`numpy.ndarray`) -- x-coordinates of the points.
                * **y** (:class:`numpy.ndarray`) -- y-coordinates of the points.
                * **n_pts** (:class:`int`) -- Number of points in the output spline curve.
                * **k** (:class:`int`, *optional*) -- Degree of the spline. Should be an odd number less than the number of
                  points and greater than 1. Default is 3.

   :returns: :class:`Spline` -- A Spline object with ``x``, ``y``, ``phi``, ``radius``, ``distance``,
             and ``line`` attributes. The ``line`` attribute returns the B-spline
             as a shapely.LineString.


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


.. py:function:: smooth_linestring(line, crs, n_pts, degree = 3)

   Smooth a line using B-spline interpolation.

   :Parameters: * **line** (:class:`shapely.LineString`) -- Line to smooth. Note that ``MultiLineString`` is not supported.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- CRS of the input line. It must be a projected CRS.
                * **n_pts** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the spline. Should be less than the number of points and
                  greater than 1. Default is 3.

   :returns: :class:`Spline` -- A Spline object with ``x``, ``y``, ``phi``, ``radius``, ``distance``,
             and ``line`` attributes. The ``line`` attribute returns the B-spline
             as a shapely.LineString.

   .. rubric:: Examples

   >>> import pygeoutils as pgu
   >>> import geopandas as gpd
   >>> import shapely
   >>> line = shapely.geometry.LineString(
   ...     [
   ...         (-97.06138, 32.837),
   ...         (-97.06133, 32.836),
   ...         (-97.06124, 32.834),
   ...         (-97.06127, 32.832),
   ...     ]
   ... )
   >>> line = pgu.geometry_reproject(line, 4326, 5070)
   >>> sp = pgu.smooth_linestring(line, 5070, 5)
   >>> line_sp = pgu.geometry_reproject(sp.line, 5070, 4326)
   >>> list(zip(*line_sp.xy))
   [(-97.06138, 32.837),
   (-97.06132, 32.83575),
   (-97.06126, 32.83450),
   (-97.06123, 32.83325),
   (-97.06127, 32.83200)]


.. py:function:: snap2nearest(lines, points, tol)

   Find the nearest points on a line to a set of points.

   :Parameters: * **lines** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Lines.
                * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Points to snap to lines.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  It must be greater than 0.0.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- Points snapped to lines.


