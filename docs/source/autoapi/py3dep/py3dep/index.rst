:py:mod:`py3dep.py3dep`
=======================

.. py:module:: py3dep.py3dep

.. autoapi-nested-parse::

   Get data from 3DEP database.



Module Contents
---------------

.. py:function:: check_3dep_availability(bbox, crs = DEF_CRS)

   Query 3DEP's resolution availability within a bounding box.

   This function checks availability of 3DEP's at the following resolutions:
   1 m, 3 m, 5 m, 10 m, 30 m, 60 m, and topobathy (integrated topobathymetry).

   :Parameters: * **bbox** (:class:`tuple`) -- Bounding box as tuple of ``(min_x, min_y, max_x, max_y)``.
                * **crs** (:class:`str` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of bbox, defaults to ``EPSG:4326``.

   :returns: :class:`dict` -- True if bbox intersects 3DEP elevation for each available resolution.
             Keys are the supported resolutions and values are their availability.

   .. rubric:: Examples

   >>> import py3dep
   >>> bbox = (-69.77, 45.07, -69.31, 45.45)
   >>> py3dep.check_3dep_availability(bbox)
   {'1m': True, '3m': False, '5m': False, '10m': True, '30m': True, '60m': False, 'topobathy': False}


.. py:function:: elevation_bycoords(coords, crs = DEF_CRS, source = 'tep')

   Get elevation for a list of coordinates.

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- Coordinates of target location as list of tuples ``[(x, y), ...]``.
                * **crs** (:class:`str` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of coords, defaults to ``EPSG:4326``.
                * **source** (:class:`str`, *optional*) -- Data source to be used, default to ``airmap``. Supported sources are
                  ``airmap`` (30 m resolution), ``tnm`` (using The National Map's Bulk Point
                  Query Service with 10 m resolution) and ``tep`` (using 3DEP's WMS service
                  at 10 m resolution). The ``tnm`` and ``tep`` sources are more accurate since they
                  use the 1/3 arc-second DEM layer from 3DEP service but it is limited to the US.
                  They both tend to be slower than the Airmap service. Note that ``tnm`` is bit unstable.
                  It's recommended to use ``tep`` unless 10-m resolution accuracy is not necessary which
                  in that case ``airmap`` is more appropriate.

   :returns: :class:`list` of :class:`float` -- Elevation in meter.


.. py:function:: elevation_bygrid(xcoords, ycoords, crs, resolution, depression_filling = False)

   Get elevation from DEM data for a grid.

   This function is intended for getting elevations for a gridded dataset.

   :Parameters: * **xcoords** (:class:`list`) -- List of x-coordinates of a grid.
                * **ycoords** (:class:`list`) -- List of y-coordinates of a grid.
                * **crs** (:class:`str` or :class:`pyproj.CRS`) -- The spatial reference system of the input grid, defaults to ``EPSG:4326``.
                * **resolution** (:class:`float`) -- The accuracy of the output, defaults to 10 m which is the highest
                  available resolution that covers CONUS. Note that higher resolution
                  increases computation time so chose this value with caution.
                * **depression_filling** (:class:`bool`, *optional*) -- Fill depressions before sampling using
                  `RichDEM <https://richdem.readthedocs.io/en/latest/>`__ package, defaults to False.

   :returns: :class:`xarray.DataArray` -- Elevations of the input coordinates as a ``xarray.DataArray``.


.. py:function:: elevation_profile(lines, spacing, dem_res = 10, crs = DEF_CRS)

   Get the elevation profile along a line at a given uniform spacing.

   This function converts the line to a B-spline and then calculates the elevation
   along the spline at a given uniform spacing.

   :Parameters: * **lines** (:class:`LineString` or :class:`MultiLineString`) -- Line segment(s) to be profiled. If its type is ``MultiLineString``,
                  it will be converted to a single ``LineString`` and if this operation
                  fails, a ``InputTypeError`` will be raised.
                * **spacing** (:class:`float`) -- Spacing between the sample points along the line in meters.
                * **dem_res** (:class:`float`, *optional*) -- Resolution of the DEM source to use in meter, defaults to 10.
                * **crs** (:class:`str` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of ``lines``, defaults to ``EPSG:4326``.

   :returns: :class:`xarray.DataArray` -- Elevation profile with dimension ``z`` and three coordinates: ``x``, ``y``,
             and ``distance``. The ``distance`` coordinate is the distance from the start
             of the line in meters.


.. py:function:: get_map(layers, geometry, resolution, geo_crs = DEF_CRS, crs = DEF_CRS)

   Access to `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`__ service.

   The 3DEP service has multi-resolution sources, so depending on the user
   provided resolution the data is resampled on server-side based
   on all the available data sources. The following layers are available:

   - ``DEM``
   - ``Hillshade Gray``
   - ``Aspect Degrees``
   - ``Aspect Map``
   - ``GreyHillshade_elevationFill``
   - ``Hillshade Multidirectional``
   - ``Slope Map``
   - ``Slope Degrees``
   - ``Hillshade Elevation Tinted``
   - ``Height Ellipsoidal``
   - ``Contour 25``
   - ``Contour Smoothed 25``

   :Parameters: * **layers** (:class:`str` or :class:`list` of :class:`str`) -- A valid 3DEP layer or a list of them.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- A shapely Polygon or a bounding box of the form ``(west, south, east, north)``.
                * **resolution** (:class:`float`) -- The target resolution in meters. The width and height of the output are computed in
                  pixels based on the geometry bounds and the given resolution.
                * **geo_crs** (:class:`str`, *optional*) -- The spatial reference system of the input geometry, defaults to ``EPSG:4326``.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``EPSG:4326``. Valid values are ``EPSG:4326``, ``EPSG:3576``, ``EPSG:3571``,
                  ``EPSG:3575``, ``EPSG:3857``, ``EPSG:3572``, ``CRS:84``, ``EPSG:3573``,
                  and ``EPSG:3574``.

   :returns: :class:`xarray.DataArray` or :class:`xarray.Dataset` -- The requested topographic data as an ``xarray.DataArray`` or ``xarray.Dataset``.


.. py:function:: query_3dep_sources(bbox, crs = DEF_CRS, res = None)

   Query 3DEP's data sources within a bounding box.

   This function queries the availability of the underlying data that 3DEP uses
   at the following resolutions:
   1 m, 3 m, 5 m, 10 m, 30 m, 60 m, and topobathy (integrated topobathymetry).

   :Parameters: * **bbox** (:class:`tuple`) -- Bounding box as tuple of ``(min_x, min_y, max_x, max_y)``.
                * **crs** (:class:`str` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of bbox, defaults to ``EPSG:4326``.
                * **res** (:class:`str`, *optional*) -- Resolution to query, defaults to ``None``, i.e., all resolutions.

   :returns: :class:`geopandas.GeoDataFrame` -- Polygon(s) representing the 3DEP data sources at each resolution.
             Resolutions are given in the ``dem_res`` column.

   .. rubric:: Examples

   >>> import py3dep
   >>> bbox = (-69.77, 45.07, -69.31, 45.45)
   >>> src = py3dep.query_3dep_sources(bbox)
   >>> src.groupby("dem_res")["OBJECTID"].count().to_dict()
   {'10m': 8, '1m': 4, '30m': 8}
   >>> src = py3dep.query_3dep_sources(bbox, res="1m")
   >>> src.groupby("dem_res")["OBJECTID"].count().to_dict()
   {'1m': 4}


