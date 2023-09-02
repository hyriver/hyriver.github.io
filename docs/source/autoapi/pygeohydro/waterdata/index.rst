:py:mod:`pygeohydro.waterdata`
==============================

.. py:module:: pygeohydro.waterdata

.. autoapi-nested-parse::

   Accessing WaterData related APIs.



Module Contents
---------------

.. py:class:: SensorThings


   Class for interacting with SensorThings API.

   .. py:method:: odata_helper(columns = None, conditionals = None, expand = None, max_count = None, extra_params = None)
      :staticmethod:

      Generate Odata filters for SensorThings API.

      :Parameters: * **columns** (:class:`list` of :class:`str`, *optional*) -- Columns to be selected from the database, defaults to ``None``.
                   * **conditionals** (:class:`str`, *optional*) -- Conditionals to be applied to the database, defaults to ``None``.
                     Note that the conditionals should have the form of
                     ``cond1 operator 'value' and/or cond2 operator 'value``.
                     For example:
                     ``properties/monitoringLocationType eq 'Stream' and ...``
                   * **expand** (:class:`dict` of :class:`dict`, *optional*) -- Expand the properties of the selected columns, defaults to ``None``.
                     Note that the expand should have the form of
                     ``{Property: {func: value, ...}}``. For example: ``{"Locations":
                     {"select": "location", "filter": "ObservedProperty/@iot.id eq '00060'"}}``
                   * **max_count** (:class:`int`, *optional*) -- Maximum number of items to be returned, defaults to ``None``.
                   * **extra_params** (:class:`dict`, *optional*) -- Extra parameters to be added to the Odata filter, defaults to ``None``.

      :returns: **odata** (:class:`dict`) -- Odata filter for the SensorThings API.


   .. py:method:: query_byodata(odata, outformat = 'json')

      Query the SensorThings API by Odata filter.

      :Parameters: * **odata** (:class:`str`) -- Odata filter for the SensorThings API.
                   * **outformat** (:class:`str`, *optional*) -- Format of the response, defaults to ``json``.
                     Valid values are ``json`` and ``geojson``.

      :returns: :class:`pandas.DataFrame` or :class:`geopandas.GeoDataFrame` -- Requested data.


   .. py:method:: sensor_info(sensor_ids)

      Query the SensorThings API by a sensor ID.

      :Parameters: **sensor_ids** (:class:`str` or :class:`list` of :class:`str`) -- A single or list of sensor IDs, e.g., ``USGS-09380000``.

      :returns: :class:`pandas.DataFrame` -- Requested sensor data.


   .. py:method:: sensor_property(sensor_property, sensor_ids)

      Query a sensor property.

      :Parameters: * **sensor_property** (:class:`str` or :class:`list` of :class:`str`) -- A sensor property, Valid properties are ``Datastreams``,
                     ``MultiDatastreams``, ``Locations``, ``HistoricalLocations``,
                     ``TaskingCapabilities``.
                   * **sensor_ids** (:class:`str` or :class:`list` of :class:`str`) -- A single or list of sensor IDs, e.g., ``USGS-09380000``.

      :returns: :class:`pandas.DataFrame` -- A dataframe containing the requested property.



.. py:class:: WaterQuality


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

   .. py:method:: data_bystation(station_ids, wq_kwds)

      Retrieve data for a single station.

      :Parameters: * **station_ids** (:class:`str` or :class:`list` of :class:`str`) -- Station ID(s). The IDs should have the format "Agency code-Station ID".
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`pandas.DataFrame` -- DataFrame of data for the stations.


   .. py:method:: get_csv(endpoint, kwds, request_method = 'GET')

      Get the CSV response from the Water Quality Web Service.

      :Parameters: * **endpoint** (:class:`str`) -- Endpoint of the Water Quality Web Service.
                   * **kwds** (:class:`dict`) -- Water Quality Web Service keyword arguments.
                   * **request_method** (:class:`str`, *optional*) -- HTTP request method. Default to GET.

      :returns: :class:`pandas.DataFrame` -- The web service response as a DataFrame.


   .. py:method:: get_json(endpoint, kwds, request_method = 'GET')

      Get the JSON response from the Water Quality Web Service.

      :Parameters: * **endpoint** (:class:`str`) -- Endpoint of the Water Quality Web Service.
                   * **kwds** (:class:`dict`) -- Water Quality Web Service keyword arguments.
                   * **request_method** (:class:`str`, *optional*) -- HTTP request method. Default to GET.

      :returns: :class:`geopandas.GeoDataFrame` -- The web service response as a GeoDataFrame.


   .. py:method:: get_param_table()

      Get the parameter table from the USGS Water Quality Web Service.


   .. py:method:: lookup_domain_values(endpoint)

      Get the domain values for the target endpoint.


   .. py:method:: station_bybbox(bbox, wq_kwds)

      Retrieve station info within bounding box.

      :Parameters: * **bbox** (:class:`tuple` of :class:`float`) -- Bounding box coordinates (west, south, east, north) in epsg:4326.
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of station info within the bounding box.


   .. py:method:: station_bydistance(lon, lat, radius, wq_kwds)

      Retrieve station within a radius (decimal miles) of a point.

      :Parameters: * **lon** (:class:`float`) -- Longitude of point.
                   * **lat** (:class:`float`) -- Latitude of point.
                   * **radius** (:class:`float`) -- Radius (decimal miles) of search.
                   * **wq_kwds** (:class:`dict`, *optional*) -- Water Quality Web Service keyword arguments. Default to None.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of station info within the radius of the point.



