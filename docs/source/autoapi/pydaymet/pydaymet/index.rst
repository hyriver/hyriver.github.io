:py:mod:`pydaymet.pydaymet`
===========================

.. py:module:: pydaymet.pydaymet

.. autoapi-nested-parse::

   Access the Daymet database for both single single pixel and gridded queries.



Module Contents
---------------

.. py:function:: get_bycoords(coords, dates, crs = DEF_CRS, variables = None, region = 'na', time_scale = 'daily', pet = None, pet_params = None)

   Get point-data from the Daymet database at 1-km resolution.

   This function uses THREDDS data service to get the coordinates
   and supports getting monthly and annual summaries of the climate
   data directly from the server.

   :Parameters: * **coords** (:class:`tuple`) -- Coordinates of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years ``[2001, 2010, ...]``.
                * **crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to ``"epsg:4326"``.
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
                * **pet_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the PET function.
                  Defaults to ``None``.

   :returns: :class:`pandas.DataFrame` -- Daily climate data for a location.

   .. rubric:: Examples

   >>> import pydaymet as daymet
   >>> coords = (-1431147.7928, 318483.4618)
   >>> dates = ("2000-01-01", "2000-12-31")
   >>> clm = daymet.get_bycoords(coords, dates, crs="epsg:3542", pet="hargreaves_samani")
   >>> clm["pet (mm/day)"].mean()
   3.713

   .. rubric:: References

   .. footbibliography::


.. py:function:: get_bygeom(geometry, dates, crs = DEF_CRS, variables = None, region = 'na', time_scale = 'daily', pet = None, pet_params = None)

   Get gridded data from the Daymet database at 1-km resolution.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`bbox`) -- The geometry of the region of interest.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
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
                * **pet_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the PET function.
                  Defaults to ``None``.

   :returns: :class:`xarray.Dataset` -- Daily climate data within the target geometry.

   .. rubric:: Examples

   >>> from shapely.geometry import Polygon
   >>> import pydaymet as daymet
   >>> geometry = Polygon(
   ...     [[-69.77, 45.07], [-69.31, 45.07], [-69.31, 45.45], [-69.77, 45.45], [-69.77, 45.07]]
   ... )
   >>> clm = daymet.get_bygeom(geometry, 2010, variables="tmin", time_scale="annual")
   >>> clm["tmin"].mean().compute().item()
   1.361

   .. rubric:: References

   .. footbibliography::


