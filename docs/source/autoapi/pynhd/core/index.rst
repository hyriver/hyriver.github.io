:py:mod:`pynhd.core`
====================

.. py:module:: pynhd.core

.. autoapi-nested-parse::

   Base classes for PyNHD functions.



Module Contents
---------------

.. py:class:: AGRBase(base_url, layer = None, outfields = '*', crs = DEF_CRS, outformat = 'json')

   Base class for getting geospatial data from a ArcGISRESTful service.

   :Parameters: * **base_url** (:class:`str`, *optional*) -- The ArcGIS RESTful service url. The URL must either include a layer number
                  after the last ``/`` in the url or the target layer must be passed as an argument.
                * **layer** (:class:`str`, *optional*) -- A valid service layer. To see a list of available layers instantiate the class
                  without passing any argument.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to EPSG:4326
                * **outformat** (:class:`str`, *optional*) -- One of the output formats offered by the selected layer. If not correct
                  a list of available formats is shown, defaults to ``json``.

   .. py:method:: bygeom(self, geom, geo_crs = DEF_CRS, sql_clause = '', distance = None, return_m = False, return_geom = True)

      Get feature within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`Polygon` or :class:`tuple`) -- A geometry (Polygon) or bounding box (tuple of length 4).
                   * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                   * **sql_clause** (:class:`str`, *optional*) -- A valid SQL 92 WHERE clause, defaults to an empty string.
                   * **distance** (:class:`int`, *optional*) -- The buffer distance for the input geometries in meters, default to None.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: byids(self, field, fids, return_m = False, return_geom = True)

      Get features based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **fids** (:class:`str` or :class:`list`) -- A list of target field ID(s).
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: bysql(self, sql_clause, return_m = False, return_geom = True)

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__

      :Parameters: * **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.
                   * **return_m** (:class:`bool`) -- Whether to activate the measure in the request, defaults to False.
                   * **return_geom** (:class:`bool`, *optional*) -- Whether to return the geometry of the feature, defaults to ``True``.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: get_validlayers(self, url)

      Get a list of valid layers.

      :Parameters: **url** (:class:`str`) -- The URL of the ArcGIS REST service.

      :returns: :class:`dict` -- A dictionary of valid layers.


   .. py:method:: service_info(self)
      :property:

      Get the service information.



.. py:class:: GeoConnex(item = None)

   Access to the GeoConnex API.

   .. rubric:: Notes

   The ``geometry`` field of the query can be a Polygon, MultiPolygon,
   or tuple/list of length 4 (bbox) in ``EPSG:4326`` CRS. They should
   be within the extent of the GeoConnex endpoint.

   :Parameters: **item** (:class:`str`, *optional*) -- The target endpoint to query, defaults to ``None``.

   .. py:method:: item(self)
      :property:

      Return the name of the endpoint.


   .. py:method:: query(self, kwds, skip_geometry = False)

      Query the GeoConnex endpoint.



.. py:class:: ScienceBase

   Access and explore files on ScienceBase.

   .. py:method:: get_children(item)
      :staticmethod:

      Get children items of an item.


   .. py:method:: get_file_urls(item)
      :staticmethod:

      Get download and meta URLs of all the available files for an item.



.. py:function:: stage_nhdplus_attrs(parquet_path = None)

   Stage the NHDPlus Attributes database and save to nhdplus_attrs.parquet.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: **parquet_path** (:class:`str` or :class:`~~pathlib.Path`) -- Path to a file with ``.parquet`` extension for saving the processed to disk for
                later use.

   :returns: :class:`pandas.DataFrame` -- The staged data as a DataFrame.


