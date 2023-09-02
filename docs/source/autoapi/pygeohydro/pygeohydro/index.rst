:py:mod:`pygeohydro.pygeohydro`
===============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: EHydro




   Access USACE Hydrographic Surveys (eHydro).

   .. rubric:: Notes

   For more info visit: https://navigation.usace.army.mil/Survey/Hydro


.. py:class:: NID


   Retrieve data from the National Inventory of Dams web service.

   .. py:property:: df

      Entire NID inventory (``csv`` version) as a ``pandas.DataFrame``.

   .. py:property:: gdf

      Entire NID inventory (``gpkg`` version) as a ``geopandas.GeoDataFrame``.

   .. py:property:: nid_inventory_path
      :type: pathlib.Path

      Path to the NID inventory feather file.

   .. py:method:: get_byfilter(query_list)

      Query dams by filters from the National Inventory of Dams web service.

      :Parameters: **query_list** (:class:`list` of :class:`dict`) -- List of dictionary of query parameters. For an exhaustive list of the parameters,
                   use the advanced fields dataframe that can be accessed via ``NID().fields_meta``.
                   Some filter require min/max values such as ``damHeight`` and ``drainageArea``.
                   For such filters, the min/max values should be passed like so:
                   ``{filter_key: ["[min1 max1]", "[min2 max2]"]}``.

      :returns: :class:`list` of :class:`geopandas.GeoDataFrame` -- Query results in the same order as the input query list.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> query_list = [
      ...    {"drainageArea": ["[200 500]"]},
      ...    {"nidId": ["CA01222"]},
      ... ]
      >>> dam_dfs = nid.get_byfilter(query_list)


   .. py:method:: get_bygeom(geometry, geo_crs)

      Retrieve NID data within a geometry.

      :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry or bounding box (west, south, east, north) for extracting the data.
                   * **geo_crs** (:class:`list` of :class:`str`) -- The CRS of the input geometry.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of NID data

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams = nid.get_bygeom((-69.77, 45.07, -69.31, 45.45), 4326)


   .. py:method:: get_suggestions(text, context_key = None)

      Get suggestions from the National Inventory of Dams web service.

      .. rubric:: Notes

      This function is useful for exploring and/or narrowing down the filter fields
      that are needed to query the dams using ``get_byfilter``.

      :Parameters: * **text** (:class:`str`) -- Text to query for suggestions.
                   * **context_key** (:class:`str`, *optional*) -- Suggestion context, defaults to empty string, i.e., all context keys.
                     For a list of valid context keys, see ``NID().fields_meta``.

      :returns: :class:`tuple` of :class:`pandas.DataFrame` -- The suggestions for the requested text as two DataFrames:
                First, is suggestions found in the dams properties and
                second, those found in the query fields such as states, huc6, etc.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams, contexts = nid.get_suggestions("houston", "city")


   .. py:method:: inventory_byid(federal_ids)

      Get extra attributes for dams based on their dam ID.

      .. rubric:: Notes

      This function is meant to be used for getting extra attributes for dams.
      For example, first you need to use either ``get_bygeom`` or ``get_byfilter``
      to get basic attributes of the target dams. Then you can use this function
      to get extra attributes using the ``id`` column of the ``GeoDataFrame``
      that ``get_bygeom`` or ``get_byfilter`` returns.

      :Parameters: **federal_ids** (:class:`list` of :class:`str`) -- List of the target dam Federal IDs.

      :returns: :class:`pandas.DataFrame` -- Dams with extra attributes in addition to the standard NID fields
                that other ``NID`` methods return.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams = nid.inventory_byid(['KY01232', 'GA02400', 'NE04081', 'IL55070', 'TN05345'])


   .. py:method:: stage_nid_inventory(fname = None)

      Download the entire NID inventory data and save to a feather file.

      :Parameters: **fname** (:class:`str`, :class:`pathlib.Path`, *optional*) -- The path to the file to save the data to, defaults to
                   ``./cache/nid_inventory.feather``.



.. py:function:: cover_statistics(cover_da)

   Percentages of the categorical NLCD cover data.

   :Parameters: **cover_da** (:class:`xarray.DataArray`) -- Land cover DataArray from a LULC Dataset from the ``nlcd_bygeom`` function.

   :returns: :class:`Stats` -- A named tuple with the percentages of the cover classes and categories.


.. py:function:: get_camels()

   Get streaflow and basin attributes of all 671 stations in CAMELS dataset.

   .. rubric:: Notes

   For more info on CAMELS visit: https://ral.ucar.edu/solutions/products/camels

   :returns: :class:`tuple` of :class:`geopandas.GeoDataFrame` and :class:`xarray.Dataset` -- The first is basin attributes as a ``geopandas.GeoDataFrame`` and the second
             is streamflow data and basin attributes as an ``xarray.Dataset``.


.. py:function:: nlcd_area_percent(geo_df, year = 2019, region = 'L48')

   Compute the area percentages of the natural, developed, and impervious areas.

   .. rubric:: Notes

   This function uses imperviousness and land use/land cover data from NLCD
   to compute the area percentages of the natural, developed, and impervious areas.
   It considers land cover classes of 21 to 24 as urban and the rest as natural.
   Then, uses imperviousness percentage to partition the urban area into developed
   and impervious areas. So, ``urban = developed + impervious`` and always
   ``natural + urban = natural + developed + impervious = 100``.

   :Parameters: * **geometry** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with the geometry to query. The indices are used
                  as keys in the output dictionary.
                * **year** (:class:`int`, *optional*) -- Year of the NLCD data, defaults to 2019. Available years are 2021, 2019, 2016,
                  2013, 2011, 2008, 2006, 2004, and 2001.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.

   :returns: :class:`pandas.DataFrame` -- A dataframe with the same index as input ``geo_df`` and columns are the area
             percentages of the natural, developed, impervious, and urban
             (sum of developed and impervious) areas. Sum of urban and natural percentages
             is always 100, as well as the sume of natural, developed, and impervious
             percentages.


.. py:function:: nlcd_bycoords(coords, years = None, region = 'L48', ssl = None)

   Get data from NLCD database (2019).

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- List of coordinates in the form of (longitude, latitude).
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to ``False`` to disable
                  SSL certification verification.

   :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame with the NLCD data and the coordinates.


.. py:function:: nlcd_bygeom(geometry, resolution, years = None, region = 'L48', crs = 4326, ssl = None)

   Get data from NLCD database (2019).

   :Parameters: * **geometry** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with the geometry to query. The indices are used
                  as keys in the output dictionary.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to ``False`` to disable
                  SSL certification verification.

   :returns: :class:`dict` of :class:`xarray.Dataset` or :class:`xarray.Dataset` -- A single or a ``dict`` of NLCD datasets. If dict, the keys are indices
             of the input ``GeoDataFrame``.


.. py:function:: overland_roughness(cover_da)

   Estimate overland roughness from land cover data.

   :Parameters: **cover_da** (:class:`xarray.DataArray`) -- Land cover DataArray from a LULC Dataset from the ``nlcd_bygeom`` function.

   :returns: :class:`xarray.DataArray` -- Overland roughness


.. py:function:: soil_gnatsgo(layers, geometry, crs = 4326)

   Get US soil data from the gNATSGO dataset.

   .. rubric:: Notes

   This function uses Microsoft's Planetary Computer service to get the data.
   The dataset's description and its suppoerted soil properties can be found at:
   https://planetarycomputer.microsoft.com/dataset/gnatsgo-rasters

   :Parameters: * **layers** (:class:`list` of :class:`str` or :class:`str`) -- Target layer(s). Available layers can be found at the dataset's website
                  `here <https://planetarycomputer.microsoft.com/dataset/gnatsgo-rasters>`__.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry or bounding box of the region of interest.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- The input geometry CRS, defaults to ``epsg:4326``.

   :returns: :class:`xarray.Dataset` -- Requested soil properties.


.. py:function:: soil_properties(properties = '*', soil_dir = 'cache')

   Get soil properties dataset in the United States from ScienceBase.

   .. rubric:: Notes

   This function downloads the source zip files from
   `ScienceBase <https://www.sciencebase.gov/catalog/item/5fd7c19cd34e30b9123cb51f>`__
   , extracts the included ``.tif`` files, and return them as an ``xarray.Dataset``.

   :Parameters: * **properties** (:class:`list` of :class:`str` or :class:`str`, *optional*) -- Soil properties to extract, default to "*", i.e., all the properties.
                  Available properties are ``awc`` for available water capacity, ``fc`` for
                  field capacity, and ``por`` for porosity.
                * **soil_dir** (:class:`str` or :class:`pathlib.Pathlib.Path`) -- Directory to store zip files or if exists read from them, defaults to
                  ``./cache``.


.. py:function:: ssebopeta_bycoords(coords, dates, crs = 4326)

   Daily actual ET for a dataframe of coords from SSEBop database in mm/day.

   :Parameters: * **coords** (:class:`pandas.DataFrame`) -- A dataframe with ``id``, ``x``, ``y`` columns.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input coordinates, defaults to ``epsg:4326``.

   :returns: :class:`xarray.Dataset` -- Daily actual ET in mm/day as a dataset with ``time`` and ``location_id`` dimensions.
             The ``location_id`` dimension is the same as the ``id`` column in the input dataframe.


.. py:function:: ssebopeta_bygeom(geometry, dates, geo_crs = 4326)

   Get daily actual ET for a region from SSEBop database.

   .. rubric:: Notes

   Since there's still no web service available for subsetting SSEBop, the data first
   needs to be downloaded for the requested period then it is masked by the
   region of interest locally. Therefore, it's not as fast as other functions and
   the bottleneck could be the download speed.

   :Parameters: * **geometry** (:class:`shapely.geometry.Polygon` or :class:`tuple`) -- The geometry for downloading clipping the data. For a tuple bbox,
                  the order should be (west, south, east, north).
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input geometry, defaults to ``epsg:4326``.

   :returns: :class:`xarray.DataArray` -- Daily actual ET within a geometry in mm/day at 1 km resolution


