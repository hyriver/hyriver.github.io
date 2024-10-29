pygeoutils.smoothing
====================

.. py:module:: pygeoutils.smoothing

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.







Module Contents
---------------

.. py:class:: GeoSpline(points, n_pts, degree = 3, smoothing = None)

   Create a parametric spline from a GeoDataFrame of points.

   :Parameters: * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` or :term:`array-like <array_like>` of :class:`shapely.Point`) -- Input points as a ``GeoDataFrame``, ``GeoSeries``, or array-like of
                  ``shapely.Point``. The results will be more accurate if the CRS is projected.
                * **npts_sp** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the smoothing spline. Must be
                  1 <= ``degree`` <= 5. Default to 3 which is a cubic spline.
                * **smoothing** (:class:`float` or :obj:`None`, *optional*) -- Smoothing factor is used for determining the number of knots.
                  This arg controls the tradeoff between closeness and smoothness of fit.
                  Larger ``smoothing`` means more smoothing while smaller values of
                  ``smoothing`` indicates less smoothing. If None (default), smoothing
                  is done with all points.

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
   >>> sp = GeoSpline(pts.to_crs(3857), 5).spline
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


.. py:function:: anchored_smoothing(line, npts = None, sigma = None)

   Fit a cubic spline through a line while anchoring the ends.

   :Parameters: * **line** (:class:`shapey.LineString`) -- Line to smooth.
                * **npts** (:class:`int`, *optional*) -- Number of points for uniform spacing of the generated spline, defaults
                  to ``None``, i.e., the number of points along the original line.
                * **sigma** (:class:`float`, *optional*) -- Standard deviation for Gaussian kernel used for filtering noise in the line
                  before fitting the spline. Defaults to ``None``, i.e., no filtering.

   :returns: :class:`numpy.ndarray` -- The fitted cubic spline.


.. py:function:: line_curvature(line, k = 3, s = None)

   Compute the curvature of a LineString.

   .. rubric:: Notes

   The formula for the curvature of a Spline curve is:

   .. math::

       \kappa = \frac{\dot{x}\ddot{y} - \ddot{x}\dot{y}}{(\dot{x}^2 + \dot{y}^2)^{3/2}}

   where :math:`\dot{x}` and :math:`\dot{y}` are the first derivatives of the
   Spline curve and :math:`\ddot{x}` and :math:`\ddot{y}` are the second
   derivatives of the Spline curve. Also, the radius of curvature is:

   .. math::

       \rho = \frac{1}{|\kappa|}

   :Parameters: * **line** (:class:`shapely.LineString`) -- Line to compute the curvature at.
                * **k** (:class:`int`, *optional*) -- Degree of the smoothing spline. Must be
                  1 <= ``k`` <= 5. Default to 3 which is a cubic spline.
                * **s** (:class:`float` or :obj:`None`, *optional*) -- Smoothing factor is used for determining the number of knots.
                  This arg controls the tradeoff between closeness and smoothness of fit.
                  Larger ``s`` means more smoothing while smaller values of ``s`` indicates
                  less smoothing. If None (default), smoothing is done with all data points.

   :returns: * **phi** (:class:`numpy.ndarray`) -- Angle of the tangent of the Spline curve.
             * **curvature** (:class:`numpy.ndarray`) -- Curvature of the Spline curve.
             * **radius** (:class:`numpy.ndarray`) -- Radius of curvature of the Spline curve.


.. py:function:: make_spline(x, y, n_pts, k = 3, s = None)

   Create a parametric spline from a set of points.

   :Parameters: * **x** (:class:`numpy.ndarray`) -- x-coordinates of the points.
                * **y** (:class:`numpy.ndarray`) -- y-coordinates of the points.
                * **n_pts** (:class:`int`) -- Number of points in the output spline curve.
                * **k** (:class:`int`, *optional*) -- Degree of the smoothing spline. Must be
                  1 <= ``k`` <= 5. Default to 3 which is a cubic spline.
                * **s** (:class:`float` or :obj:`None`, *optional*) -- Smoothing factor is used for determining the number of knots.
                  This arg controls the tradeoff between closeness and smoothness of fit.
                  Larger ``s`` means more smoothing while smaller values of ``s`` indicates
                  less smoothing. If None (default), smoothing is done with all data points.

   :returns: :class:`Spline` -- A Spline object with ``x``, ``y``, ``phi``, ``radius``, ``distance``,
             and ``line`` attributes. The ``line`` attribute returns the Spline
             as a ``shapely.LineString``.


.. py:function:: smooth_linestring(line, smoothing = None, npts = None)

   Smooth a LineString using ``UnivariateSpline`` from ``scipy``.

   :Parameters: * **line** (:class:`shapely.LineString`) -- Centerline to be smoothed.
                * **smoothing** (:class:`float` or :obj:`None`, *optional*) -- Smoothing factor is used for determining the number of knots.
                  This arg controls the tradeoff between closeness and smoothness of fit.
                  Larger ``smoothing`` means more smoothing while smaller values of
                  ``smoothing`` indicates less smoothing. If None (default), smoothing
                  is done with all points.
                * **npts** (:class:`int`, *optional*) -- Number of points in the output smoothed line. Defaults to 5 times
                  the number of points in the input line.

   :returns: :class:`shapely.LineString` -- Smoothed line with uniform spacing.

   .. rubric:: Examples

   >>> import geopandas as gpd
   >>> import shapely
   >>> line = shapely.LineString(
   ...     [
   ...         (-97.06138, 32.837),
   ...         (-97.06133, 32.836),
   ...         (-97.06124, 32.834),
   ...         (-97.06127, 32.832),
   ...     ]
   ... )
   >>> line_smooth = smooth_linestring(line, 4326, 5)
   >>> list(zip(*line_smooth.xy))
   [(-97.06138, 32.837),
   (-97.06132, 32.83575),
   (-97.06126, 32.83450),
   (-97.06123, 32.83325),
   (-97.06127, 32.83200)]


.. py:function:: smooth_multilinestring(mline, npts_list = None, sigma = None)

   Smooth a MultiLineString using a cubic spline.

   :Parameters: * **mline** (:class:`shapely.MultiLineString`) -- MultiLineString to smooth.
                * **npts_list** (:class:`list` of :class:`int`, *optional*) -- Number of points for uniform spacing of the generated spline, defaults
                  to ``None``, i.e., the number of points along each line in the MultiLineString.
                * **sigma** (:class:`float`, *optional*) -- Standard deviation for Gaussian kernel used for filtering noise in the line
                  before fitting the spline. Defaults to ``None``, i.e., no filtering.

   :returns: :class:`shapely.MultiLineString` -- The fitted cubic spline.


.. py:function:: spline_curvature(spline_x, spline_y, konts)

   Compute the curvature of a Spline curve.

   .. rubric:: Notes

   The formula for the curvature of a Spline curve is:

   .. math::

       \kappa = \frac{\dot{x}\ddot{y} - \ddot{x}\dot{y}}{(\dot{x}^2 + \dot{y}^2)^{3/2}}

   where :math:`\dot{x}` and :math:`\dot{y}` are the first derivatives of the
   Spline curve and :math:`\ddot{x}` and :math:`\ddot{y}` are the second
   derivatives of the Spline curve. Also, the radius of curvature is:

   .. math::

       \rho = \frac{1}{|\kappa|}

   :Parameters: * **spline_x** (:class:`scipy.interpolate.UnivariateSpline`) -- Spline curve for the x-coordinates of the points.
                * **spline_y** (:class:`scipy.interpolate.UnivariateSpline`) -- Spline curve for the y-coordinates of the points.
                * **konts** (:class:`numpy.ndarray`) -- Knots along the Spline curve to compute the curvature at. The knots
                  must be strictly increasing.

   :returns: * **phi** (:class:`numpy.ndarray`) -- Angle of the tangent of the Spline curve.
             * **curvature** (:class:`numpy.ndarray`) -- Curvature of the Spline curve.
             * **radius** (:class:`numpy.ndarray`) -- Radius of curvature of the Spline curve.


.. py:function:: spline_linestring(line, n_pts, degree = 3, smoothing = None)

   Generate a parametric spline from a LineString.

   :Parameters: * **line** (:class:`shapely.LineString`, :class:`shapely.MultiLineString`) -- Line to smooth. Note that if ``line`` is ``MultiLineString``
                  it will be merged into a single ``LineString``. If the merge
                  fails, an exception will be raised.
                * **n_pts** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the smoothing spline. Must be
                  1 <= ``degree`` <= 5. Default to 3 which is a cubic spline.
                * **smoothing** (:class:`float` or :obj:`None`, *optional*) -- Smoothing factor is used for determining the number of knots.
                  This arg controls the tradeoff between closeness and smoothness of fit.
                  Larger ``smoothing`` means more smoothing while smaller values of
                  ``smoothing`` indicates less smoothing. If None (default), smoothing
                  is done with all points.

   :returns: :class:`Spline` -- A :class:`Spline` object with ``x``, ``y``, ``phi``, ``radius``,
             ``distance``, and ``line`` attributes. The ``line`` attribute
             returns the Spline as a shapely.LineString.

   .. rubric:: Examples

   >>> import geopandas as gpd
   >>> import shapely
   >>> line = shapely.LineString(
   ...     [
   ...         (-97.06138, 32.837),
   ...         (-97.06133, 32.836),
   ...         (-97.06124, 32.834),
   ...         (-97.06127, 32.832),
   ...     ]
   ... )
   >>> sp = spline_linestring(line, 4326, 5)
   >>> list(zip(*sp.line.xy))
   [(-97.06138, 32.837),
   (-97.06132, 32.83575),
   (-97.06126, 32.83450),
   (-97.06123, 32.83325),
   (-97.06127, 32.83200)]


