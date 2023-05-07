:py:mod:`pynldas2.pynldas2`
===========================

.. py:module:: pynldas2.pynldas2

.. autoapi-nested-parse::

   Get hourly NLDAS2 forcing data.



Module Contents
---------------

.. py:function:: get_bycoords(coords, start_date, end_date, coords_id = None, crs = 4326, variables = None, to_xarray = False, n_conn = 4, snow = False, snow_params = None, source = 'grib')

   Get NLDAS climate forcing data for a list of coordinates.

   :Parameters: * **coords** (:class:`list` of :class:`tuples`) -- List of (lon, lat) coordinates.
                * **start_date** (:class:`str`) -- Start date of the data.
                * **end_date** (:class:`str`) -- End date of the data.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input coordinates, defaults to ``EPSG:4326``.
                * **variables** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Variables to download. If None, all variables are downloaded.
                  Valid variables are: ``prcp``, ``pet``, ``temp``, ``wind_u``, ``wind_v``,
                  ``rlds``, ``rsds``, and ``humidity`` (and ``psurf`` if ``source=netcdf``)
                * **to_xarray** (:class:`bool`, *optional*) -- If True, the data is returned as an xarray dataset.
                * **n_conn** (:class:`int`, *optional*) -- Number of parallel connections to use for retrieving data, defaults to 4.
                  The maximum number of connections is 4, if more than 4 are requested, 4
                  connections will be used.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **source** (:class:`str`, *optional*) -- Source to pull data rods from. Valid sources are: ``grib`` and ``netcdf``

   :returns: :class:`pandas.DataFrame` -- The requested data as a dataframe.


.. py:function:: get_bygeom(geometry, start_date, end_date, geo_crs, variables = None, n_conn = 4, snow = False, snow_params = None, source = 'grib')

   Get hourly NLDAS climate forcing within a geometry at 0.125 resolution.

   :Parameters: * **geometry** (:class:`shapely.Polygon`, :class:`shapely.MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Input polygon or a bounding box like so (xmin, ymin, xmax, ymax).
                * **start_date** (:class:`str`) -- Start date of the data.
                * **end_date** (:class:`str`) -- End date of the data.
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- CRS of the input geometry
                * **variables** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Variables to download. If None, all variables are downloaded.
                  Valid variables are: ``prcp``, ``pet``, ``temp``, ``wind_u``, ``wind_v``,
                  ``rlds``, ``rsds``, and ``humidity`` (and ``psurf`` if ``source=netcdf``)
                * **n_conn** (:class:`int`, *optional*) -- Number of parallel connections to use for retrieving data, defaults to 4.
                  It should be less than 4.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **source** (:class:`str`, *optional*) -- Source to pull data rods from. Valid sources are: ``grib`` and ``netcdf``.

   :returns: :class:`xarray.Dataset` -- The requested forcing data.


.. py:function:: get_grid_mask()

   Get the NLDAS2 grid that contains the land/water/soil/vegetation mask.

   :returns: :class:`xarray.Dataset` -- The grid mask.


