:py:mod:`pydaymet.pydaymet`
===========================

.. py:module:: pydaymet.pydaymet

.. autoapi-nested-parse::

   Access the Daymet database for both single single pixel and gridded queries.



Module Contents
---------------

.. py:function:: get_bycoords(coords, dates, coords_id = None, crs = 4326, variables = None, region = 'na', time_scale = 'daily', pet = None, pet_params = None, snow = False, snow_params = None, ssl = True, to_xarray = False)

   Get point-data from the Daymet database at 1-km resolution.

   This function uses THREDDS data service to get the coordinates
   and supports getting monthly and annual summaries of the climate
   data directly from the server.

   :Parameters: * **coords** (:class:`tuple` or :class:`list` of :class:`tuples`) -- Coordinates of the location(s) of interest as a tuple (x, y)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years ``[2001, 2010, ...]``.
                * **coords_id** (:class:`list` of :class:`int` or :class:`str`, *optional*) -- A list of identifiers for the coordinates. This option only applies when ``to_xarray``
                  is set to ``True``. If not provided, the coordinates will be enumerated.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input coordinates, defaults to ``EPSG:4326``.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                * **region** (:class:`str`, *optional*) -- Target region in the US, defaults to ``na``. Acceptable values are:

                  * ``na``: Continental North America
                  * ``hi``: Hawaii
                  * ``pr``: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be ``daily``, ``monthly`` (monthly summaries),
                  or ``annual`` (annual summaries). Defaults to ``daily``.
                * **pet** (:class:`str`, *optional*) -- Method for computing PET. Supported methods are
                  ``penman_monteith``, ``priestley_taylor``, ``hargreaves_samani``, and
                  None (don't compute PET). The ``penman_monteith`` method is based on
                  :footcite:t:`Allen_1998` assuming that soil heat flux density is zero.
                  The ``priestley_taylor`` method is based on
                  :footcite:t:`Priestley_1972` assuming that soil heat flux density is zero.
                  The ``hargreaves_samani`` method is based on :footcite:t:`Hargreaves_1982`.
                  Defaults to ``None``.
                * **pet_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary, defaults to ``None``. An important
                  parameter for ``priestley_taylor`` and ``penman_monteith`` methods is
                  ``arid_correction`` which is used to correct the actual vapor pressure
                  for arid regions. Since relative humidity is not provided by Daymet, the actual
                  vapor pressure is computed assuming that the dewpoint temperature is equal to
                  the minimum temperature. However, for arid regions, FAO 56 suggests to subtract
                  minimum temperature by 2-3 °C to account for the fact that in arid regions,
                  the air might not be saturated when its temperature is at its minimum. For such
                  areas, you can pass ``{"arid_correction": True, ...}`` to subtract 2°C from the
                  minimum temperature for computing the actual vapor pressure.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **ssl** (:class:`bool`, *optional*) -- Whether to verify SSL certification, defaults to ``True``.
                * **to_xarray** (:class:`bool`, *optional*) -- Return the data as an ``xarray.Dataset``. Defaults to ``False``.

   :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- Daily climate data for a single or list of locations.

   .. rubric:: Examples

   >>> import pydaymet as daymet
   >>> coords = (-1431147.7928, 318483.4618)
   >>> dates = ("2000-01-01", "2000-12-31")
   >>> clm = daymet.get_bycoords(
   ...     coords,
   ...     dates,
   ...     crs="epsg:3542",
   ...     pet="hargreaves_samani",
   ... )
   >>> clm["pet (mm/day)"].mean()
   3.713

   .. rubric:: References

   .. footbibliography::


.. py:function:: get_bygeom(geometry, dates, crs = 4326, variables = None, region = 'na', time_scale = 'daily', pet = None, pet_params = None, snow = False, snow_params = None, ssl = True)

   Get gridded data from the Daymet database at 1-km resolution.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`bbox`) -- The geometry of the region of interest.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:

                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly average),
                  or annual (annual average). Defaults to daily.
                * **pet** (:class:`str`, *optional*) -- Method for computing PET. Supported methods are
                  ``penman_monteith``, ``priestley_taylor``, ``hargreaves_samani``, and
                  None (don't compute PET). The ``penman_monteith`` method is based on
                  :footcite:t:`Allen_1998` assuming that soil heat flux density is zero.
                  The ``priestley_taylor`` method is based on
                  :footcite:t:`Priestley_1972` assuming that soil heat flux density is zero.
                  The ``hargreaves_samani`` method is based on :footcite:t:`Hargreaves_1982`.
                  Defaults to ``None``.
                * **pet_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary, defaults to ``None``. Valid
                  parameters are:

                  * ``penman_monteith``: ``soil_heat_flux``, ``albedo``, ``alpha``,
                    and ``arid_correction``.
                  * ``priestley_taylor``: ``soil_heat_flux``, ``albedo``, and ``arid_correction``.
                  * ``hargreaves_samani``: None.

                  Default values for the parameters are: ``soil_heat_flux`` = 0, ``albedo`` = 0.23,
                  ``alpha`` = 1.26, and ``arid_correction`` = False.
                  An important parameter for ``priestley_taylor`` and ``penman_monteith`` methods
                  is ``arid_correction`` which is used to correct the actual vapor pressure
                  for arid regions. Since relative humidity is not provided by Daymet, the actual
                  vapor pressure is computed assuming that the dewpoint temperature is equal to
                  the minimum temperature. However, for arid regions, FAO 56 suggests to subtract
                  minimum temperature by 2-3 °C to account for the fact that in arid regions,
                  the air might not be saturated when its temperature is at its minimum. For such
                  areas, you can pass ``{"arid_correction": True, ...}`` to subtract 2 °C from the
                  minimum temperature for computing the actual vapor pressure.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **ssl** (:class:`bool`, *optional*) -- Whether to verify SSL certification, defaults to ``True``.

   :returns: :class:`xarray.Dataset` -- Daily climate data within the target geometry.

   .. rubric:: Examples

   >>> from shapely import Polygon
   >>> import pydaymet as daymet
   >>> geometry = Polygon(
   ...     [[-69.77, 45.07], [-69.31, 45.07], [-69.31, 45.45], [-69.77, 45.45], [-69.77, 45.07]]
   ... )
   >>> clm = daymet.get_bygeom(geometry, 2010, variables="tmin", time_scale="annual")
   >>> clm["tmin"].mean().compute().item()
   1.361

   .. rubric:: References

   .. footbibliography::


