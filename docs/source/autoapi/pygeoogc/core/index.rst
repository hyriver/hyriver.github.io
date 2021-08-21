:mod:`pygeoogc.core`
====================

.. py:module:: pygeoogc.core

.. autoapi-nested-parse::

   Base classes and function for REST, WMS, and WMF services.



Module Contents
---------------

.. py:class:: ArcGISRESTfulBase(base_url: str, layer: Optional[int] = None, outformat: str = 'geojson', outfields: Union[List[str], str] = '*', crs: Union[str, pyproj.CRS] = DEF_CRS, max_workers: int = 1)

   Access to an ArcGIS REST service.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an argument.
                * **layer** (:class:`int`, *optional*) -- Target layer number, defaults to None. If None layer number must be included as after
                  the last ``/`` in ``base_url``.
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``geojson``.
                  It defaults to ``esriSpatialRelIntersects``.
                * **outfields** (:class:`str` or :class:`list`) -- The output fields to be requested. Setting ``*`` as outfields requests
                  all the available fields which is the default behaviour.
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the output data, defaults to EPSG:4326
                * **max_workers** (:class:`int`, *optional*) -- Max number of simultaneous requests, default to 2. Note
                  that some services might face issues when several requests are sent
                  simultaneously and will return the requests partially. It's recommended
                  to avoid using too many workers unless you are certain the web service can handle it.

   .. method:: get_features(self, return_m: bool = False) -> List[Dict[str, Any]]

      Get features based on the feature IDs.

      :Parameters: **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`dict` -- (Geo)json response from the web service.


   .. method:: initialize_service(self) -> None

      Initialize the RESTFul service.


   .. method:: partition_oids(self, oids: Union[List[int], int, None]) -> List[Tuple[str, ...]]

      Partition feature IDs based on service's max record number.



.. py:class:: RESTValidator



   Validate ArcGISRESTful inputs.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an argument.
                * **layer** (:class:`int`, *optional*) -- Target layer number, defaults to None. If None layer number must be included as after
                  the last ``/`` in ``base_url``.
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``geojson``.
                  It defaults to ``esriSpatialRelIntersects``.
                * **outfields** (:class:`str` or :class:`list`) -- The output fields to be requested. Setting ``*`` as outfields requests
                  all the available fields which is the default behaviour.
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the output data, defaults to EPSG:4326
                * **max_workers** (:class:`int`, *optional*) -- Max number of simultaneous requests, default to 2. Note
                  that some services might face issues when several requests are sent
                  simultaneously and will return the requests partially. It's recommended
                  to avoid using too many workers unless you are certain the web service can handle it.


.. py:class:: WFSBase

   Base class for WFS service.

   :Parameters: * **url** (:class:`str`) -- The base url for the WFS service, for examples:
                  https://hazards.fema.gov/nfhl/services/public/NFHL/MapServer/WFSServer
                * **layer** (:class:`str`) -- The layer from the service to be downloaded, defaults to None which throws
                  an error and includes all the available layers offered by the service.
                * **outformat** (:class:`str`) --

                  The data format to request for data from the service, defaults to None which
                   throws an error and includes all the available format offered by the service.
                * **version** (:class:`str`, *optional*) -- The WFS service version which should be either 1.0.0, 1.1.0, or 2.0.0.
                  Defaults to 2.0.0.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.
                * **read_method** (:class:`str`, *optional*) -- Method for reading the retrieved data, defaults to ``json``. Valid options are
                  ``json``, ``binary``, and ``text``.
                * **max_nrecords** (:class:`int`, *optional*) -- The maximum number of records in a single request to be retrieved from the service,
                  defaults to 1000. If the number of records requested is greater than this value,
                  it will be split into multiple requests.

   .. method:: get_validnames(self) -> List[str]

      Get valid column names for a layer.


   .. method:: validate_wfs(self) -> None

      Validate input arguments with the WFS service.



.. py:class:: WMSBase

   Base class for accessing a WMS service.

   :Parameters: * **url** (:class:`str`) -- The base url for the WMS service e.g., https://www.mrlc.gov/geoserver/mrlc_download/wms
                * **layers** (:class:`str` or :class:`list`) -- A layer or a list of layers from the service to be downloaded. You can pass an empty
                  string to get a list of available layers.
                * **outformat** (:class:`str`) -- The data format to request for data from the service. You can pass an empty
                  string to get a list of available output formats.
                * **version** (:class:`str`, *optional*) -- The WMS service version which should be either 1.1.1 or 1.3.0, defaults to 1.3.0.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.

   .. method:: get_validlayers(self) -> Dict[str, str]

      Get the layers supported by the WMS service.


   .. method:: validate_wms(self) -> None

      Validate input arguments with the WMS service.



