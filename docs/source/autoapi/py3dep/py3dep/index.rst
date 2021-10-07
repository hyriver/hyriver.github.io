:py:mod:`py3dep.py3dep`
=======================

.. py:module:: py3dep.py3dep

.. autoapi-nested-parse::

   Get data from 3DEP database.



Module Contents
---------------

.. py:function:: elevation_bycoords(coords, crs = DEF_CRS, source = 'airmap')

   Get elevation for a list of coordinates.

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- Coordinates of target location as list of tuples ``[(x, y), ...]``.
                * **crs** (:class:`str` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of coords, defaults to ``EPSG:4326``.
                * **source** (:class:`str`, *optional*) -- Data source to be used, default to ``airmap``. Supported sources are
                  ``airmap`` (30 m resolution) and ``tnm`` (using The National Map's Bulk Point
                  Query Service with 10 m resolution). The ``tnm`` source is more accurate since it
                  uses the 1/3 arc-second DEM layer from 3DEP service but it is limited to the US.
                  It also tends to be slower than the Airmap service and more unstable.
                  It's recommended to use ``airmap`` unless you need 10-m resolution accuracy.

   :returns: :class:`list` of :class:`float` -- Elevation in meter.


.. py:function:: elevation_bygrid(xcoords, ycoords, crs, resolution, depression_filling = False)

   Get elevation from DEM data for a grid.

   This function is intended for getting elevations for a gridded dataset.

   :Parameters: * **xcoords** (:class:`list`) -- List of x-coordinates of a grid.
                * **ycoords** (:class:`list`) -- List of y-coordinates of a grid.
                * **crs** (:class:`str`) -- The spatial reference system of the input grid, defaults to ``EPSG:4326``.
                * **resolution** (:class:`float`) -- The accuracy of the output, defaults to 10 m which is the highest
                  available resolution that covers CONUS. Note that higher resolution
                  increases computation time so chose this value with caution.
                * **depression_filling** (:class:`bool`, *optional*) -- Fill depressions before sampling using
                  `RichDEM <https://richdem.readthedocs.io/en/latest/>`__ package, defaults to False.

   :returns: :class:`xarray.DataArray` -- Elevations of the input coordinates as a ``xarray.DataArray``.


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


