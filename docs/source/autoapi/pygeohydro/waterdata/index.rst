:py:mod:`pygeohydro.waterdata`
==============================

.. py:module:: pygeohydro.waterdata

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NWIS

   Access NWIS web service.

   .. rubric:: Notes

   More information about query parameters and codes that NWIS accepts
   can be found at its help
   `webpage <https://help.waterdata.usgs.gov/codes-and-parameters>`__.

   .. py:method:: get_info(queries, expanded = False, fix_names = True)

      Send multiple queries to USGS Site Web Service.

      :Parameters: * **queries** (:class:`dict` or :class:`list` of :class:`dict`) -- A single or a list of valid queries.
                   * **expanded** (:class:`bool`, *optional*) -- Whether to get expanded site information for example drainage area,
                     default to False.
                   * **fix_names** (:class:`bool`, *optional*) -- If ``True``, reformat station names and some small annoyances,
                     defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- A correctly typed ``GeoDataFrame`` containing site(s) information.


   .. py:method:: get_parameter_codes(keyword)

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
      >>> codes.loc[codes.parameter_cd == "00060", "parm_nm"][0]
      'Discharge, cubic feet per second'


   .. py:method:: get_streamflow(station_ids, dates, freq = 'dv', mmd = False, to_xarray = False)

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



.. py:class:: WBD(layer, outfields = '*', crs = 4326)



   Access Watershed Boundary Dataset (WBD).

   .. rubric:: Notes

   This web service offers Hydrologic Unit (HU) polygon boundaries for
   the United States, Puerto Rico, and the U.S. Virgin Islands.
   For more info visit: https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. Valid layers are:

                  - ``wbdline``
                  - ``huc2``
                  - ``huc4``
                  - ``huc6``
                  - ``huc8``
                  - ``huc10``
                  - ``huc12``
                  - ``huc14``
                  - ``huc16``
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- Target spatial reference, default to ``EPSG:4326``.


.. py:function:: huc_wb_full(huc_lvl)

   Get the full watershed boundary for a given HUC level.

   .. rubric:: Notes

   This function is designed for cases where the full watershed boundary is needed
   for a given HUC level. If only a subset of the HUCs is needed, then use
   the ``pygeohydro.WBD`` class. The full dataset is downloaded from the National Maps'
   `WBD staged products <https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Hydrography/WBD/HU2/Shape/>`__.

   :Parameters: **huc_lvl** (:class:`int`) -- HUC level, must be even numbers between 2 and 16.

   :returns: :class:`geopandas.GeoDataFrame` -- The full watershed boundary for the given HUC level.


.. py:function:: irrigation_withdrawals()

   Get monthly water use for irrigation at HUC12-level for CONUS.

   .. rubric:: Notes

   Dataset is retrieved from https://doi.org/10.5066/P9FDLY8P.


