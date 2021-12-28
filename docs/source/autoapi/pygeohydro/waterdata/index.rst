:py:mod:`pygeohydro.waterdata`
==============================

.. py:module:: pygeohydro.waterdata

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NWIS(expire_after = EXPIRE, disable_caching = False)

   Access NWIS web service.

   :Parameters: * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   .. py:method:: get_info(self, queries, expanded = False)

      Send multiple queries to USGS Site Web Service.

      :Parameters: * **queries** (:class:`dict` or :class:`list` of :class:`dict`) -- A single or a list of valid queries.
                   * **expanded** (:class:`bool`, *optional*) -- Whether to get expanded sit information for example drainage area, default to False.

      :returns: :class:`pandas.DataFrame` -- A typed dataframe containing the site information.


   .. py:method:: get_parameter_codes(self, keyword)

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


   .. py:method:: get_streamflow(self, station_ids, dates, freq = 'dv', mmd = False, to_xarray = False)

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


   .. py:method:: retrieve_rdb(self, url, payloads)

      Retrieve and process requests with RDB format.

      :Parameters: * **url** (:class:`str`) -- Name of USGS REST service, valid values are ``site``, ``dv``, ``iv``,
                     ``gwlevels``, and ``stat``. Please consult USGS documentation
                     `here <https://waterservices.usgs.gov/rest>`__ for more information.
                   * **payloads** (:class:`list` of :class:`dict`) -- List of target payloads.

      :returns: :class:`pandas.DataFrame` -- Requested features as a pandas's DataFrame.



.. py:class:: WaterQuality(expire_after = EXPIRE, disable_caching = False)

   Water Quality Web Service https://www.waterqualitydata.us.

   .. rubric:: Notes

   This class has a number of convenience methods to retrieve data from the
   Water Quality Data. Since there are many parameter combinations that can be
   used to retrieve data, a general method is also provided to retrieve data from
   any of the valid endpoints. You can use ``get_json`` to retrieve stations info
   as a ``geopandas.GeoDataFrame`` or ``get_csv`` to retrieve stations data as a
   ``pandas.DataFrame``. You can construct a dictionary of the parameters and pass
   it to one of these functions. For more information on the parameters, please
   consult the
   `Water Quality Data documentation <https://www.waterqualitydata.us/webservices_documentation>`__.

   :Parameters: * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   .. py:method:: data_bystation(self, station_ids, wq_kwds)

      Retrieve data for a single station.

      :Parameters: * **station_ids** (:class:`str` or :class:`list` of :class:`str`) -- Station ID(s). The IDs should have the format "Agency code-Station ID".
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`pandas.DataFrame` -- DataFrame of data for the stations.


   .. py:method:: get_csv(self, endpoint, kwds, request_method = 'GET')

      Get the CSV response from the Water Quality Web Service.

      :Parameters: * **endpoint** (:class:`str`) -- Endpoint of the Water Quality Web Service.
                   * **kwds** (:class:`dict`) -- Water Quality Web Service keyword arguments.
                   * **request_method** (:class:`str`, *optional*) -- HTTP request method. Default to GET.

      :returns: :class:`pandas.DataFrame` -- The web service response as a DataFrame.


   .. py:method:: get_json(self, endpoint, kwds, request_method = 'GET')

      Get the JSON response from the Water Quality Web Service.

      :Parameters: * **endpoint** (:class:`str`) -- Endpoint of the Water Quality Web Service.
                   * **kwds** (:class:`dict`) -- Water Quality Web Service keyword arguments.
                   * **request_method** (:class:`str`, *optional*) -- HTTP request method. Default to GET.

      :returns: :class:`geopandas.GeoDataFrame` -- The web service response as a GeoDataFrame.


   .. py:method:: get_param_table(self)

      Get the parameter table from the USGS Water Quality Web Service.


   .. py:method:: lookup_domain_values(self, endpoint)

      Get the domain values for the target endpoint.


   .. py:method:: station_bybbox(self, bbox, wq_kwds)

      Retrieve station info within bounding box.

      :Parameters: * **bbox** (:class:`tuple` of :class:`float`) -- Bounding box coordinates (west, south, east, north) in epsg:4326.
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of station info within the bounding box.


   .. py:method:: station_bydistance(self, lon, lat, radius, wq_kwds)

      Retrieve station within a radius (decimal miles) of a point.

      :Parameters: * **lon** (:class:`float`) -- Longitude of point.
                   * **lat** (:class:`float`) -- Latitude of point.
                   * **radius** (:class:`float`) -- Radius (decimal miles) of search.
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of station info within the radius of the point.



.. py:function:: interactive_map(bbox, crs = DEF_CRS, nwis_kwds = None, expire_after = EXPIRE, disable_caching = False)

   Generate an interactive map including all USGS stations within a bounding box.

   :Parameters: * **bbox** (:class:`tuple`) -- List of corners in this order (west, south, east, north)
                * **crs** (:class:`str`, *optional*) -- CRS of the input bounding box, defaults to EPSG:4326.
                * **nwis_kwds** (:class:`dict`, *optional*) -- Optional keywords to include in the NWIS request as a dictionary like so:
                  ``{"hasDataTypeCd": "dv,iv", "outputDataTypeCd": "dv,iv", "parameterCd": "06000"}``.
                  Default to None.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`folium.Map` -- Interactive map within a bounding box.

   .. rubric:: Examples

   >>> import pygeohydro as gh
   >>> nwis_kwds = {"hasDataTypeCd": "dv,iv", "outputDataTypeCd": "dv,iv"}
   >>> m = gh.interactive_map((-69.77, 45.07, -69.31, 45.45), nwis_kwds=nwis_kwds)
   >>> n_stations = len(m.to_dict()["children"]) - 1
   >>> n_stations
   10


