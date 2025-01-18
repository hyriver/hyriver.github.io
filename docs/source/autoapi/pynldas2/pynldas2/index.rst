pynldas2.pynldas2
=================

.. py:module:: pynldas2.pynldas2

.. autoapi-nested-parse::

   Get hourly NLDAS2 forcing data.





Module Contents
---------------

.. py:function:: get_bycoords(coords, start_date, end_date, coords_id = None, crs = 4326, variables = None, to_xarray = False, snow = False, snow_params = None)

   Get NLDAS-2 climate forcing data for a list of coordinates.

   :Parameters: * **coords** (:class:`list` of :class:`tuples`) -- List of (lon, lat) coordinates.
                * **start_date** (:class:`str`) -- Start date of the data.
                * **end_date** (:class:`str`) -- End date of the data.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input coordinates, defaults to ``EPSG:4326``.
                * **variables** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Variables to download. If None, all variables are downloaded.
                  Valid variables are: ``prcp``, ``pet``, ``temp``, ``wind_u``, ``wind_v``,
                  ``rlds``, ``rsds``, and ``humidity`` and ``psurf``.
                * **to_xarray** (:class:`bool`, *optional*) -- If True, the data is returned as an xarray dataset.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.

   :returns: :class:`pandas.DataFrame` -- The requested data as a dataframe.


.. py:function:: get_bygeom(geometry, start_date, end_date, geo_crs = 4326, variables = None, snow = False, snow_params = None)

   Get hourly NLDAS-2 climate forcing within a geometry at 0.125 resolution.

   :Parameters: * **geometry** (:class:`Polygon` or :class:`tuple`) -- The geometry of the region of interest. It can be a shapely Polygon or a tuple
                  of length 4 representing the bounding box (minx, miny, maxx, maxy).
                * **start_date** (:class:`str`) -- Start date of the data.
                * **end_date** (:class:`str`) -- End date of the data.
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- CRS of the input geometry
                * **variables** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Variables to download. If None, all variables are downloaded.
                  Valid variables are: ``prcp``, ``pet``, ``temp``, ``wind_u``, ``wind_v``,
                  ``rlds``, ``rsds``, and ``humidity`` and ``psurf``.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.

   :returns: :class:`xarray.Dataset` -- The requested forcing data.


