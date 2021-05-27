:mod:`pydaymet.core`
====================

.. py:module:: pydaymet.core

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:class:: Daymet(variables: Optional[Union[Iterable[str], str]] = None, pet: bool = False, time_scale: str = 'daily', region: str = 'na')

   Base class for Daymet requests.

   :Parameters: * **variables** (:class:`str` or :class:`list` or :class:`tuple`, *optional*) -- List of variables to be downloaded. The acceptable variables are:
                  ``tmin``, ``tmax``, ``prcp``, ``srad``, ``vp``, ``swe``, ``dayl``
                  Descriptions can be found `here <https://daymet.ornl.gov/overview>`__.
                  Defaults to None i.e., all the variables are downloaded.
                * **pet** (:class:`bool`, *optional*) -- Whether to compute evapotranspiration based on
                  `UN-FAO 56 paper <http://www.fao.org/3/X0490E/x0490e06.htm#equation>`__.
                  The default is False
                * **time_scale** (:class:`str`, *optional*) -- Data time scale which can be daily, monthly (monthly summaries),
                  or annual (annual summaries). Defaults to daily.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to na. Acceptable values are:
                  * na: Continental North America
                  * hi: Hawaii
                  * pr: Puerto Rico

   .. method:: check_dates(dates: Union[Tuple[str, str], Union[int, List[int]]]) -> None
      :staticmethod:

      Check if input dates are in correct format and valid.


   .. method:: check_input_validity(inp: str, valid_list: Iterable[str]) -> str
      :staticmethod:

      Check the validity of input based on a list of valid options.


   .. method:: dates_todict(dates: Tuple[str, str]) -> Dict[str, str]
      :staticmethod:

      Set dates by start and end dates as a tuple, (start, end).


   .. method:: dates_tolist(self, dates: Tuple[str, str]) -> List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **dates** (:class:`tuple`) -- Target start and end dates.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.


   .. method:: pet_bycoords(clm_df: pd.DataFrame, coords: Tuple[float, float], crs: str = DEF_CRS, alt_unit: bool = False) -> pd.DataFrame
      :staticmethod:

      Compute Potential EvapoTranspiration using Daymet dataset for a single location.

      .. rubric:: Notes

      The method is based on
      `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm#equation>`__.
      Moreover, we assume that soil heat flux density is zero and wind speed at 2 m height
      is 2 m/s. The following variables are required:
      tmin (deg c), tmax (deg c), lat, lon, vp (Pa), srad (W/m2), dayl (s/day)
      The computed PET's unit is mm/day.

      :Parameters: * **clm_df** (:class:`~pandas.DataFrame`) -- A dataframe with columns named as follows:
                     ``tmin (deg c)``, ``tmax (deg c)``, ``vp (Pa)``, ``srad (W/m^2)``, ``dayl (s)``
                   * **coords** (:class:`tuple` of :class:`floats`) -- Coordinates of the daymet data location as a tuple, (x, y).
                   * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to epsg:4326
                   * **alt_unit** (:class:`str`, *optional*) -- Whether to use alternative units rather than the official ones, defaults to False.

      :returns: :class:`pandas.DataFrame` -- The input DataFrame with an additional column named ``pet (mm/day)``


   .. method:: pet_bygrid(clm_ds: xr.Dataset) -> xr.Dataset
      :staticmethod:

      Compute Potential EvapoTranspiration using Daymet dataset.

      The method is based on
      `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm#equation>`__.
      Moreover, we assume that soil heat flux density is zero and wind speed at 2 m height
      is 2 m/s. The following variables are required:
      tmin (deg c), tmax (deg c), lat, lon, vp (Pa), srad (W/m2), dayl (s/day)
      The computed PET's unit is mm/day.

      :Parameters: **clm_ds** (:class:`xarray.DataArray`) -- The dataset should include the following variables:
                   ``tmin``, ``tmax``, ``lat``, ``lon``, ``vp``, ``srad``, ``dayl``

      :returns: :class:`xarray.DataArray` -- The input dataset with an additional variable called ``pet``.


   .. method:: years_todict(years: Union[List[int], int]) -> Dict[str, str]
      :staticmethod:

      Set date by list of year(s).


   .. method:: years_tolist(self, years: Union[List[int], int]) -> List[Tuple[pd.DatetimeIndex, pd.DatetimeIndex]]

      Correct dates for Daymet accounting for leap years.

      Daymet doesn't account for leap years and removes Dec 31 when
      it's leap year.

      :Parameters: **years** (:class:`list`) -- A list of target years.

      :returns: :class:`list` -- All the dates in the Daymet database within the provided date range.



