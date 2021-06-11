:mod:`py3dep.py3dep`
====================

.. py:module:: py3dep.py3dep

.. autoapi-nested-parse::

   Get data from 3DEP database.



Module Contents
---------------

.. function:: deg2mpm(da: xr.DataArray) -> xr.DataArray

   Convert slope from degree to meter/meter.


.. function:: elevation_bycoords(coords: List[Tuple[float, float]], crs: str = DEF_CRS) -> List[int]

   Get elevation from Airmap at 1-arc resolution (~30 m) for a list of coordinates.

   :Parameters: * **coords** (:class:`list` of :class:`tuples`) -- Coordinates of target location as list of tuples ``[(x, y), ...]``.
                * **crs** (:class:`str`, *optional*) -- Spatial reference (CRS) of coords, defaults to ``EPSG:4326``.

   :returns: :class:`list` of :class:`int` -- Elevation in meter.


.. function:: elevation_bygrid(xcoords: List[float], ycoords: List[float], crs: str, resolution: float, dim_names: Optional[Tuple[str, str]] = None, resampling: rio_warp.Resampling = rio_warp.Resampling.bilinear) -> xr.DataArray

   Get elevation from DEM data for a grid.

   This function is intended for getting elevations for a gridded dataset.

   :Parameters: * **xcoords** (:class:`list`) -- List x-coordinates of a a grid.
                * **ycoords** (:class:`list`) -- List of y-coordinates of a grid.
                * **crs** (:class:`str`) -- The spatial reference system of the input grid, defaults to ``EPSG:4326``.
                * **resolution** (:class:`float`) -- The accuracy of the output, defaults to 10 m which is the highest
                  available resolution that covers CONUS. Note that higher resolution
                  increases computation time so chose this value with caution.
                * **dim_names** (:class:`tuple`) -- A tuple of length two containing the coordinate names, defaults to ``("x", "y")``.
                * **resampling** (:class:`rasterio.warp.Resampling`) -- The reasmpling method to use if the input crs is not in the supported
                  3DEP's CRS list which are ``EPSG:4326`` and ``EPSG:3857``.
                  It defaults to bilinear. The available methods can be found
                  `here <https://rasterio.readthedocs.io/en/latest/api/rasterio.enums.html#rasterio.enums.Resampling>`__

   :returns: :class:`xarray.DataArray` -- An data array with name elevation and the given dim names.


.. function:: get_map(layers: Union[str, List[str]], geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], resolution: float, geo_crs: str = DEF_CRS, crs: str = DEF_CRS) -> Union[xr.DataArray, xr.Dataset]

   Access to `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`__ service.

   The 3DEP service has multi-resolution sources so depending on the user
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

   :Parameters: * **layers** (:class:`str` or :class:`list`) -- A valid 3DEP layer or a list of them.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- A shapely Polygon or a bounding box ``(west, south, east, north)``.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in
                  pixels
                  based on the geometry bounds and the given resolution.
                * **geo_crs** (:class:`str`, *optional*) -- The spatial reference system of the input geometry, defaults to
                  ``EPSG:4326``.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``EPSG:4326``.

   :returns: :class:`dict` -- A dict where the keys are the layer name and values are the returned response
             from the WMS service as bytes. You can use ``utils.create_dataset`` function
             to convert the responses to ``xarray.Dataset``.


