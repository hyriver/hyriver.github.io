pynhd.core
==========

.. py:module:: pynhd.core

.. autoapi-nested-parse::

   Base classes for PyNHD functions.





Module Contents
---------------

.. py:class:: AGRBase(base_url, layer = None, outfields = '*', crs = 4326, outformat = 'json')

   Base class for getting geospatial data from a ArcGISRESTful service.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an argument.
                * **layer** (:class:`str`, *optional*) -- A valid service layer. To see a list of available layers instantiate the class
                  without passing any argument.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- Target spatial reference, default to ``EPSG:4326``
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``json``.


   .. py:method:: bygeom(geom, geo_crs = 4326, sql_clause = '', distance = None, return_m = False, return_geom = True)

      Get feature within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`Polygon` or :class:`tuple`) -- A geometry (Polygon) or bounding box (tuple of length 4).
                   * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                   * **sql_clause** (:class:`str`, *optional*) -- A valid SQL 92 WHERE clause, defaults to an empty string.
                   * **distance** (:class:`int`, *optional*) -- The buffer distance for the input geometries in meters, default to None.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.



   .. py:method:: byids(field, fids, return_m = False, return_geom = True)

      Get features based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **fids** (:class:`str` or :class:`list`) -- A list of target field ID(s).
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.



   .. py:method:: bysql(sql_clause, return_m = False, return_geom = True)

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__

      :Parameters: * **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.
                   * **return_m** (:class:`bool`) -- Whether to activate the measure in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.



   .. py:method:: get_validlayers(url)
      :staticmethod:


      Get a list of valid layers.

      :Parameters: **url** (:class:`str`) -- The URL of the ArcGIS REST service.

      :returns: :class:`dict` -- A dictionary of valid layers.



   .. py:property:: service_info
      :type: ServiceInfo


      Get the service information.


.. py:class:: GeoConnex(item = None, dev = False, max_nfeatures = 10000)

   Access to the GeoConnex API.

   .. rubric:: Notes

   The ``geometry`` field of the query can be a Polygon, MultiPolygon,
   or tuple/list of length 4 (bbox) in ``EPSG:4326`` CRS. They should
   be within the extent of the GeoConnex endpoint.

   :Parameters: * **The item (service endpoint) to query. Valid endpoints are** --

                  - ``hu02`` for Two-digit Hydrologic Regions
                  - ``hu04`` for Four-digit Hydrologic Subregion
                  - ``hu06`` for Six-digit Hydrologic Basins
                  - ``hu08`` for Eight-digit Hydrologic Subbasins
                  - ``hu10`` for Ten-digit Watersheds
                  - ``nat_aq`` for National Aquifers of the United States from
                      USGS National Water Information System National Aquifer code list.
                  - ``principal_aq`` for Principal Aquifers of the United States from
                      2003 USGS data release
                  - ``sec_hydrg_reg`` for Secondary Hydrogeologic Regions of the
                      Conterminous United States from 2018 USGS data release
                  - ``gages`` for US Reference Stream Gauge Monitoring Locations
                  - ``mainstems`` for US Reference Mainstem Rivers
                  - ``states`` for U.S. States
                  - ``counties`` for U.S. Counties
                  - ``aiannh`` for Native American Lands
                  - ``cbsa`` for U.S. Metropolitan and Micropolitan Statistical Areas
                  - ``ua10`` for Urbanized Areas and Urban Clusters (2010 Census)
                  - ``places`` for U.S. legally incororated and Census designated places
                  - ``pws`` for U.S. Public Water Systems
                  - ``dams`` for US Reference Dams
                * **dev** (:class:`bool`, *optional*) -- Whether to use the development endpoint, defaults to ``False``.
                * **max_nfeatures** (:class:`int`, *optional*) -- The maximum number of features to request from the service,
                  defaults to 10000.


   .. py:method:: bybox(bbox, skip_geometry = False)

      Query the GeoConnex endpoint by bounding box.

      :Parameters: * **bbox** (:class:`tuple`) -- A bounding box in the form of ``(xmin, ymin, xmax, ymax)``,
                     in ``EPSG:4326`` CRS, i.e., decimal degrees.
                   * **skip_geometry** (:class:`bool`, *optional*) -- If ``True``, no geometry will not be returned, by default ``False``.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame``.



   .. py:method:: bycql(cql_dict: dict[str, Any], skip_geometry: Literal[False] = False) -> geopandas.GeoDataFrame
                  bycql(cql_dict: dict[str, Any], skip_geometry: Literal[True]) -> pandas.DataFrame

      Query the GeoConnex endpoint.

      .. rubric:: Notes

      GeoConnex only supports Basinc CQL2 queries. For more information
      and examples visit this
      `link <https://docs.ogc.org/is/21-065r2/21-065r2.html#cql2-core>`__.
      Use this for non-spatial queries, since there's a dedicated method
      for spatial queries, :meth:`.bygeometry`.

      :Parameters: * **cql_dict** (:class:`dict`) -- A valid CQL dictionary (non-spatial queries).
                   * **skip_geometry** (:class:`bool`, *optional*) -- If ``True``, no geometry will not be returned, by default ``False``.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame``.



   .. py:method:: byfilter(filter_str, skip_geometry = False)

      Query the GeoConnex endpoint.

      .. rubric:: Notes

      GeoConnex only supports simple CQL queries. For more information
      and examples visit https://portal.ogc.org/files/96288

      :Parameters: * **filter_str** (:class:`dict`) -- A valid filter string. The filter string shouldn't be long
                     since a GET request is used.
                   * **skip_geometry** (:class:`bool`, *optional*) -- If ``True``, no geometry will not be returned, by default ``False``.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame``.



   .. py:method:: bygeometry(geometry1: GeoType, geometry2: GeoType | None = ..., predicate: str = ..., crs: CRSType = ..., skip_geometry: Literal[False] = False) -> geopandas.GeoDataFrame
                  bygeometry(geometry1: GeoType, geometry2: GeoType | None = ..., predicate: str = ..., crs: CRSType = ..., skip_geometry: Literal[True] = True) -> pandas.DataFrame

      Query the GeoConnex endpoint by geometry.

      :Parameters: * **geometry1** (:class:`Polygon` or :class:`tuple` of :class:`float`) -- The first geometry or bounding boxes to query. A bounding box is
                     a tuple of length 4 in the form of ``(xmin, ymin, xmax, ymax)``.
                     For example, an spatial query for a single geometry would be
                     ``INTERSECTS(geom, geometry1)``.
                   * **geometry2** (:class:`Polygon` or :class:`tuple` of :class:`float`, *optional*) -- The second geometry or bounding boxes to query. A bounding box is
                     a tuple of length 4 in the form of ``(xmin, ymin, xmax, ymax)``.
                     Default is ``None``. For example, an spatial query for a two
                     geometries would be ``CROSSES(geometry1, geometry2)``.
                   * **predicate** (:class:`str`, *optional*) -- The predicate to use, by default ``intersects``. Supported
                     predicates are ``intersects``, ``equals``, ``disjoint``, ``touches``,
                     ``within``, ``overlaps``, ``crosses`` and ``contains``.
                   * **crs** (:class:`int` or :class:`str` or :class:`pyproj.CRS`, *optional*) -- The CRS of the polygon, by default ``EPSG:4326``. If the input
                     is a ``geopandas.GeoDataFrame`` or ``geopandas.GeoSeries``,
                     this argument will be ignored.
                   * **skip_geometry** (:class:`bool`, *optional*) -- If ``True``, no geometry will not be returned.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame``.



   .. py:method:: byid(feature_name: str, feature_ids: list[str] | str, skip_geometry: Literal[False] = False) -> geopandas.GeoDataFrame
                  byid(feature_name: str, feature_ids: list[str] | str, skip_geometry: Literal[True]) -> pandas.DataFrame

      Query the GeoConnex endpoint.

      :Parameters: * **feature_name** (:class:`str`) -- The name of the feature to query.
                   * **feature_ids** (:class:`list` or :class:`str`) -- The IDs of the feature to query.
                   * **skip_geometry** (:class:`bool`, *optional*) -- If ``True``, no geometry will not be returned, by default ``False``.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame`` or a ``pandas.DataFrame``.



   .. py:method:: byitem(item_id)

      Query the GeoConnex endpoint by an item ID.

      :Parameters: **item_id** (:class:`str`) -- The ID of the item to query. Note that this GeoConnex's item ID which
                   is not necessarily the same as the provider's item ID. For example,
                   for querying gages, the item ID is not the same as the USGS gage ID
                   but for querying HUC02, the item ID is the same as the HUC02 ID.

      :returns: :class:`geopandas.GeoDataFrame` -- The query result as a ``geopandas.GeoDataFrame``.



   .. py:property:: dev
      :type: bool


      Return the name of the endpoint.


   .. py:property:: item
      :type: str | None


      Return the name of the endpoint.


.. py:class:: ScienceBase

   Access and explore items on USGS's ScienceBase.


   .. py:method:: get_children(item)
      :staticmethod:


      Get children items of an item.



   .. py:method:: get_file_urls(item)
      :staticmethod:


      Get download and meta URLs of all the available files for an item.



