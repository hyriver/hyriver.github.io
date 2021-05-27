:mod:`pygeoogc.core`
====================

.. py:module:: pygeoogc.core

.. autoapi-nested-parse::

   Base classes and function for REST, WMS, and WMF services.



Module Contents
---------------

.. py:class:: ArcGISRESTfulBase(base_url: str, outformat: str = 'geojson', outfields: Union[List[str], str] = '*', spatial_relation: str = 'esriSpatialRelIntersects', crs: str = DEF_CRS, n_threads: int = 1)

   Access to an ArcGIS REST service.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url.
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``geojson``.
                * **spatial_relation** (:class:`str`, *optional*) -- The spatial relationship to be applied on the input geometry
                  while performing the query. If not correct a list of available options is shown.
                  It defaults to ``esriSpatialRelIntersects``.
                * **outfields** (:class:`str` or :class:`list`) -- The output fields to be requested. Setting ``*`` as outfields requests
                  all the available fields which is the default behaviour.
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the output data, defaults to EPSG:4326
                * **n_threads** (:class:`int`, *optional*) -- Number of simultaneous download, default to 1 i.e., no threading. Note
                  that some services might face issues when several requests are sent
                  simultaniously and will return the requests partially. It's recommended
                  to avoid performing threading unless you are certain the web service can handle it.

   .. method:: featureids(self) -> List[Tuple[str, ...]]
      :property:

      Set feature ID(s).


   .. method:: get_validfields(self) -> Dict[str, str]

      Get all the valid service output fields.


   .. method:: get_validlayers(self) -> Dict[str, str]

      Get all the valid service layer.


   .. method:: layer(self) -> int
      :property:

      Set service layer.


   .. method:: max_nrecords(self) -> int
      :property:

      Set maximum number of features per request.


   .. method:: n_threads(self) -> int
      :property:

      Set number of threads.


   .. method:: outfields(self) -> List[str]
      :property:

      Set service output field(s).


   .. method:: outformat(self) -> str
      :property:

      Set service output format.


   .. method:: spatial_relation(self) -> str
      :property:

      Set spatial relationship of the input geometry with the source data.


   .. method:: test_url(self) -> None

      Test the generated url and get the required parameters from the service.



.. py:class:: WFSBase(url: str, layer: Optional[str] = None, outformat: Optional[str] = None, version: str = '2.0.0', crs: str = DEF_CRS)

   Base class for WFS service.

   :Parameters: * **url** (:class:`str`) -- The base url for the WFS service, for examples:
                  https://hazards.fema.gov/nfhl/services/public/NFHL/MapServer/WFSServer
                * **layer** (:class:`str`) -- The layer from the service to be downloaded, defaults to None which throws
                  an error and includes all the available layers offered by the service.
                * **outformat** (:class:`str`) --

                  The data format to request for data from the service, defaults to None which
                   throws an error and includes all the available format offered by the service.
                * **version** (:class:`str`, *optional*) -- The WFS service version which should be either 1.1.1, 1.3.0, or 2.0.0.
                  Defaults to 2.0.0.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.

   .. method:: get_validnames(self) -> List[str]

      Get valid column names for a layer.


   .. method:: validate_wfs(self) -> None

      Validate input arguments with the WFS service.



.. py:class:: WMSBase(url: str, layers: Union[str, List[str]], outformat: str, version: str = '1.3.0', crs: str = DEF_CRS)

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



