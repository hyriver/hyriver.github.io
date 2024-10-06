pygeohydro.stnfloodevents
=========================

.. py:module:: pygeohydro.stnfloodevents

.. autoapi-nested-parse::

   Access USGS Short-Term Network (STN) via Restful API.







Module Contents
---------------

.. py:class:: STNFloodEventData

   Client for STN Flood Event Data's RESTFUL Service API.

   Advantages of using this client are:

   - The user does not need to know the details of RESTFUL in
     general and of this API specifically.
   - Parses the data and returns Python objects
     (e.g., pandas.DataFrame, geopandas.GeoDataFrame) instead of JSON.
   - Convenience functions are offered for data dictionaries.
   - Geo-references the data where applicable.

   .. attribute:: service_url

      The service url of the STN Flood Event Data RESTFUL Service API.

      :type: :class:`str`

   .. attribute:: data_dictionary_url

      The data dictionary url of the STN Flood Event Data RESTFUL Service API.

      :type: :class:`str`

   .. attribute:: service_crs

      The CRS of the data from the service which is ``EPSG:4326``.

      :type: :class:`int`

   .. attribute:: instruments_query_params

      The accepted query parameters for the instruments data type.
      Accepted values are ``SensorType``, ``CurrentStatus``, ``States``,
      ``Event``, ``County``, ``DeploymentType``, ``EventType``,
      ``EventStatus``, and ``CollectionCondition``.

      :type: :class:`set`

   .. attribute:: peaks_query_params

      The accepted query parameters for the peaks data type.
      Accepted values are ``EndDate``, ``States``, ``Event``, ``StartDate``,
      ``County``, ``EventType``, and ``EventStatus``.

      :type: :class:`set`

   .. attribute:: hwms_query_params

      The accepted query parameters for the hwms data type.
      Accepted values are ``EndDate``, ``States``, ``Event``, ``StartDate``,
      ``County``, ``EventType``, and ``EventStatus``.

      :type: :class:`set`

   .. attribute:: sites_query_params

      The accepted query parameters for the sites data type.
      Accepted values are ``OPDefined``, ``HousingTypeOne``, ``NetworkName``,
      ``HousingTypeSeven``, ``RDGOnly``, ``HWMOnly``, ``Event``,
      ``SensorOnly``, ``State``, ``SensorType``, and ``HWMSurveyed``.

      :type: :class:`set`

   .. rubric:: Notes

   Point data from the service is assumed to be in the WGS84
   coordinate reference system (``EPSG:4326``).

   .. rubric:: References

   * `USGS Short-Term Network (STN) <https://stn.wim.usgs.gov/STNWeb/#/>`__
   * `All Sensors API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/Sensor/AllSensors>`__
   * `All Peak Summary API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/PeakSummary/AllPeakSummaries>`__
   * `All HWM API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/HWM/AllHWMs>`__
   * `All Sites API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/Site/AllSites>`__
   * `USGS Flood Event Viewer: Providing Hurricane and Flood Response Data <https://www.usgs.gov/mission-areas/water-resources/science/usgs-flood-event-viewer-providing-hurricane-and-flood>`__
   * `A USGS guide for finding and interpreting high-water marks <https://www.usgs.gov/media/videos/a-usgs-guide-finding-and-interpreting-high-water-marks>`__
   * `High-Water Marks and Flooding <https://www.usgs.gov/special-topics/water-science-school/science/high-water-marks-and-flooding>`__
   * `Identifying and preserving high-water mark data <https://doi.org/10.3133/tm3A24>`__


   .. py:method:: data_dictionary(data_type: str, *, as_dict: Literal[False] = False, async_retriever_kwargs: dict[str, Any] | None = None) -> pandas.DataFrame
                  data_dictionary(data_type: str, *, as_dict: Literal[True], async_retriever_kwargs: dict[str, Any] | None = None) -> dict[str, Any]
      :classmethod:


      Retrieve data dictionaries from the STN Flood Event Data API.

      :Parameters: * **data_type** (:class:`str`) -- The data source from STN Flood Event Data API.
                     It can be ``instruments``, ``peaks``, ``hwms``, or ``sites``.
                   * **as_dict** (:class:`bool`, *default* :class:`= False`) -- If True, return the data dictionary as a dictionary.
                     Otherwise, it returns as ``pandas.DataFrame``.
                   * **async_retriever_kwargs** (:class:`dict`, *optional*) -- Additional keyword arguments to pass to
                     ``async_retriever.retrieve_json()``. The ``url`` and ``request_kwds``
                     options are already set.

      :returns: :class:`pandas.DataFrame` or :class:`dict` -- The retrieved data dictionary as pandas.DataFrame or dict.

      .. seealso::

         :meth:`~get_all_data`
             Retrieves all data for a given data type.
         
         :meth:`~get_filtered_data`
             Retrieves filtered data for a given data type.

      .. rubric:: Examples

      >>> from pygeohydro import STNFloodEventData
      >>> data = STNFloodEventData.data_dictionary(data_type="instruments", as_dict=False)  # doctest: +SKIP
      >>> data.shape[1]  # doctest: +SKIP
      2
      >>> data.columns  # doctest: +SKIP
      Index(['Field', 'Definition'], dtype='object')



   .. py:method:: get_all_data(data_type: str, *, as_list: Literal[False] = False, crs: CRSTYPE = 4326, async_retriever_kwargs: dict[str, Any] | None = None) -> geopandas.GeoDataFrame | pandas.DataFrame
                  get_all_data(data_type: str, *, as_list: Literal[True], crs: CRSTYPE = 4326, async_retriever_kwargs: dict[str, Any] | None = None) -> list[dict[str, Any]]
      :classmethod:


      Retrieve all data from the STN Flood Event Data API.

      :Parameters: * **data_type** (:class:`str`) -- The data source from STN Flood Event Data API.
                     It can be ``instruments``, ``peaks``, ``hwms``, or ``sites``.
                   * **as_list** (:class:`bool`, *optional*) -- If True, return the data as a list, defaults to False.
                   * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- Desired Coordinate reference system (CRS) of output.
                     Only used for GeoDataFrames with ``hwms`` and ``sites`` data types.
                   * **async_retriever_kwargs** (:class:`dict`, *optional*) -- Additional keyword arguments to pass to
                     ``async_retriever.retrieve_json()``. The ``url`` and ``request_kwds``
                     options are already set.

      :returns: :class:`geopandas.GeoDataFrame` or :class:`pandas.DataFrame` or :class:`list` of :class:`dict` -- The retrieved data as a GeoDataFrame, DataFrame, or a list of dictionaries.

      :raises InputValueError: If the input data_type is not one of
          ``instruments``, ``peaks``, ``hwms``, or ``sites``

      .. seealso::

         :meth:`~get_filtered_data`
             Retrieves filtered data for a given data type.
         
         :meth:`~data_dictionary`
             Retrieves the data dictionary for a given data type.

      .. rubric:: Notes

      Notice schema differences between the data dictionaries, filtered data
      queries, and all data queries. This is a known issue and is being addressed
      by USGS.

      .. rubric:: Examples

      >>> from pygeohydro.stnfloodevents import STNFloodEventData
      >>> data = STNFloodEventData.get_all_data(data_type="instruments")
      >>> data.shape[1]
      18
      >>> data.columns
      Index(['instrument_id', 'sensor_type_id', 'deployment_type_id',
             'location_description', 'serial_number', 'interval', 'site_id',
             'event_id', 'inst_collection_id', 'housing_type_id', 'sensor_brand_id',
             'vented', 'instrument_status', 'data_files', 'files', 'last_updated',
             'last_updated_by', 'housing_serial_number'],
             dtype='object')



   .. py:method:: get_filtered_data(data_type: str, query_params: dict[str, Any] | None = None, *, as_list: Literal[False] = False, crs: CRSTYPE = 4326, async_retriever_kwargs: dict[str, Any] | None = None) -> geopandas.GeoDataFrame | pandas.DataFrame
                  get_filtered_data(data_type: str, query_params: dict[str, Any] | None = None, *, as_list: Literal[True], crs: CRSTYPE = 4326, async_retriever_kwargs: dict[str, Any] | None = None) -> list[dict[str, Any]]
      :classmethod:


      Retrieve filtered data from the STN Flood Event Data API.

      :Parameters: * **data_type** (:class:`str`) -- The data source from STN Flood Event Data API.
                     It can be ``instruments``, ``peaks``, ``hwms``, or ``sites``.
                   * **query_params** (:class:`dict`, *optional*) -- RESTFUL API query parameters. For accepted values, see
                     the STNFloodEventData class attributes :attr:`~instruments_query_params`,
                     :attr:`~peaks_query_params`, :attr:`~hwms_query_params`, and
                     :attr:`~sites_query_params` for available values.

                     Also, see the API documentation for each data type for more information:
                         - `instruments <https://stn.wim.usgs.gov/STNServices/Documentation/Sensor/FilteredSensors>`__
                         - `peaks <https://stn.wim.usgs.gov/STNServices/Documentation/PeakSummary/FilteredPeakSummaries>`__
                         - `hwms <https://stn.wim.usgs.gov/STNServices/Documentation/HWM/FilteredHWMs>`__
                         - `sites <https://stn.wim.usgs.gov/STNServices/Documentation/Site/FilteredSites>`__
                   * **as_list** (:class:`bool`, *optional*) -- If True, return the data as a list, defaults to False.
                   * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- Desired Coordinate reference system (CRS) of output.
                     Only used for GeoDataFrames outputs.
                   * **async_retriever_kwargs** (:class:`dict`, *optional*) -- Additional keyword arguments to pass to
                     ``async_retriever.retrieve_json()``. The ``url`` and ``request_kwds``
                     options are already set.

      :returns: :class:`geopandas.GeoDataFrame` or :class:`pandas.DataFrame` or :class:`list` of :class:`dict` -- The retrieved data as a GeoDataFrame, DataFrame, or a
                list of dictionaries.

      :raises InputValueError: If the input data_type is not one of
          ``instruments``, ``peaks``, ``hwms``, or ``sites``
      :raises InputValueError: If any of the input query_params are not in accepted
          parameters (See :attr:`~instruments_query_params`,
          :attr:`~peaks_query_params`, :attr:`~hwms_query_params`,
          or :attr:`~sites_query_params`).

      .. seealso::

         :meth:`~get_all_data`
             Retrieves all data for a given data type.
         
         :meth:`~data_dictionary`
             Retrieves the data dictionary for a given data type.

      .. rubric:: Notes

      Notice schema differences between the data dictionaries,
      filtered data queries, and all data queries. This is a known
      issue and is being addressed by USGS.

      .. rubric:: Examples

      >>> from pygeohydro.stnfloodevents import STNFloodEventData
      >>> query_params = {"States": "SC, CA"}
      >>> data = STNFloodEventData.get_filtered_data(data_type="instruments", query_params=query_params)
      >>> data.shape[1]
      34
      >>> data.columns
      Index(['sensorType', 'deploymentType', 'eventName', 'collectionCondition',
          'housingType', 'sensorBrand', 'statusId', 'timeStamp', 'site_no',
          'latitude', 'longitude', 'siteDescription', 'networkNames', 'stateName',
          'countyName', 'siteWaterbody', 'siteHDatum', 'sitePriorityName',
          'siteZone', 'siteHCollectMethod', 'sitePermHousing', 'instrument_id',
          'sensor_type_id', 'deployment_type_id', 'location_description',
          'serial_number', 'housing_serial_number', 'interval', 'site_id',
          'vented', 'instrument_status', 'data_files', 'files', 'geometry'],
          dtype='object')



.. py:function:: stn_flood_event(data_type, query_params = None)

   Retrieve data from the STN Flood Event Data API.

   :Parameters: * **data_type** (:class:`str`) -- The data source from STN Flood Event Data API.
                  It can be ``instruments``, ``peaks``, ``hwms``, or ``sites``.
                * **query_params** (:class:`dict`, *optional*) -- RESTFUL API query parameters, defaults to ``None`` which returns
                  a ``pandas.DataFrame`` of information about the given ``data_type``.
                  For accepted values, see the ``STNFloodEventData`` class attributes
                  :attr:`~.STNFloodEventData.instruments_query_params`,
                  :attr:`~.STNFloodEventData.peaks_query_params`,
                  :attr:`~.STNFloodEventData.hwms_query_params`, and
                  :attr:`~.STNFloodEventData.sites_query_params` for available values.

                  Also, see the API documentation for each data type for more information:

                  - `instruments <https://stn.wim.usgs.gov/STNServices/Documentation/Sensor/FilteredSensors>`__
                  - `peaks <https://stn.wim.usgs.gov/STNServices/Documentation/PeakSummary/FilteredPeakSummaries>`__
                  - `hwms <https://stn.wim.usgs.gov/STNServices/Documentation/HWM/FilteredHWMs>`__
                  - `sites <https://stn.wim.usgs.gov/STNServices/Documentation/Site/FilteredSites>`__

   :returns: :class:`geopandas.GeoDataFrame` or :class:`pandas.DataFrame` -- The retrieved data as a GeoDataFrame or DataFrame
             (if ``query_params`` is not passed).

   :raises InputValueError: If the input data_type is not one of
       ``instruments``, ``peaks``, ``hwms``, or ``sites``
   :raises InputValueError: If any of the input query_params are not in accepted
       parameters.

   .. rubric:: References

   * `USGS Short-Term Network (STN) <https://stn.wim.usgs.gov/STNWeb/#/>`__
   * `Filtered Sensors API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/Sensor/FilteredSensors>`__
   * `Peak Summary API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/PeakSummary/FilteredPeakSummaries>`__
   * `Filtered HWM API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/HWM/FilteredHWMs>`__
   * `Filtered Sites API Documentation <https://stn.wim.usgs.gov/STNServices/Documentation/Site/FilteredSites>`__
   * `USGS Flood Event Viewer: Providing Hurricane and Flood Response Data <https://www.usgs.gov/mission-areas/water-resources/science/usgs-flood-event-viewer-providing-hurricane-and-flood>`__
   * `A USGS guide for finding and interpreting high-water marks <https://www.usgs.gov/media/videos/a-usgs-guide-finding-and-interpreting-high-water-marks>`__
   * `High-Water Marks and Flooding  <https://www.usgs.gov/special-topics/water-science-school/science/high-water-marks-and-flooding>`__
   * `Identifying and preserving high-water mark data <https://doi.org/10.3133/tm3A24>`__

   .. rubric:: Notes

   Notice schema differences between the data dictionaries,
   filtered data queries, and all data queries. This is a known
   issue and is being addressed by USGS.

   .. rubric:: Examples

   >>> query_params = {"States": "SC, CA"}
   >>> data = stn_flood_event("instruments", query_params=query_params)
   >>> data.shape[1]
   34
   >>> data.columns
   Index(['sensorType', 'deploymentType', 'eventName', 'collectionCondition',
       'housingType', 'sensorBrand', 'statusId', 'timeStamp', 'site_no',
       'latitude', 'longitude', 'siteDescription', 'networkNames', 'stateName',
       'countyName', 'siteWaterbody', 'siteHDatum', 'sitePriorityName',
       'siteZone', 'siteHCollectMethod', 'sitePermHousing', 'instrument_id',
       'sensor_type_id', 'deployment_type_id', 'location_description',
       'serial_number', 'housing_serial_number', 'interval', 'site_id',
       'vented', 'instrument_status', 'data_files', 'files', 'geometry'],
       dtype='object')


