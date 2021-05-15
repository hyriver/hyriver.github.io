:mod:`pydaymet.pydaymet`
========================

.. py:module:: pydaymet.pydaymet

.. autoapi-nested-parse::

   Access the Daymet database for both single single pixel and gridded queries.



Module Contents
---------------

.. py:class:: Daymet(variables: Optional[Union[List[str], str]] = None, pet: bool = False, time_scale: str = 'daily')

   Base class for Daymet requests.

   :Parameters: * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`bool`, *optional*) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
                  The default is False
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.

   .. method:: check_dates(dates: Union[Tuple[str, str], Union[int, List[int]]]) -> None
      :staticmethod:

      Check if input dates are in correct format and valid.


   .. method:: dates_todict(dates: Tuple[str, str]) -> Dict[str, str]
      :staticmethod:

      Set dates by start and end dates as a tuple, (start, end).


   .. method:: dates_tolist(self, dates: Tuple[str, str]) -> List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **dates** (:class:`tuple`) -- Target start and end dates.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.


   .. method:: pet_bygrid(clm_ds: xr.Dataset) -> xr.Dataset
      :staticmethod:

      Compute Potential EvapoTranspiration using Daymet dataset.

      The method is based on `FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
      The following variables are required:
      tmin (deg c), tmax (deg c), lat, lon, vp (Pa), srad (W/m2), dayl (s/day)
      The computed PET's unit is mm/day.

      :Parameters: **clm_ds** (:class:`xarray.DataArray`) -- The dataset should include the following variables:
                   ``tmin``, ``tmax``, ``lat``, ``lon``, ``vp``, ``srad``, ``dayl``

      :returns: :class:`xarray.DataArray` -- The input dataset with an additional variable called ``pet``.


   .. method:: pet_byloc(clm_df: pd.DataFrame, coords: Tuple[float, float], crs: str = DEF_CRS, alt_unit: bool = False) -> pd.DataFrame
      :staticmethod:

      Compute Potential EvapoTranspiration using Daymet dataset for a single location.

      The method is based on `FAO-56 <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
      The following variables are required:
      tmin (deg c), tmax (deg c), lat, lon, vp (Pa), srad (W/m2), dayl (s/day)
      The computed PET's unit is mm/day.

      :Parameters: * **clm_df** (:class:`~pandas.DataFrame`) -- A dataframe with columns named as follows:
                     ``tmin (deg c)``, ``tmax (deg c)``, ``vp (Pa)``, ``srad (W/m^2)``, ``dayl (s)``
                   * **coords** (:class:`tuple` of :class:`floats`) -- Coordinates of the daymet data location as a tuple, (x, y).
                   * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to epsg:4326
                   * **alt_unit** (:class:`str`, *optional*) -- Whether to use alternative units rather than the official ones, defaults to False.

      :returns: :class:`pandas.DataFrame` -- The input DataFrame with an additional column named ``pet (mm/day)``


   .. method:: years_todict(years: Union[List[int], int]) -> Dict[str, str]
      :staticmethod:

      Set date by list of year(s).


   .. method:: years_tolist(self, years: Union[List[int], int]) -> List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **years** (:class:`list`) -- A list of target years.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.



.. function:: coord_urls(code: int, coord: Tuple[float, float], region: str, variables: List[str], dates: List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]) -> Iterator[List[Tuple[str, Dict[str, str]]]]

   Generate an iterable URL list for downloading Daymet data.

   :Parameters: * **code** (:class:`int`) -- Endpoint code which should be one of the following:
                  * 1840: Daily
                  * 1855: Monthly average
                  * 1852: Annual average
                * **coord** (:class:`tuple` of :class:`length 2`) -- Coordinates in EPSG:4326 CRS (lon, lat)
                * **region** (:class:`str`) -- Region in the US. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **variables** (:class:`list`) -- A list of Daymet variables
                * **dates** (:class:`list`) -- A list of dates

   :returns: :class:`generator` -- An iterator of generated URLs.


.. function:: get_bycoords(coords: Tuple[float, float], dates: Union[Tuple[str, str], Union[int, List[int]]], loc_crs: str = DEF_CRS, variables: Optional[List[str]] = None, pet: bool = False, region: str = 'na', time_scale: str = 'daily') -> xr.Dataset

   Get point-data from the Daymet database at 1-km resolution.

   This function uses THREDDS data service to get the coordinates
   and supports getting monthly and annual summaries of the climate
   data directly from the server.

   :Parameters: * **coords** (:class:`tuple`) -- Coordinates of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **loc_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                * **pet** (:class:`bool`) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
                  The default is False
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.

   :returns: :class:`xarray.Dataset` -- Daily climate data within a geometry


.. function:: get_bygeom(geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], dates: Union[Tuple[str, str], Union[int, List[int]]], geo_crs: str = DEF_CRS, variables: Optional[List[str]] = None, pet: bool = False, region: str = 'na', time_scale: str = 'daily') -> xr.Dataset

   Get gridded data from the Daymet database at 1-km resolution.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`bbox`) -- The geometry of the region of interest.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                * **pet** (:class:`bool`) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
                  The default is False
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly average),
                  or annual (annual average). Defaults to daily.

   :returns: :class:`xarray.Dataset` -- Daily climate data within a geometry


.. function:: get_byloc(coords: Tuple[float, float], dates: Union[Tuple[str, str], Union[int, List[int]]], crs: str = DEF_CRS, variables: Optional[Union[List[str], str]] = None, pet: bool = False) -> pd.DataFrame

   Get daily climate data from Daymet for a single point.

   This function uses Daymet's RESTful service to get the daily
   climate data and does not support monthly and annual summaries.
   If you want to get the summaries directly use get_bycoords function.

   :Parameters: * **coords** (:class:`tuple`) -- Longitude and latitude of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`) -- Either a tuple (start, end) or a list of years [YYYY, ...].
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinates, defaults to epsg:4326
                * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`bool`, *optional*) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`__.
                  The default is False

   :returns: :class:`pandas.DataFrame` -- Daily climate data for a location


.. function:: get_filename(code: int, region: str) -> Dict[int, Callable[[str], str]]

   Generate an iterable URL list for downloading Daymet data.

   :Parameters: * **code** (:class:`int`) -- Endpoint code which should be one of the following:
                  * 1840: Daily
                  * 1855: Monthly average
                  * 1852: Annual average
                * **region** (:class:`str`) -- Region in the US. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico

   :returns: :class:`generator` -- An iterator of generated URLs.


.. function:: gridded_urls(code: int, bounds: Tuple[float, float, float, float], region: str, variables: List[str], dates: List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]) -> Iterator[Tuple[str, Dict[str, str]]]

   Generate an iterable URL list for downloading Daymet data.

   :Parameters: * **code** (:class:`int`) -- Endpoint code which should be one of the following:
                  * 1840: Daily
                  * 1855: Monthly average
                  * 1852: Annual average
                * **bounds** (:class:`tuple` of :class:`length 4`) -- Bounding box (west, south, east, north)
                * **region** (:class:`str`) -- Region in the US. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico
                * **variables** (:class:`list`) -- A list of Daymet variables
                * **dates** (:class:`list`) -- A list of dates

   :returns: :class:`generator` -- An iterator of generated URLs.


