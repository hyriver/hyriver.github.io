:py:mod:`pynhd.pynhd`
=====================

.. py:module:: pynhd.pynhd

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



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



.. py:class:: NHDPlusHR(layer = None, outfields = '*', crs = DEF_CRS, service = 'hydro', auto_switch = False)



   Access NHDPlus HR database through the National Map ArcGISRESTful.

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. To see a list of available layers instantiate the class
                  without passing any argument like so ``NHDPlusHR()``.
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to EPSG:4326
                * **service** (:class:`str`, *optional*) -- Name of the web service to use, defaults to hydro. Supported web services are:

                  * hydro: https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer
                  * edits: https://edits.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/NHDPlus_HR/MapServer
                * **auto_switch** (:class:`bool`, *optional*) -- Automatically switch to other services' URL if the first one doesn't work, default to False.


.. py:class:: NLDI

   Access the Hydro Network-Linked Data Index (NLDI) service.

   .. py:method:: comid_byloc(self, coords, loc_crs = DEF_CRS)

      Get the closest ComID(s) based on coordinates.

      :Parameters: * **coords** (:class:`tuple` or :class:`list`) -- A tuple of length two (x, y) or a list of them.
                   * **loc_crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to EPSG:4326.

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed ComID(s) in EPSG:4326. If some coords don't return any ComID
                a list of missing coords are returned as well.


   .. py:method:: get_basins(self, station_ids)

      Get basins for a list of station IDs.

      :Parameters: **station_ids** (:class:`str` or :class:`list`) -- USGS station ID(s).

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed basins in EPSG:4326. If some IDs don't return any features
                a list of missing ID(s) are returned as well.


   .. py:method:: get_validchars(self, char_type)

      Get all the available characteristics IDs for a given characteristics type.


   .. py:method:: getcharacteristic_byid(self, comids, char_type, char_ids = 'all', values_only = True)

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


   .. py:method:: getfeature_byid(self, fsource, fid)

      Get feature(s) based ID(s).

      :Parameters: * **fsource** (:class:`str`) -- The name of feature(s) source. The valid sources are:
                     comid, huc12pp, nwissite, wade, wqp
                   * **fid** (:class:`str` or :class:`list`) -- Feature ID(s).

      :returns: :class:`geopandas.GeoDataFrame` or :class:`(geopandas.GeoDataFrame`, :class:`list)` -- NLDI indexed features in EPSG:4326. If some IDs don't return any features
                a list of missing ID(s) are returned as well.


   .. py:method:: navigate_byid(self, fsource, fid, navigation, source, distance = 500)

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


   .. py:method:: navigate_byloc(self, coords, navigation = None, source = None, loc_crs = DEF_CRS, distance = 500)

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



.. py:class:: PyGeoAPI

   Access `PyGeoAPI <https://labs.waterdata.usgs.gov/api/nldi/pygeoapi>`__ service.

   .. py:method:: cross_section(self, coord, width, numpts, crs = DEF_CRS)

      Return a GeoDataFrame from the xsatpoint service.

      :Parameters: * **coord** (:class:`tuple`) -- The coordinate of the point to extract the cross-section as a tuple,e.g., (lon, lat).
                   * **width** (:class:`float`) -- The width of the cross-section in meters.
                   * **numpts** (:class:`int`) -- The number of points to extract the cross-section from the DEM.
                   * **crs** (:class:`str`, *optional*) -- The coordinate reference system of the coordinates, defaults to EPSG:4326.

      :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame containing the cross-section at the requested point.

      .. rubric:: Examples

      >>> from pynhd import PyGeoAPI
      >>> pygeoapi = PyGeoAPI()
      >>> gdf = pygeoapi.cross_section((-103.80119, 40.2684), width=1000.0, numpts=101, crs=DEF_CRS)
      >>> print(gdf.iloc[-1, 1])
      1000.0


   .. py:method:: elevation_profile(self, coords, numpts, dem_res, crs = DEF_CRS)

      Return a GeoDataFrame from the xsatendpts service.

      :Parameters: * **coords** (:class:`list`) -- A list of two coordinates to trace as a list of tuples,e.g., [(lon, lat), (lon, lat)].
                   * **numpts** (:class:`int`) -- The number of points to extract the elevation profile from the DEM.
                   * **dem_res** (:class:`int`) -- The target resolution for requesting the DEM from 3DEP service.
                   * **crs** (:class:`str`, *optional*) -- The coordinate reference system of the coordinates, defaults to EPSG:4326.

      :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame containing the elevation profile along the requested endpoints.

      .. rubric:: Examples

      >>> from pynhd import PyGeoAPI
      >>> pygeoapi = PyGeoAPI()
      >>> gdf = pygeoapi.elevation_profile(
      ...     [(-103.801086, 40.26772), (-103.80097, 40.270568)], numpts=101, dem_res=1, crs=DEF_CRS
      ... )
      >>> print(gdf.iloc[-1, 1])
      411.5906


   .. py:method:: flow_trace(self, coord, crs = DEF_CRS, raindrop = False, direction = 'down')

      Return a GeoDataFrame from the flowtrace service.

      :Parameters: * **coord** (:class:`tuple`) -- The coordinate of the point to trace as a tuple,e.g., (lon, lat).
                   * **crs** (:class:`str`) -- The coordinate reference system of the coordinates, defaults to EPSG:4326.
                   * **raindrop** (:class:`bool`, *optional*) -- If True, use raindrop-based flowpaths, i.e. use raindrop trace web service
                     with direction set to "none", defaults to False.
                   * **direction** (:class:`str`, *optional*) -- The direction of flowpaths, either "down", "up", or "none". Defaults to "down".

      :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame containing the traced flowline.

      .. rubric:: Examples

      >>> from pynhd import PyGeoAPI
      >>> pygeoapi = PyGeoAPI()
      >>> gdf = pygeoapi.flow_trace(
      ...     (1774209.63, 856381.68), crs="ESRI:102003", raindrop=False, direction="none"
      ... )
      >>> print(gdf.comid.iloc[0])
      22294818


   .. py:method:: split_catchment(self, coord, crs = DEF_CRS, upstream = False)

      Return a GeoDataFrame from the splitcatchment service.

      :Parameters: * **coord** (:class:`tuple`) -- The coordinate of the point to trace as a tuple,e.g., (lon, lat).
                   * **crs** (:class:`str`, *optional*) -- The coordinate reference system of the coordinates, defaults to EPSG:4326.
                   * **upstream** (:class:`bool`, *optional*) -- If True, return all upstream catchments rather than just the local catchment,
                     defaults to False.

      :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame containing the local catchment or the entire upstream catchments.

      .. rubric:: Examples

      >>> from pynhd import PyGeoAPI
      >>> pygeoapi = PyGeoAPI()
      >>> gdf = pygeoapi.split_catchment((-73.82705, 43.29139), crs=DEF_CRS, upstream=False)
      >>> print(gdf.catchmentID.iloc[0])
      22294818



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



.. py:class:: WaterData(layer, crs = DEF_CRS)

   Access to `Water Data <https://labs.waterdata.usgs.gov/geoserver>`__ service.

   :Parameters: * **layer** (:class:`str`) -- A valid layer from the WaterData service. Valid layers are:
                  ``nhdarea``, ``nhdwaterbody``, ``catchmentsp``, ``nhdflowline_network``
                  ``gagesii``, ``huc08``, ``huc12``, ``huc12agg``, and ``huc12all``. Note that
                  the layers' worksapce for the Water Data service is ``wmadata`` which will
                  be added to the given ``layer`` argument if it is not provided.
                * **crs** (:class:`str`, *optional*) -- The target spatial reference system, defaults to ``epsg:4326``.

   .. py:method:: bybox(self, bbox, box_crs = DEF_CRS)

      Get features within a bounding box.


   .. py:method:: bydistance(self, coords, distance, loc_crs = DEF_CRS)

      Get features within a radius (in meters) of a point.


   .. py:method:: byfilter(self, cql_filter, method = 'GET')

      Get features based on a CQL filter.


   .. py:method:: bygeom(self, geometry, geo_crs = DEF_CRS, xy = True, predicate = 'INTERSECTS')

      Get features within a geometry.

      :Parameters: * **geometry** (:class:`shapely.geometry`) -- The input geometry
                   * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, default to epsg:4326.
                   * **xy** (:class:`bool`, *optional*) -- Whether axis order of the input geometry is xy or yx.
                   * **predicate** (:class:`str`, *optional*) -- The geometric prediacte to use for requesting the data, defaults to
                     INTERSECTS. Valid predicates are:
                     ``EQUALS``, ``DISJOINT``, ``INTERSECTS``, ``TOUCHES``, ``CROSSES``, ``WITHIN``
                     ``CONTAINS``, ``OVERLAPS``, ``RELATE``, ``BEYOND``

      :returns: :class:`geopandas.GeoDataFrame` -- The requested features in the given geometry.


   .. py:method:: byid(self, featurename, featureids)

      Get features based on IDs.



.. py:function:: nhd_fcode()

   Get all the NHDPlus FCodes.


.. py:function:: nhdplus_attrs(name = None, save_dir = None)

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: * **name** (:class:`str`, *optional*) -- Name of the NHDPlus attribute, defaults to None which returns a dataframe containing
                  metadata of all the available attributes in the database.
                * **save_dir** (:class:`str`, *optional*) -- Directory to save the staged data frame containing metadata for the database,
                  defaults to system's temp directory. The metadata dataframe is saved as a feather
                  file, nhdplus_attrs.feather, in save_dir that can be loaded with Pandas.

   :returns: :class:`pandas.DataFrame` -- Either a dataframe containing the database metadata or the requested attribute over CONUS.


.. py:function:: nhdplus_vaa(parquet_name = None)

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

   >>> vaa = nhdplus_vaa()
   >>> print(vaa.slope.max())
   4.6


