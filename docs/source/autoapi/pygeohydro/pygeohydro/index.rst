:py:mod:`pygeohydro.pygeohydro`
===============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NID(version = 2)



   Retrieve data from the National Inventory of Dams web service.

   :Parameters: **version** (:class:`str`, *optional*) -- The database version. Version 2 and 3 are available. Version 2 has
                NID 2019 data and version 3 includes more recent data as well. At the
                moment both services are experimental and might not always work. The
                default version is 2. More information can be found at https://damsdev.net.


.. py:class:: NWIS

   Access NWIS web service.

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


   .. py:method:: retrieve_rdb(url, payloads)
      :staticmethod:

      Retrieve and process requests with RDB format.

      :Parameters: * **service** (:class:`str`) -- Name of USGS REST service, valid values are ``site``, ``dv``, ``iv``,
                     ``gwlevels``, and ``stat``. Please consult USGS documentation
                     `here <https://waterservices.usgs.gov/rest>`__ for more information.
                   * **payloads** (:class:`list` of :class:`dict`) -- List of target payloads.

      :returns: :class:`pandas.DataFrame` -- Requested features as a pandas's DataFrame.



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



.. py:function:: cover_statistics(ds)

   Percentages of the categorical NLCD cover data.

   :Parameters: **ds** (:class:`xarray.DataArray`) -- Cover DataArray from a LULC Dataset from the ``nlcd`` function.

   :returns: :class:`dict` -- Statistics of NLCD cover data


.. py:function:: interactive_map(bbox, crs = DEF_CRS, nwis_kwds = None)

   Generate an interactive map including all USGS stations within a bounding box.

   :Parameters: * **bbox** (:class:`tuple`) -- List of corners in this order (west, south, east, north)
                * **crs** (:class:`str`, *optional*) -- CRS of the input bounding box, defaults to EPSG:4326.
                * **nwis_kwds** (:class:`dict`, *optional*) -- Optional keywords to include in the NWIS request as a dictionary like so:
                  ``{"hasDataTypeCd": "dv,iv", "outputDataTypeCd": "dv,iv", "parameterCd": "06000"}``.
                  Default to None.

   :returns: :class:`folium.Map` -- Interactive map within a bounding box.

   .. rubric:: Examples

   >>> import pygeohydro as gh
   >>> nwis_kwds = {"hasDataTypeCd": "dv,iv", "outputDataTypeCd": "dv,iv"}
   >>> m = gh.interactive_map((-69.77, 45.07, -69.31, 45.45), nwis_kwds=nwis_kwds)
   >>> n_stations = len(m.to_dict()["children"]) - 1
   >>> n_stations
   10


.. py:function:: nlcd(geometry, resolution, years = None, region = 'L48', geo_crs = DEF_CRS, crs = DEF_CRS)

   Get data from NLCD database (2016).

   Download land use/land cover data from NLCD (2016) database within
   a given geometry in epsg:4326.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry or bounding box (west, south, east, north) for extracting the data.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to ``L48``. Valid values are L48 (for CONUS), HI (for Hawaii),
                  AK (for Alaska), and PR (for Puerto Rico). Both lower and upper cases are acceptable.
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.

   :returns: :class:`xarray.DataArray` -- NLCD within a geometry


.. py:function:: ssebopeta_bygeom(geometry, dates, geo_crs = DEF_CRS)

   Get daily actual ET for a region from SSEBop database.

   .. rubric:: Notes

   Since there's still no web service available for subsetting SSEBop, the data first
   needs to be downloaded for the requested period then it is masked by the
   region of interest locally. Therefore, it's not as fast as other functions and
   the bottleneck could be the download speed.

   :Parameters: * **geometry** (:class:`shapely.geometry.Polygon` or :class:`tuple`) -- The geometry for downloading clipping the data. For a tuple bbox,
                  the order should be (west, south, east, north).
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.

   :returns: :class:`xarray.DataArray` -- Daily actual ET within a geometry in mm/day at 1 km resolution


.. py:function:: ssebopeta_byloc(coords, dates)

   Daily actual ET for a location from SSEBop database in mm/day.

   :Parameters: * **coords** (:class:`tuple`) -- Longitude and latitude of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].

   :returns: :class:`pandas.DataFrame` -- Daily actual ET for a location


