:py:mod:`pydaymet.pydaymet`
===========================

.. py:module:: pydaymet.pydaymet

.. autoapi-nested-parse::

   Access the Daymet database for both single single pixel and gridded queries.



Module Contents
---------------

.. py:function:: get_bycoords(coords, dates, crs = DEF_CRS, variables = None, pet = False, region = 'na', time_scale = 'daily')

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
                * **pet** (:class:`bool`) -- Whether to compute evapotranspiration based on
                  `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm>`__.
                  The default is False
                * **region** (:class:`str`, *optional*) -- Target region in the US, defaults to ``na``. Acceptable values are:

                  * ``na``: Continental North America
                  * ``hi``: Hawaii
                  * ``pr``: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.

   :returns: :class:`pandas.DataFrame` -- Daily climate data for a location.

   .. rubric:: Examples

   >>> import pydaymet as daymet
   >>> coords = (-1431147.7928, 318483.4618)
   >>> dates = ("2000-01-01", "2000-12-31")
   >>> clm = daymet.get_bycoords(coords, dates, crs="epsg:3542", pet=True)
   >>> clm["pet (mm/day)"].mean()
   3.497


.. py:function:: get_bygeom(geometry, dates, crs = DEF_CRS, variables = None, pet = False, region = 'na', time_scale = 'daily')

   Get gridded data from the Daymet database at 1-km resolution.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`bbox`) -- The geometry of the region of interest.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                * **pet** (:class:`bool`) -- Whether to compute evapotranspiration based on
                  `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm>`__.
                  The default is False
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:

                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly average),
                  or annual (annual average). Defaults to daily.

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


.. py:function:: get_byloc(coords, dates, crs = DEF_CRS, variables = None, pet = False)

   Get daily climate data from Daymet for a single point.

   .. deprecated:: 0.9.0
       Please use ``get_bycoords`` instead. This function will be removed in the future.

   :Parameters: * **coords** (:class:`tuple`) -- Longitude and latitude of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`) -- Either a tuple (start, end) or a list of years [YYYY, ...].
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinates, defaults to epsg:4326
                * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`bool`, *optional*) -- Whether to compute evapotranspiration based on
                  `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm>`__.
                  The default is False

   :returns: :class:`pandas.DataFrame` -- Daily climate data for a location.


