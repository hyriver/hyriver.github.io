:py:mod:`pygeoogc.pygeoogc`
===========================

.. py:module:: pygeoogc.pygeoogc

.. autoapi-nested-parse::

   Base classes and function for REST, WMS, and WMF services.



Module Contents
---------------

.. py:class:: ArcGISRESTful(base_url, layer = None, outformat = 'geojson', outfields = '*', crs = 4326, max_workers = 1, verbose = False, disable_retry = False)

   Access to an ArcGIS REST service.

   .. rubric:: Notes

   By default, all retrieval methods retry to get the missing feature IDs,
   if there are any. You can disable this behavior by setting ``disable_retry``
   to ``True``. If there are any missing feature IDs after the retry,
   they are saved to a text file, ipath of which can be accessed by
   ``self.client.failed_path``.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an argument.
                * **layer** (:class:`int`, *optional*) -- Target layer number, defaults to None. If None layer number must be included as after
                  the last ``/`` in ``base_url``.
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``geojson``.
                * **outfields** (:class:`str` or :class:`list`) -- The output fields to be requested. Setting ``*`` as outfields requests
                  all the available fields which is the default behaviour.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the output data, defaults to ``epsg:4326``.
                * **max_workers** (:class:`int`, *optional*) -- Number of simultaneous download, default to 1, i.e., no threading. Note
                  that some services might face issues when several requests are sent
                  simultaneously and will return the requests partially. It's recommended
                  to avoid using too many workers unless you are certain the web service
                  can handle it.
                * **verbose** (:class:`bool`, *optional*) -- If True, prints information about the requests and responses,
                  defaults to False.
                * **disable_retry** (:class:`bool`, *optional*) -- If ``True`` in case there are any failed queries, no retrying attempts
                  is done and object IDs of the failed requests is saved to a text file
                  which its ipath can be accessed via ``self.client.failed_path``.

   .. py:method:: get_features(featureids, return_m = False, return_geom = True)

      Get features based on the feature IDs.

      :Parameters: * **featureids** (:class:`list`) -- List of feature IDs.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request,
                     defaults to ``False``.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`dict` -- (Geo)json response from the web service.


   .. py:method:: oids_byfield(field, ids)

      Get Object IDs based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **ids** (:class:`str` or :class:`list`) -- A list of target ID(s).

      :returns: :class:`list` of :class:`tuples` -- A list of feature IDs partitioned by ``self.max_nrecords``.


   .. py:method:: oids_bygeom(geom, geo_crs = 4326, spatial_relation = 'esriSpatialRelIntersects', sql_clause = None, distance = None)

      Get feature IDs within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`LineString`, :class:`Polygon`, :class:`Point`, :class:`MultiPoint`, :class:`tuple`, or :class:`list` of :class:`tuples`) -- A geometry (LineString, Polygon, Point, MultiPoint), tuple of length two
                     (``(x, y)``), a list of tuples of length 2 (``[(x, y), ...]``), or bounding box
                     (tuple of length 4 (``(xmin, ymin, xmax, ymax)``)).
                   * **geo_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the input geometry, defaults to ``epsg:4326``.
                   * **spatial_relation** (:class:`str`, *optional*) -- The spatial relationship to be applied on the input geometry
                     while performing the query. If not correct a list of available options is shown.
                     It defaults to ``esriSpatialRelIntersects``. Valid predicates are:

                     * ``esriSpatialRelIntersects``
                     * ``esriSpatialRelContains``
                     * ``esriSpatialRelCrosses``
                     * ``esriSpatialRelEnvelopeIntersects``
                     * ``esriSpatialRelIndexIntersects``
                     * ``esriSpatialRelOverlaps``
                     * ``esriSpatialRelTouches``
                     * ``esriSpatialRelWithin``
                     * ``esriSpatialRelRelation``
                   * **sql_clause** (:class:`str`, *optional*) -- Valid SQL 92 WHERE clause, default to None.
                   * **distance** (:class:`int`, *optional*) -- Buffer distance in meters for the input geometries, default to None.

      :returns: :class:`list` of :class:`tuples` -- A list of feature IDs partitioned by ``self.max_nrecords``.


   .. py:method:: oids_bysql(sql_clause)

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__.

      :Parameters: **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.

      :returns: :class:`list` of :class:`tuples` -- A list of feature IDs partitioned by ``self.max_nrecords``.


   .. py:method:: partition_oids(oids)

      Partition feature IDs based on ``self.max_nrecords``.

      :Parameters: **oids** (:class:`list` of :class:`int` or :class:`int`) -- A list of feature ID(s).

      :returns: :class:`list` of :class:`tuples` -- A list of feature IDs partitioned by ``self.max_nrecords``.



.. py:class:: HttpURLs



   URLs of the supported HTTP services.


.. py:class:: RESTfulURLs



   URLs of the supported RESTful services.


.. py:class:: ServiceURL



   URLs of the supported services.


.. py:class:: WFS(url, layer = None, outformat = None, version = '2.0.0', crs = 4326, read_method = 'json', max_nrecords = 1000, validation = True)



   Data from any WFS service within a geometry or by featureid.

   :Parameters: * **url** (:class:`str`) -- The base url for the WFS service, for examples:
                  https://hazards.fema.gov/nfhl/services/public/NFHL/MapServer/WFSServer
                * **layer** (:class:`str`) -- The layer from the service to be downloaded, defaults to None which throws
                  an error and includes all the available layers offered by the service.
                * **outformat** (:class:`str`) --

                  The data format to request for data from the service, defaults to None which
                   throws an error and includes all the available format offered by the service.
                * **version** (:class:`str`, *optional*) -- The WFS service version which should be either 1.0.0, 1.1.0, or 2.0.0.
                  Defaults to 2.0.0.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **read_method** (:class:`str`, *optional*) -- Method for reading the retrieved data, defaults to ``json``. Valid options are
                  ``json``, ``binary``, and ``text``.
                * **max_nrecords** (:class:`int`, *optional*) -- The maximum number of records in a single request to be retrieved from the service,
                  defaults to 1000. If the number of records requested is greater than this value,
                  it will be split into multiple requests.
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WFS service, defaults to True. Set this
                  to False if you are sure all the WFS settings such as layer and crs are correct
                  to avoid sending extra requests.

   .. py:method:: getfeature_bybox(bbox, box_crs = 4326, always_xy = False)

      Get data from a WFS service within a bounding box.

      :Parameters: * **bbox** (:class:`tuple`) -- A bounding box for getting the data: [west, south, east, north]
                   * **box_crs** (:class:`str`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system of the input bbox, defaults to
                     ``epsg:4326``.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.

      :returns: :class:`str` or :class:`bytes` or :class:`dict` -- WFS query response within a bounding box.


   .. py:method:: getfeature_byfilter(cql_filter, method = 'GET')

      Get features based on a valid CQL filter.

      .. rubric:: Notes

      The validity of the input CQL expression is user's responsibility since
      the function does not perform any checks and just sends a request using
      the input filter.

      :Parameters: * **cql_filter** (:class:`str`) -- A valid CQL filter expression.
                   * **method** (:class:`str`) -- The request method, could be GET or POST (for long filters).

      :returns: :class:`str` or :class:`bytes` or :class:`dict` -- WFS query response


   .. py:method:: getfeature_bygeom(geometry, geo_crs = 4326, always_xy = False, predicate = 'INTERSECTS')

      Get features based on a geometry.

      :Parameters: * **geometry** (:class:`shapely.geometry`) -- The input geometry
                   * **geo_crs** (:class:`str`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input geometry, default to ``epsg:4326``.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.
                   * **predicate** (:class:`str`, *optional*) -- The geometric predicate to use for requesting the data, defaults to ``INTERSECTS``.
                     Valid predicates are:

                     * ``EQUALS``
                     * ``DISJOINT``
                     * ``INTERSECTS``
                     * ``TOUCHES``
                     * ``CROSSES``
                     * ``WITHIN``
                     * ``CONTAINS``
                     * ``OVERLAPS``
                     * ``RELATE``
                     * ``BEYOND``

      :returns: :class:`str` or :class:`bytes` or :class:`dict` -- WFS query response based on the given geometry.


   .. py:method:: getfeature_byid(featurename, featureids)

      Get features based on feature IDs.

      :Parameters: * **featurename** (:class:`str`) -- The name of the column for searching for feature IDs.
                   * **featureids** (:class:`str` or :class:`list`) -- The feature ID(s).

      :returns: :class:`str` or :class:`bytes` or :class:`dict` -- WMS query response.



.. py:class:: WFSURLs



   URLs of the supported WFS services.


.. py:class:: WMS(url, layers, outformat, version = '1.3.0', crs = 4326, validation = True, ssl = None)

   Get data from a WMS service within a geometry or bounding box.

   :Parameters: * **url** (:class:`str`) -- The base url for the WMS service e.g., https://www.mrlc.gov/geoserver/mrlc_download/wms
                * **layers** (:class:`str` or :class:`list`) -- A layer or a list of layers from the service to be downloaded. You can pass an empty
                  string to get a list of available layers.
                * **outformat** (:class:`str`) -- The data format to request for data from the service. You can pass an empty
                  string to get a list of available output formats.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **version** (:class:`str`, *optional*) -- The WMS service version which should be either 1.1.1 or 1.3.0, defaults to 1.3.0.
                * **validation** (:class:`bool`, *optional*) -- Validate the input arguments from the WMS service, defaults to True. Set this
                  to False if you are sure all the WMS settings such as layer and crs are correct
                  to avoid sending extra requests.
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to False to disable
                  SSL certification verification.

   .. py:method:: get_validlayers()

      Get the layers supported by the WMS service.


   .. py:method:: getmap_bybox(bbox, resolution, box_crs = 4326, always_xy = False, max_px = 8000000, kwargs = None)

      Get data from a WMS service within a geometry or bounding box.

      :Parameters: * **bbox** (:class:`tuple`) -- A bounding box for getting the data.
                   * **resolution** (:class:`float`) -- The output resolution in meters. The width and height of output are computed in pixel
                     based on the geometry bounds and the given resolution.
                   * **box_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system of the input bbox, defaults to
                     ``epsg:4326``.
                   * **always_xy** (:class:`bool`, *optional*) -- Whether to always use xy axis order, defaults to False. Some services change the axis
                     order from xy to yx, following the latest WFS version specifications but some don't.
                     If the returned value does not have any geometry, it indicates that most probably the
                     axis order does not match. You can set this to True in that case.
                   * **max_px** (:class:`int`, :class:`opitonal`) -- The maximum allowable number of pixels (width x height) for a WMS requests,
                     defaults to 8 million based on some trial-and-error.
                   * **kwargs** (:class:`dict`, *optional*) -- Optional additional keywords passed as payload, defaults to None.
                     For example, ``{"styles": "default"}``.

      :returns: :class:`dict` -- A dict where the keys are the layer name and values are the returned response
                from the WMS service as bytes.



.. py:class:: WMSURLs



   URLs of the supported WMS services.


