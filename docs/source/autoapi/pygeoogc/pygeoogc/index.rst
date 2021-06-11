:mod:`pygeoogc.pygeoogc`
========================

.. py:module:: pygeoogc.pygeoogc

.. autoapi-nested-parse::

   Base classes and function for REST, WMS, and WMF services.



Module Contents
---------------

.. py:class:: ArcGISRESTful



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
                  simultaneously and will return the requests partially. It's recommended
                  to avoid performing threading unless you are certain the web service can handle it.

   .. method:: get_features(self, return_m: bool = False) -> List[Dict[str, Any]]

      Get features based on the feature IDs.

      :Parameters: **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`dict` -- (Geo)json response from the web service.


   .. method:: oids_byfield(self, field: str, ids: Union[str, List[str]]) -> None

      Get Object IDs based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **ids** (:class:`str` or :class:`list`) -- A list of target ID(s).


   .. method:: oids_bygeom(self, geom: Union[LineString, Polygon, Point, MultiPoint, Tuple[float, float], List[Tuple[float, float]], Tuple[float, float, float, float]], geo_crs: str = DEF_CRS, sql_clause: Optional[str] = None, distance: Optional[int] = None) -> None

      Get feature IDs within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`LineString`, :class:`Polygon`, :class:`Point`, :class:`MultiPoint`, :class:`tuple`, or :class:`list` of :class:`tuples`) --

                     A geometry (LineString, Polygon, Point, MultiPoint), tuple of length
                      2 (``(x, y)``), a list of tuples of length 2 (``[(x, y), ...]``), or bounding box
                      (tuple of length 4 (``(xmin, ymin, xmax, ymax)``)).
                   * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry, defaults to EPSG:4326.
                   * **sql_clause** (:class:`str`, *optional*) -- A valid SQL 92 WHERE clause, default to None.
                   * **distance** (:class:`int`, *optional*) -- The buffer distance for the input geometries in meters, default to None.


   .. method:: oids_bysql(self, sql_clause: str) -> None

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__

      :Parameters: **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.



.. py:class:: ServiceURL

   Base URLs of the supported services.

   .. method:: http(self) -> SimpleNamespace
      :property:

      Read HTTP URLs from the source yml file.


   .. method:: restful(self) -> SimpleNamespace
      :property:

      Read RESTful URLs from the source yml file.


   .. method:: wfs(self) -> SimpleNamespace
      :property:

      Read WFS URLs from the source yml file.


   .. method:: wms(self) -> SimpleNamespace
      :property:

      Read WMS URLs from the source yml file.



.. py:class:: WFS(url: str, layer: Optional[str] = None, outformat: Optional[str] = None, version: str = '2.0.0', crs: str = DEF_CRS, validation: bool = True)



   Data from any WFS service within a geometry or by featureid.

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
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WFS service, defaults to True. Set this
                  to False if you are sure all the WFS settings such as layer and crs are correct
                  to avoid sending extra requests.

   .. method:: getfeature_bybox(self, bbox: Tuple[float, float, float, float], box_crs: str = DEF_CRS, always_xy: bool = False) -> Response

      Get data from a WFS service within a bounding box.

      :Parameters: * **bbox** (:class:`tuple`) -- A bounding box for getting the data: [west, south, east, north]
                   * **box_crs** (:class:`str`, *optional*) -- The spatial reference system of the input bbox, defaults to
                     epsg:4326.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.

      :returns: :class:`Response` -- WFS query response within a bounding box.


   .. method:: getfeature_byfilter(self, cql_filter: str, method: str = 'GET') -> Response

      Get features based on a valid CQL filter.

      .. rubric:: Notes

      The validity of the input CQL expression is user's responsibility since
      the function does not perform any checks and just sends a request using
      the input filter.

      :Parameters: * **cql_filter** (:class:`str`) -- A valid CQL filter expression.
                   * **method** (:class:`str`) -- The request method, could be GET or POST (for long filters).

      :returns: :class:`Response` -- WFS query response


   .. method:: getfeature_bygeom(self, geometry: Union[Polygon, MultiPolygon], geo_crs: str = DEF_CRS, always_xy: bool = False, predicate: str = 'INTERSECTS') -> Response

      Get features based on a geometry.

      :Parameters: * **geometry** (:class:`shapely.geometry`) -- The input geometry
                   * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, default to epsg:4326.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.
                   * **predicate** (:class:`str`, *optional*) -- The geometric prediacte to use for requesting the data, defaults to
                     INTERSECTS. Valid predicates are:
                     EQUALS, DISJOINT, INTERSECTS, TOUCHES, CROSSES, WITHIN, CONTAINS,
                     OVERLAPS, RELATE, BEYOND

      :returns: :class:`Response` -- WFS query response based on the given geometry.


   .. method:: getfeature_byid(self, featurename: str, featureids: Union[List[str], str]) -> Response

      Get features based on feature IDs.

      :Parameters: * **featurename** (:class:`str`) -- The name of the column for searching for feature IDs
                   * **featureids** (:class:`str` or :class:`list`) -- The feature ID(s)

      :returns: :class:`Response` -- WMS query response



.. py:class:: WMS(url: str, layers: Union[str, List[str]], outformat: str, version: str = '1.3.0', crs: str = DEF_CRS, validation: bool = True)



   Get data from a WMS service within a geometry or bounding box.

   :Parameters: * **url** (:class:`str`) -- The base url for the WMS service e.g., https://www.mrlc.gov/geoserver/mrlc_download/wms
                * **layers** (:class:`str` or :class:`list`) -- A layer or a list of layers from the service to be downloaded. You can pass an empty
                  string to get a list of available layers.
                * **outformat** (:class:`str`) -- The data format to request for data from the service. You can pass an empty
                  string to get a list of available output formats.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.
                * **version** (:class:`str`, *optional*) -- The WMS service version which should be either 1.1.1 or 1.3.0, defaults to 1.3.0.
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WMS service, defaults to True. Set this
                  to False if you are sure all the WMS settings such as layer and crs are correct
                  to avoid sending extra requests.

   .. method:: getmap_bybox(self, bbox: Tuple[float, float, float, float], resolution: float, box_crs: str = DEF_CRS, always_xy: bool = False, max_px: int = 8000000) -> Dict[str, bytes]

      Get data from a WMS service within a geometry or bounding box.

      :Parameters: * **bbox** (:class:`tuple`) -- A bounding box for getting the data.
                   * **resolution** (:class:`float`) -- The output resolution in meters. The width and height of output are computed in pixel
                     based on the geometry bounds and the given resolution.
                   * **box_crs** (:class:`str`, *optional*) -- The spatial reference system of the input bbox, defaults to
                     epsg:4326.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.
                   * **max_px** (:class:`int`, :class:`opitonal`) -- The maximum allowable number of pixels (width x height) for a WMS requests,
                     defaults to 8 million based on some trial-and-error.

      :returns: :class:`dict` -- A dict where the keys are the layer name and values are the returned response
                from the WMS service as bytes. You can use ``utils.create_dataset`` function
                to convert the responses to ``xarray.Dataset``.



