:py:mod:`py3dep.py3dep`
=======================

.. py:module:: py3dep.py3dep

.. autoapi-nested-parse::

   Get data from 3DEP database.



Module Contents
---------------

.. py:function:: add_elevation(ds, resolution = None, x_dim = 'x', y_dim = 'y', mask = None)

   Add elevation data to a dataset as a new variable.

   :Parameters: * **ds** (:class:`xarray.DataArray` or :class:`xarray.Dataset`) -- The dataset to add elevation data to. It must contain
                  CRS information.
                * **resolution** (:class:`float`, *optional*) -- Target DEM source resolution in meters, defaults ``None``, i.e.,
                  the resolution of the input ``ds`` will be used.
                * **x_dim** (:class:`str`, *optional*) -- Name of the x-coordinate dimension in ``ds``, defaults to ``x``.
                * **y_dim** (:class:`str`, *optional*) -- Name of the y-coordinate dimension in ``ds``, defaults to ``y``.
                * **mask** (:class:`xarray.DataArray`, *optional*) -- A mask to apply to the elevation data, defaults to ``None``.

   :returns: :class:`xarray.Dataset` -- The dataset with ``elevation`` variable added.


.. py:function:: check_3dep_availability(bbox, crs = 4326)

   Query 3DEP's resolution availability within a bounding box.

   This function checks availability of 3DEP's at the following resolutions:
   1 m, 3 m, 5 m, 10 m, 30 m, 60 m, and topobathy (integrated topobathymetry).

   :Parameters: * **bbox** (:class:`tuple`) -- Bounding box as tuple of ``(min_x, min_y, max_x, max_y)``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of ``bbox``, defaults to ``EPSG:4326``.

   :returns: :class:`dict` -- ``True`` if bbox intersects 3DEP elevation for each available resolution.
             Keys are the supported resolutions and values are their availability.
             If the query fails due to any reason, the value will be ``Failed``.
             If necessary, you can try again later until there is no ``Failed`` value.

   .. rubric:: Examples

   >>> import py3dep
   >>> bbox = (-69.77, 45.07, -69.31, 45.45)
   >>> py3dep.check_3dep_availability(bbox)
   {'1m': True, '3m': False, '5m': False, '10m': True, '30m': True, '60m': False, 'topobathy': False}


.. py:function:: elevation_bycoords(coords: tuple[float, float], crs: CRSTYPE = ..., source: Literal[tep, tnm] = ...) -> float
                 elevation_bycoords(coords: list[tuple[float, float]], crs: CRSTYPE = ..., source: Literal[tep, tnm] = ...) -> list[float]

   Get elevation for a list of coordinates.

   :Parameters: * **coords** (:class:`tuple` or :class:`list` of :class:`tuple`) -- Coordinates of target location(s), e.g., ``[(x, y), ...]``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of coords, defaults to ``EPSG:4326``.
                * **source** (:class:`str`, *optional*) -- Data source to be used, default to ``tep``. Supported sources are
                  ``tnm`` (using The National Map's Bulk Point
                  Query Service with 10 m resolution) and ``tep`` (using 3DEP's static DEM VRTs
                  at 10 m resolution). The ``tnm`` and ``tep`` sources are more accurate since they
                  use the 1/3 arc-second DEM layer from 3DEP service but it is limited to the US.
                  Note that ``tnm`` is bit unstable. It's recommended to use ``tep`` unless 10-m
                  resolution accuracy is not necessary.

   :returns: :class:`float` or :class:`list` of :class:`float` -- Elevation in meter.


.. py:function:: elevation_bygrid(xcoords, ycoords, crs, resolution, depression_filling = False)

   Get elevation from DEM data for a grid.

   This function is intended for getting elevations for a gridded dataset.

   :Parameters: * **xcoords** (:class:`list`) -- List of x-coordinates of a grid.
                * **ycoords** (:class:`list`) -- List of y-coordinates of a grid.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS` or :class:`pyproj.CRS`) -- The spatial reference system of the input grid,
                  defaults to ``EPSG:4326``.
                * **resolution** (:class:`int`) -- The accuracy of the output, defaults to 10 m which is the highest
                  available resolution that covers CONUS. Note that higher resolution
                  increases computation time so chose this value with caution.
                * **depression_filling** (:class:`bool`, *optional*) -- Fill depressions before sampling using
                  `pyflwdir <https://deltares.github.io/pyflwdir>`__ package,
                  defaults to ``False``.

   :returns: :class:`xarray.DataArray` -- Elevations of the input coordinates as a ``xarray.DataArray``.


.. py:function:: elevation_profile(lines, spacing, crs = 4326)

   Get the elevation profile along a line at a given uniform spacing.

   .. note::

       This function converts the line to a spline and then calculates the elevation
       along the spline at a given uniform spacing using 10-m resolution DEM from 3DEP.

   :Parameters: * **lines** (:class:`LineString` or :class:`MultiLineString`) -- Line segment(s) to be profiled. If its type is ``MultiLineString``,
                  it will be converted to a single ``LineString`` and if this operation
                  fails, an ``InputTypeError`` will be raised.
                * **spacing** (:class:`float`) -- Spacing between the sample points along the line in meters.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- Spatial reference System (CRS) of ``lines``, defaults to ``EPSG:4326``.

   :returns: :class:`xarray.DataArray` -- Elevation profile with dimension ``z`` and three coordinates: ``x``, ``y``,
             and ``distance``. The ``distance`` coordinate is the distance from the start
             of the line in meters.


.. py:function:: get_dem(geometry, resolution, crs = 4326)

   Get DEM data at any resolution from 3DEP.

   .. rubric:: Notes

   This function is a wrapper of ``static_3dep_dem`` and ``get_map`` functions.
   Since ``static_3dep_dem`` is much faster, if the requested resolution is 10 m,
   30 m, or 60 m, ``static_3dep_dem`` will be used. Otherwise, ``get_map``
   will be used.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry to get DEM within. It can be a polygon or a boundong box
                  of form (xmin, ymin, xmax, ymax).
                * **resolution** (:class:`int`) -- Target DEM source resolution in meters.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system of the input geometry, defaults to ``EPSG:4326``.

   :returns: :class:`xarray.DataArray` -- DEM at the specified resolution in meters and 4326 CRS.


.. py:function:: get_dem_vrt(bbox, resolution, vrt_path, tiff_dir = 'cache', crs = 4326)

   Get DEM data at any resolution from 3DEP and save it as a VRT file.

   :Parameters: * **bbox** (:class:`tuple` of :class:`length 4`) -- The boundong box of form (xmin, ymin, xmax, ymax).
                * **resolution** (:class:`int`) -- Target DEM source resolution in meters.
                * **vrt_path** (:class:`str` or :class:`pathlib.Path`) -- Path to the output VRT file.
                * **tiff_dir** (:class:`str` or :class:`pathlib.Path`, *optional*) -- Path to the directory to save the downloaded TIFF file, defaults
                  to ``./cache``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system of ``bbox``, defaults to ``EPSG:4326``.


.. py:function:: get_map(layers: str, geometry: shapely.Polygon | shapely.MultiPolygon | tuple[float, float, float, float], resolution: int, geo_crs: CRSTYPE = ..., crs: CRSTYPE = ...) -> xarray.DataArray
                 get_map(layers: list[str], geometry: shapely.Polygon | shapely.MultiPolygon | tuple[float, float, float, float], resolution: int, geo_crs: CRSTYPE = ..., crs: CRSTYPE = ...) -> xarray.Dataset

   Access dynamic layer of `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`__.

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
                * **resolution** (:class:`int`) -- The target resolution in meters. The width and height of the output are computed in
                  pixels based on the geometry bounds and the given resolution.
                * **geo_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system of the input geometry, defaults to ``EPSG:4326``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``EPSG:4326``. Valid values are ``EPSG:4326``, ``EPSG:3576``, ``EPSG:3571``,
                  ``EPSG:3575``, ``EPSG:3857``, ``EPSG:3572``, ``CRS:84``, ``EPSG:3573``,
                  and ``EPSG:3574``.

   :returns: :class:`xarray.DataArray` or :class:`xarray.Dataset` -- The requested topographic data as an ``xarray.DataArray`` or ``xarray.Dataset``.


.. py:function:: query_3dep_sources(bbox, crs = 4326, res = None)

   Query 3DEP's data sources within a bounding box.

   This function queries the availability of the underlying data that 3DEP uses
   at the following resolutions:
   1 m, 3 m, 5 m, 10 m, 30 m, 60 m, and topobathy (integrated topobathymetry).

   :Parameters: * **bbox** (:class:`tuple`) -- Bounding box as tuple of ``(min_x, min_y, max_x, max_y)``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS` or :class:`pyproj.CRS`, *optional*) -- Spatial reference (CRS) of bbox, defaults to ``EPSG:4326``.
                * **res** (:class:`str`, :class:`list` of :class:`str`, *optional*) -- Resolution to query, defaults to ``None``, i.e., all resolutions.
                  Available resolutions are: ``1m``, ``3m``, ``5m``, ``10m``, ``30m``,
                  ``60m``, and ``topobathy``.

   :returns: :class:`geopandas.GeoDataFrame` -- Polygon(s) representing the 3DEP data sources at each resolution.
             Resolutions are given in the ``dem_res`` column.

   .. rubric:: Examples

   >>> import py3dep
   >>> bbox = (-69.77, 45.07, -69.31, 45.45)
   >>> src = py3dep.query_3dep_sources(bbox)
   >>> src.groupby("dem_res")["OBJECTID"].count().to_dict()
   {'10m': 8, '1m': 2, '30m': 8}
   >>> src = py3dep.query_3dep_sources(bbox, res="1m")
   >>> src.groupby("dem_res")["OBJECTID"].count().to_dict()
   {'1m': 2}


.. py:function:: static_3dep_dem(geometry, crs, resolution = 10)

   Get DEM data at specific resolution from 3DEP.

   .. rubric:: Notes

   In contrast to ``get_map`` function, this function only gets DEM data at
   specific resolution, namely 10 m, 30 m, and 60 m. However, this function
   is faster. This function is intended for cases where only need DEM at a
   specific resolution is required and for the other requests ``get_map``
   should be used.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry to get DEM within. It can be a polygon or a boundong box
                  of form (xmin, ymin, xmax, ymax).
                * **crs** (:class:`int`, :class:`str`, :class:`of pyproj.CRS`) -- CRS of the input geometry.
                * **resolution** (:class:`int`, *optional*) -- Target DEM source resolution in meters, defaults to 10 m which is the highest
                  resolution available over the US. Available options are 10, 30, and 60.

   :returns: :class:`xarray.DataArray` -- The request DEM at the specified resolution.


