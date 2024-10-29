pygeohydro.pygeohydro
=====================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.







Module Contents
---------------

.. py:class:: EHydro(data_type = 'points', cache_dir = 'ehydro_cache')



   Access USACE Hydrographic Surveys (eHydro).

   .. rubric:: Notes

   For more info visit: https://navigation.usace.army.mil/Survey/Hydro

   .. method:: bygeom(geom, geo_crs=4326, sql_clause="", distance=None, return_m=False, return_geom=True)

      Get features within a geometry that can be combined with a SQL where clause.

   .. method:: byids(field, fids, return_m=False, return_geom=True)

      Get features by object IDs.

   .. method:: bysql(sql_clause, return_m=False, return_geom=True)

      Get features using a valid SQL 92 WHERE clause.
      

   :Parameters: * **data_type** (:class:`str`, *optional*) -- Type of the survey data to retrieve, defaults to ``points``.
                  Note that the ``points`` data type gets the best available point
                  cloud data, i.e., if ``SurveyPointHD`` is available, it will be
                  returned, otherwise ``SurveyPoint`` will be returned.
                  Available types are:

                  - ``points``: Point clouds
                  - ``outlines``: Polygons of survey outlines
                  - ``contours``: Depth contours
                  - ``bathymetry``: Bathymetry data

                  Note that point clouds are not available for all surveys.
                * **cache_dir** (:class:`str` or :class:`pathlib.Path`, *optional*) -- Directory to store the downloaded raw data, defaults to ``./ehydro_cache``.


   .. py:property:: survey_grid
      :type: geopandas.GeoDataFrame


      Full survey availability on hexagonal grid cells of 35 km resolution.


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


.. py:function:: soil_soilgrids(layers, geometry, geo_crs = 4326)

   Get soil data from SoilGrids for the area of interest.

   .. rubric:: Notes

   For more information on the SoilGrids dataset, visit
   `ISRIC <https://www.isric.org/explore/soilgrids/faq-soilgrids#What_do_the_filename_codes_mean>`__.

   :Parameters: * **layers** (:class:`list` of :class:`str`) -- SoilGrids layers to get. Available options are:
                  ``bdod_*``, ``cec_*``, ``cfvo_*``, ``clay_*``, ``nitrogen_*``, ``ocd_*``,
                  ``ocs_*``, ``phh2o_*``, ``sand_*``, ``silt_*``, and ``soc_*`` where ``*``
                  is the depth in cm and can be one of ``5``, ``15``, ``30``, ``60``,
                  ``100``, or ``200``. For example, ``bdod_5`` is the mean bulk density of
                  the fine earth fraction at 0-5 cm depth, and ``bdod_200`` is the mean bulk
                  density of the fine earth fraction at 100-200 cm depth.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry to get DEM within. It can be a polygon or a boundong box
                  of form (xmin, ymin, xmax, ymax).
                * **geo_crs** (:class:`int`, :class:`str`, :class:`of pyproj.CRS`, *optional*) -- CRS of the input geometry, defaults to ``epsg:4326``.

   :returns: :class:`xarray.DataArray` -- The request DEM at the specified resolution.


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


