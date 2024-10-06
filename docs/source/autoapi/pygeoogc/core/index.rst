pygeoogc.core
=============

.. py:module:: pygeoogc.core

.. autoapi-nested-parse::

   Base classes and function for REST, WMS, and WMF services.





Module Contents
---------------

.. py:class:: ArcGISRESTfulBase(base_url, layer = None, outformat = 'geojson', outfields = '*', crs = 4326, max_workers = 1, verbose = False, disable_retry = False)

   Access to an ArcGIS REST service.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an
                  argument.
                * **layer** (:class:`int`, *optional*) -- Target layer number, defaults to None. If None layer number must be
                  included as after the last ``/`` in ``base_url``.
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``geojson``.
                  It defaults to ``esriSpatialRelIntersects``.
                * **outfields** (:class:`str` or :class:`list`) -- The output fields to be requested. Setting ``*`` as outfields requests
                  all the available fields which is the default setting.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the output data, defaults to ``epsg:4326``
                * **max_workers** (:class:`int`, *optional*) -- Max number of simultaneous requests, default to 2. Note
                  that some services might face issues when several requests are sent
                  simultaneously and will return the requests partially. It's recommended
                  to avoid using too many workers unless you are certain the web service
                  can handle it.
                * **verbose** (:class:`bool`, *optional*) -- If True, prints information about the requests and responses,
                  defaults to False.
                * **disable_retry** (:class:`bool`, *optional*) -- If ``True`` in case there are any failed queries, no retrying attempts
                  is done and object IDs of the failed requests is saved to a text file
                  which its ipath can be accessed via ``self.failed_path``.


   .. py:method:: get_features(featureids, return_m = False, return_geom = True)

      Get features based on the feature IDs.

      :Parameters: * **featureids** (:class:`list`) -- List of feature IDs.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request,
                     defaults to ``False``.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`dict` -- (Geo)json response from the web service.



   .. py:method:: get_response(url, payloads, method = 'GET')

      Send payload and get the response.



   .. py:method:: initialize_service()

      Initialize the RESTFul service.



   .. py:method:: partition_oids(oids)

      Partition feature IDs based on ``self.max_nrecords``.



   .. py:method:: retry_failed_requests()

      Retry failed requests.



.. py:class:: WFSBase(url, layer = None, outformat = None, version = '2.0.0', crs = 4326, read_method = 'json', max_nrecords = 1000, validation = True)

   Base class for WFS service.

   :Parameters: * **url** (:class:`str`) -- The base url for the WFS service, for examples:
                  https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/WFSServer
                * **layer** (:class:`str`) -- The layer from the service to be downloaded, defaults to None which throws
                  an error and includes all the available layers offered by the service.
                * **outformat** (:class:`str`) --

                  The data format to request for data from the service, defaults to None which
                   throws an error and includes all the available format offered by the service.
                * **version** (:class:`str`, *optional*) -- The WFS service version which should be either ``1.0.0``, ``1.1.0``, or
                  ``2.0.0``. Defaults to ``2.0.0``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **read_method** (:class:`str`, *optional*) -- Method for reading the retrieved data, defaults to ``json``. Valid options are
                  ``json``, ``binary``, and ``text``.
                * **max_nrecords** (:class:`int`, *optional*) -- The maximum number of records in a single request to be retrieved from the service,
                  defaults to 1000. If the number of requested records is greater than this value,
                  the query will be split into multiple requests.
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WFS service, defaults to True. Set this
                  to False if you are sure all the WFS settings such as layer and crs are correct
                  to avoid sending extra requests.


   .. py:method:: get_service_options()

      Validate input arguments with the WFS service.



   .. py:method:: sort_params(sort_attr, nfeatures, start_index)

      Get sort parameters for a WFS request.



   .. py:method:: validate_wfs()

      Validate input arguments with the WFS service.



.. py:class:: WMSBase(url, layers = '', outformat = '', version = '1.3.0', crs = 4326, validation = True)

   Base class for accessing a WMS service.

   :Parameters: * **url** (:class:`str`) -- The base url for the WMS service e.g., https://www.mrlc.gov/geoserver/mrlc_download/wms
                * **layers** (:class:`str` or :class:`list`, *optional*) -- A layer or a list of layers from the service to be downloaded. You can pass an empty
                  string to get a list of available layers.
                * **outformat** (:class:`str`, *optional*) -- The data format to request for data from the service. You can pass an empty
                  string to get a list of available output formats.
                * **version** (:class:`str`, *optional*) -- The WMS service version which should be either 1.1.1 or 1.3.0, defaults to 1.3.0.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WMS service, defaults to True. Set this
                  to False if you are sure all the WMS settings such as layer and crs are correct
                  to avoid sending extra requests.


   .. py:method:: get_service_options()

      Validate input arguments with the WMS service.



   .. py:method:: get_validlayers()

      Get the layers supported by the WMS service.



   .. py:method:: validate_wms()

      Validate input arguments with the WMS service.



