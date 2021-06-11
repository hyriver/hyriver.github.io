:mod:`pynhd.pynhd`
==================

.. py:module:: pynhd.pynhd

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:class:: AGRBase(layer: str, outfields: Union[str, List[str]] = '*', crs: str = DEF_CRS, service: Optional[ArcGISRESTful] = None)

   Base class for accessing NHD(Plus) HR database through the National Map ArcGISRESTful.

   :Parameters: * **layer** (:class:`str`) -- A valid service layer. For a list of available layers pass an empty string to
                  the class.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to EPSG:4326

   .. method:: bygeom(self, geom: Union[Polygon, List[Tuple[float, float]], Tuple[float, float, float, float]], geo_crs: str = DEF_CRS, sql_clause: str = '', distance: Optional[int] = None, return_m: bool = False) -> gpd.GeoDataFrame

      Get feature within a geometry that can be combined with a SQL where clause.

      :Parameters: * **geom** (:class:`Polygon` or :class:`tuple`) -- A geometry (Polygon) or bounding box (tuple of length 4).
                   * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                   * **sql_clause** (:class:`str`, *optional*) -- A valid SQL 92 WHERE clause, defaults to an empty string.
                   * **distance** (:class:`int`, *optional*) -- The buffer distance for the input geometries in meters, default to None.
                   * **return_m** (:class:`bool`, *optional*) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. method:: byids(self, field: str, fids: Union[str, List[str]], return_m: bool = False) -> gpd.GeoDataFrame

      Get features based on a list of field IDs.

      :Parameters: * **field** (:class:`str`) -- Name of the target field that IDs belong to.
                   * **fids** (:class:`str` or :class:`list`) -- A list of target field ID(s).
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. method:: bysql(self, sql_clause: str, return_m: bool = False) -> gpd.GeoDataFrame

      Get feature IDs using a valid SQL 92 WHERE clause.

      .. rubric:: Notes

      Not all web services support this type of query. For more details look
      `here <https://developers.arcgis.com/rest/services-reference/query-feature-service-.htm#ESRI_SECTION2_07DD2C5127674F6A814CE6C07D39AD46>`__

      :Parameters: * **sql_clause** (:class:`str`) -- A valid SQL 92 WHERE clause.
                   * **return_m** (:class:`bool`) -- Whether to activate the Return M (measure) in the request, defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features as a GeoDataFrame.


   .. method:: connect_to(self, service: str, service_list: Dict[str, str], auto_switch: bool) -> None

      Connect to a web service.

      :Parameters: * **service** (:class:`str`, *optional*) -- Name of the preferred web service to connect to from the list provided in service_list.
                   * **service_list** (:class:`dict`) -- A dict where keys are names of the web services and values are their URLs.
                   * **auto_switch** (:class:`bool`, *optional*) -- Automatically switch to other services' URL if the first one doesn't work, default to False.



.. py:class:: NHDPlusHR(layer: str, outfields: Union[str, List[str]] = '*', crs: str = DEF_CRS, service: str = 'hydro', auto_switch: bool = False)



   Access NHDPlus HR database through the National Map ArcGISRESTful.

   :Parameters: * **layer** (:class:`str`) -- A valid service layer. For a list of available layers pass an empty string to
                  the class.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to EPSG:4326
                * **service** (:class:`str`, *optional*) -- Name of the web service to use, defaults to hydro. Supported web services are:

                  * hydro: https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer
                  * edits: https://edits.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/NHDPlus_HR/MapServer
                * **auto_switch** (:class:`bool`, *optional*) -- Automatically switch to other services' URL if the first one doesn't work, default to False.


.. py:class:: NLDI

   Access the Hydro Network-Linked Data Index (NLDI) service.

   .. method:: comid_byloc(self, coords: Union[Tuple[float, float], List[Tuple[float, float]]], loc_crs: str = DEF_CRS) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[Tuple[float, float]]]]

      Get the closest ComID(s) based on coordinates.

      :Parameters: * **coords** (:class:`tuple` or :class:`list`) -- A tuple of length two (x, y) or a list of them.
                   * **loc_crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to EPSG:4326.

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed ComID(s) in EPSG:4326. If some coords don't return any ComID
                a list of missing coords are returned as well.


   .. method:: get_basins(self, station_ids: Union[str, List[str]]) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[str]]]

      Get basins for a list of station IDs.

      :Parameters: **station_ids** (:class:`str` or :class:`list`) -- USGS station ID(s).

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed basins in EPSG:4326. If some IDs don't return any features
                a list of missing ID(s) are returned as well.


   .. method:: get_validchars(self, char_type: str) -> pd.DataFrame

      Get all the available characteristics IDs for a given characteristics type.


   .. method:: getcharacteristic_byid(self, comids: Union[List[str], str], char_type: str, char_ids: Union[str, List[str]] = 'all', values_only: bool = True) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]

      Get characteristics using a list ComIDs.

      :Parameters: * **comids** (:class:`str` or :class:`list`) -- The ID of the feature.
                   * **char_type** (:class:`str`) -- Type of the characteristic. Valid values are ``local`` for
                     individual reach catchments, ``tot`` for network-accumulated values
                     using total cumulative drainage area and ``div`` for network-accumulated values
                     using divergence-routed.
                   * **char_ids** (:class:`str` or :class:`list`, *optional*) -- Name(s) of the target characteristics, default to all.
                   * **values_only** (:class:`bool`, *optional*) -- Whether to return only ``characteristic_value`` as a series, default to True.
                     If is set to False, ``percent_nodata`` is returned as well.

      :returns: :class:`pandas.DataFrame` or :class:`tuple` of :class:`pandas.DataFrame` -- Either only ``characteristic_value`` as a dataframe or
                or if ``values_only`` is Fale return ``percent_nodata`` as well.


   .. method:: getfeature_byid(self, fsource: str, fid: Union[str, List[str]]) -> Union[gpd.GeoDataFrame, Tuple[gpd.GeoDataFrame, List[str]]]

      Get feature(s) based ID(s).

      :Parameters: * **fsource** (:class:`str`) -- The name of feature(s) source. The valid sources are:
                     comid, huc12pp, nwissite, wade, wqp
                   * **fid** (:class:`str` or :class:`list`) -- Feature ID(s).

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed features in EPSG:4326. If some IDs don't return any features
                a list of missing ID(s) are returned as well.


   .. method:: navigate_byid(self, fsource: str, fid: str, navigation: str, source: str, distance: int = 500) -> gpd.GeoDataFrame

      Navigate the NHDPlus database from a single feature id up to a distance.

      :Parameters: * **fsource** (:class:`str`) -- The name of feature source. The valid sources are:
                     ``comid``, ``huc12pp``, ``nwissite``, ``wade``, ``WQP``.
                   * **fid** (:class:`str`) -- The ID of the feature.
                   * **navigation** (:class:`str`) -- The navigation method.
                   * **source** (:class:`str`, *optional*) -- Return the data from another source after navigating
                     the features using fsource, defaults to None.
                   * **distance** (:class:`int`, *optional*) -- Limit the search for navigation up to a distance in km,
                     defaults is 500 km. Note that this is an expensive request so you
                     have be mindful of the value that you provide. The value must be
                     between 1 to 9999 km.

      :returns: :class:`geopandas.GeoDataFrame` -- NLDI indexed features in EPSG:4326.


   .. method:: navigate_byloc(self, coords: Tuple[float, float], navigation: Optional[str] = None, source: Optional[str] = None, loc_crs: str = DEF_CRS, distance: int = 500) -> gpd.GeoDataFrame

      Navigate the NHDPlus database from a coordinate.

      :Parameters: * **coords** (:class:`tuple`) -- A tuple of length two (x, y).
                   * **navigation** (:class:`str`, *optional*) -- The navigation method, defaults to None which throws an exception
                     if comid_only is False.
                   * **source** (:class:`str`, *optional*) -- Return the data from another source after navigating
                     the features using fsource, defaults to None which throws an exception
                     if comid_only is False.
                   * **loc_crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to EPSG:4326.
                   * **distance** (:class:`int`, *optional*) -- Limit the search for navigation up to a distance in km,
                     defaults to 500 km. Note that this is an expensive request so you
                     have be mindful of the value that you provide. If you want to get
                     all the available features you can pass a large distance like 9999999.

      :returns: :class:`geopandas.GeoDataFrame` -- NLDI indexed features in EPSG:4326.



.. py:class:: ScienceBase(save_dir: Optional[str] = None)

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: **save_dir** (:class:`str`) -- Directory to save the staged data frame containing metadata for the database,
                defaults to system's temp directory. The metadata dataframe is saved as a feather
                file, nhdplus_attrs.feather, in save_dir that can be loaded with Pandas.

   .. method:: get_children(self, item: str) -> Dict[str, Any]

      Get children items of an item.


   .. method:: get_files(self, item: str) -> Dict[str, Tuple[str, str]]

      Get all the available zip files in an item.


   .. method:: stage_data(self) -> pd.DataFrame

      Stage the NHDPlus Attributes database and save to nhdplus_attrs.feather.



.. py:class:: WaterData(layer: str, crs: str = DEF_CRS)

   Access to `Water Data <https://labs.waterdata.usgs.gov/geoserver>`__ service.

   :Parameters: * **layer** (:class:`str`) -- A valid layer from the WaterData service. Valid layers are:
                  ``nhdarea``, ``nhdwaterbody``, ``catchmentsp``, ``nhdflowline_network``
                  ``gagesii``, ``huc08``, ``huc12``, ``huc12agg``, and ``huc12all``. Note that
                  the layers' worksapce for the Water Data service is ``wmadata`` which will
                  be added to the given ``layer`` argument if it is not provided.
                * **crs** (:class:`str`, *optional*) -- The target spatial reference system, defaults to ``epsg:4326``.

   .. method:: bybox(self, bbox: Tuple[float, float, float, float], box_crs: str = DEF_CRS) -> gpd.GeoDataFrame

      Get features within a bounding box.


   .. method:: bydistance(self, coords: Tuple[float, float], distance: int, loc_crs: str = DEF_CRS) -> gpd.GeoDataFrame

      Get features within a radius (in meters) of a point.


   .. method:: byfilter(self, cql_filter: str, method: str = 'GET') -> gpd.GeoDataFrame

      Get features based on a CQL filter.


   .. method:: bygeom(self, geometry: Union[Polygon, MultiPolygon], geo_crs: str = DEF_CRS, xy: bool = True, predicate: str = 'INTERSECTS') -> gpd.GeoDataFrame

      Get features within a geometry.

      :Parameters: * **geometry** (:class:`shapely.geometry`) -- The input geometry
                   * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, default to epsg:4326.
                   * **xy** (:class:`bool`, *optional*) -- Whether axis order of the input geometry is xy or yx.
                   * **predicate** (:class:`str`, *optional*) -- The geometric prediacte to use for requesting the data, defaults to
                     INTERSECTS. Valid predicates are:
                     ``EQUALS``, ``DISJOINT``, ``INTERSECTS``, ``TOUCHES``, ``CROSSES``, ``WITHIN``
                     ``CONTAINS``, ``OVERLAPS``, ``RELATE``, ``BEYOND``

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features in the given geometry.


   .. method:: byid(self, featurename: str, featureids: Union[List[str], str]) -> gpd.GeoDataFrame

      Get features based on IDs.



.. function:: nhdplus_attrs(name: Optional[str] = None, save_dir: Optional[str] = None) -> pd.DataFrame

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: * **name** (:class:`str`, *optional*) -- Name of the NHDPlus attribute, defaults to None which returns a dataframe containing
                  metadata of all the available attributes in the database.
                * **save_dir** (:class:`str`, *optional*) -- Directory to save the staged data frame containing metadata for the database,
                  defaults to system's temp directory. The metadata dataframe is saved as a feather
                  file, nhdplus_attrs.feather, in save_dir that can be loaded with Pandas.

   :returns: :class:`pandas.DataFrame` -- Either a dataframe containing the database metadata or the requested attribute over CONUS.


.. function:: nhdplus_vaa(parquet_name: Optional[Union[Path, str]] = None) -> pd.DataFrame

   Get NHDPlus Value Added Attributes with ComID-level roughness and slope values.

   .. rubric:: Notes

   This downloads a 200 MB ``parquet`` file from
   `here <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726>`__ .
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_name** (:class:`str` or :class:`~~pathlib.Path`) -- Path to a file with ``.parquet`` extension for saving the processed to disk for
                later use.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.

   .. rubric:: Examples

   >>> import tempfile
   >>> from pathlib import Path
   >>> vaa = nhdplus_vaa(Path(tempfile.gettempdir(), "nhdplus_vaa.parquet"))
   >>> print(vaa.slope.max())
   4.6


