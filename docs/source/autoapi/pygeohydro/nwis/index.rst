pygeohydro.nwis
===============

.. py:module:: pygeohydro.nwis

.. autoapi-nested-parse::

   Accessing NWIS.







Module Contents
---------------

.. py:class:: NWIS

   Access NWIS web service.

   .. rubric:: Notes

   More information about query parameters and codes that NWIS accepts
   can be found at its help
   `webpage <https://help.waterdata.usgs.gov/codes-and-parameters>`__.


   .. py:method:: get_info(queries, expanded = False, fix_names = True, nhd_info = False)
      :classmethod:


      Send multiple queries to USGS Site Web Service.

      :Parameters: * **queries** (:class:`dict` or :class:`list` of :class:`dict`) -- A single or a list of valid queries.
                   * **expanded** (:class:`bool`, *optional*) -- Whether to get expanded site information for example drainage area,
                     default to False.
                   * **fix_names** (:class:`bool`, *optional*) -- If ``True``, reformat station names and some small annoyances,
                     defaults to ``True``.
                   * **nhd_info** (:class:`bool`, *optional*) -- If ``True``, get NHD information for each site, defaults to ``False``.
                     This will add four new columns: ``nhd_comid``, ``nhd_areasqkm``,
                     ``nhd_reachcode``, and ``nhd_measure``. Where ``nhd_id`` is the NHD
                     COMID of the flowline that the site is located in, ``nhd_reachcode``
                     is the NHD Reach Code that the site is located in, and ``nhd_measure``
                     is the measure along the flowline that the site is located at.

      :returns: :class:`geopandas.GeoDataFrame` -- A correctly typed ``GeoDataFrame`` containing site(s) information.



   .. py:method:: get_parameter_codes(keyword)
      :classmethod:


      Search for parameter codes by name or number.

      .. rubric:: Notes

      NWIS guideline for keywords is as follows:

          By default an exact search is made. To make a partial search the term
          should be prefixed and suffixed with a % sign. The % sign matches zero
          or more characters at the location. For example, to find all with "discharge"
          enter %discharge% in the field. % will match any number of characters
          (including zero characters) at the location.

      :Parameters: **keyword** (:class:`str`) -- Keyword to search for parameters by name of number.

      :returns: :class:`pandas.DataFrame` -- Matched parameter codes as a dataframe with their description.

      .. rubric:: Examples

      >>> from pygeohydro import NWIS
      >>> nwis = NWIS()
      >>> codes = nwis.get_parameter_codes("%discharge%")
      >>> codes.loc[codes.parameter_cd == "00060", "parm_nm"].iloc[0]
      'Discharge, cubic feet per second'



   .. py:method:: get_streamflow(station_ids: collections.abc.Sequence[str] | str, dates: tuple[str, str], freq: str = 'dv', mmd: bool = False, *, to_xarray: Literal[False] = False) -> pandas.DataFrame
                  get_streamflow(station_ids: collections.abc.Sequence[str] | str, dates: tuple[str, str], freq: str = 'dv', mmd: bool = False, *, to_xarray: Literal[True]) -> xarray.Dataset
      :classmethod:


      Get mean daily streamflow observations from USGS.

      :Parameters: * **station_ids** (:class:`str`, :class:`list`) -- The gage ID(s)  of the USGS station.
                   * **dates** (:class:`tuple`) -- Start and end dates as a tuple (start, end).
                   * **freq** (:class:`str`, *optional*) -- The frequency of the streamflow data, defaults to ``dv`` (daily values).
                     Valid frequencies are ``dv`` (daily values), ``iv`` (instantaneous values).
                     Note that for ``iv`` the time zone for the input dates is assumed to be UTC.
                   * **mmd** (:class:`bool`, *optional*) -- Convert cms to mm/day based on the contributing drainage area of the stations.
                     Defaults to False.
                   * **to_xarray** (:class:`bool`, *optional*) -- Whether to return a xarray.Dataset. Defaults to False.

      :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- Streamflow data observations in cubic meter per second (cms). The stations that
                don't provide the requested discharge data in the target period will be dropped.
                Note that when frequency is set to ``iv`` the time zone is converted to UTC.



   .. py:method:: retrieve_rdb(url, payloads)
      :staticmethod:


      Retrieve and process requests with RDB format.

      :Parameters: * **url** (:class:`str`) -- Name of USGS REST service, valid values are ``site``, ``dv``, ``iv``,
                     ``gwlevels``, and ``stat``. Please consult USGS documentation
                     `here <https://waterservices.usgs.gov/rest>`__ for more information.
                   * **payloads** (:class:`list` of :class:`dict`) -- List of target payloads.

      :returns: :class:`pandas.DataFrame` -- Requested features as a pandas's DataFrame.



.. py:function:: streamflow_fillna(streamflow, missing_max = 5)

   Fill missing data (NAN) in daily streamflow observations.

   It drops stations with more than ``missing_max`` days missing data
   per year. Missing data in the remaining stations, are filled with
   day-of-year average over the entire dataset.

   :Parameters: * **streamflow** (:class:`xarray.DataArray` or :class:`pandas.DataFrame` or :class:`pandas.Series`) -- Daily streamflow observations with at least 10 years of daily data.
                * **missing_max** (:class:`int`) -- Maximum allowed number of missing daily data per year for filling,
                  defaults to 5.

   :returns: :class:`xarray.DataArray` or :class:`pandas.DataFrame` or :class:`pandas.Series` -- Streamflow observations with missing data filled for stations with
             less than ``missing_max`` days of missing data.


