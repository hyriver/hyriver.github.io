:py:mod:`pynhd.core`
====================

.. py:module:: pynhd.core

.. autoapi-nested-parse::

   Base classes for PyNHD functions.



Module Contents
---------------

.. py:class:: AGRBase

   Base class for accessing NHD(Plus) HR database through the National Map ArcGISRESTful.

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. To see a list of available layers instantiate the class
                  without passing any argument.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to EPSG:4326

   .. py:method:: bygeom(self, geom, geo_crs = DEF_CRS, sql_clause = '', distance = None, return_m = False)

      Get feature within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`Polygon` or :class:`tuple`) -- A geometry (Polygon) or bounding box (tuple of length 4).
                   * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                   * **sql_clause** (:class:`str`, *optional*) -- A valid SQL 92 WHERE clause, defaults to an empty string.
                   * **distance** (:class:`int`, *optional*) -- The buffer distance for the input geometries in meters, default to None.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: byids(self, field, fids, return_m = False)

      Get features based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **fids** (:class:`str` or :class:`list`) -- A list of target field ID(s).
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: bysql(self, sql_clause, return_m = False)

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__

      :Parameters: * **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. py:method:: connect_to(self, service, service_list, auto_switch)

      Connect to a web service.

      :Parameters: * **service** (:class:`str`) -- Name of the preferred web service to connect to from the list provided in service_list.
                   * **service_list** (:class:`dict`) -- A dict where keys are names of the web services and values are their URLs.
                   * **auto_switch** (:class:`bool`, *optional*) -- Automatically switch to other services' URL if the first one doesn't work, default to False.


   .. py:method:: get_validlayers(url)
      :staticmethod:

      Get valid layer for a ArcGISREST service.


   .. py:method:: service(self)
      :property:

      Connect to a RESTFul service.



.. py:class:: ScienceBase(save_dir = None)

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: **save_dir** (:class:`str`) -- Directory to save the staged data frame containing metadata for the database,
                defaults to system's temp directory. The metadata dataframe is saved as a feather
                file, nhdplus_attrs.feather, in save_dir that can be loaded with Pandas.

   .. py:method:: get_children(item)
      :staticmethod:

      Get children items of an item.


   .. py:method:: get_files(item)
      :staticmethod:

      Get all the available zip files in an item.


   .. py:method:: stage_data(self)

      Stage the NHDPlus Attributes database and save to nhdplus_attrs.feather.


