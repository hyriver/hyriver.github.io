:py:mod:`pygeohydro.pygeohydro`
===============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: EHydro(data_type = 'points')




   Access USACE Hydrographic Surveys (eHydro).

   .. rubric:: Notes

   For more info visit: https://navigation.usace.army.mil/Survey/Hydro

   .. method:: bygeom(geom, geo_crs=4326, sql_clause="", distance=None, return_m=False, return_geom=True)

      Get features within a geometry that can be combined with a SQL where clause.

   .. method:: byids(field, fids, return_m=False, return_geom=True)

      Get features by object IDs.

   .. method:: bysql(sql_clause, return_m=False, return_geom=True)

      Get features using a valid SQL 92 WHERE clause.
      

   :Parameters: **data_type** (:class:`str`, *optional*) -- Type of the survey data to retrieve, defaults to ``points``.
                Note that the ``points`` data type gets the best available point
                cloud data, i.e., if ``SurveyPointHD`` is available, it will be
                returned, otherwise ``SurveyPoint`` will be returned.
                Available types are:

                - ``points``: Point clouds
                - ``outlines``: Polygons of survey outlines
                - ``contours``: Depth contours
                - ``bathymetry``: Bathymetry data

                Note that point clouds are not available for all surveys.

   .. py:property:: survey_grid
      :type: geopandas.GeoDataFrame

      Full survey availability on hexagonal grid cells of 35 km resolution.


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



.. py:function:: get_camels()

   Get streaflow and basin attributes of all 671 stations in CAMELS dataset.

   .. rubric:: Notes

   For more info on CAMELS visit: https://ral.ucar.edu/solutions/products/camels

   :returns: :class:`tuple` of :class:`geopandas.GeoDataFrame` and :class:`xarray.Dataset` -- The first is basin attributes as a ``geopandas.GeoDataFrame`` and the second
             is streamflow data and basin attributes as an ``xarray.Dataset``.


.. py:function:: soil_gnatsgo(layers, geometry, crs = 4326)

   Get US soil data from the gNATSGO dataset.

   .. rubric:: Notes

   This function uses Microsoft's Planetary Computer service to get the data.
   The dataset's description and its supported soil properties can be found at:
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

   :Parameters: * **geometry** (:class:`shapely.Polygon` or :class:`tuple`) -- The geometry for downloading clipping the data. For a tuple bbox,
                  the order should be (west, south, east, north).
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input geometry, defaults to ``epsg:4326``.

   :returns: :class:`xarray.DataArray` -- Daily actual ET within a geometry in mm/day at 1 km resolution


