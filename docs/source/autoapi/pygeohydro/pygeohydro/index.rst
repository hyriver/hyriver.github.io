:py:mod:`pygeohydro.pygeohydro`
===============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NID(expire_after = EXPIRE, disable_caching = False)

   Retrieve data from the National Inventory of Dams web service.

   :Parameters: * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   .. py:method:: get_byfilter(self, query_list)

      Query dams by filters from the National Inventory of Dams web service.

      :Parameters: **query_list** (:class:`list` of :class:`dict`) -- List of dictionary of query parameters. For an exhaustive list of the parameters,
                   use the advanced fields dataframe that can be accessed via ``NID().fields_meta``.
                   Some filter require min/max values such as ``damHeight`` and ``drainageArea``.
                   For such filters, the min/max values should be passed like so:
                   ``{filter_key: ["[min1 max1]", "[min2 max2]"]}``.

      :returns: :class:`geopandas.GeoDataFrame` -- Query results.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> query_list = [
      ...    {"huc6": ["160502", "100500"], "drainageArea": ["[200 500]"]},
      ...    {"nidId": ["CA01222"]},
      ... ]
      >>> dam_dfs = nid.get_byfilter(query_list)
      >>> print(dam_dfs[0].name[0])
      Stillwater Point Dam


   .. py:method:: get_bygeom(self, geometry, geo_crs)

      Retrieve NID data within a geometry.

      :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- Geometry or bounding box (west, south, east, north) for extracting the data.
                   * **geo_crs** (:class:`list` of :class:`str`) -- The CRS of the input geometry, defaults to epsg:4326.

      :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of NID data

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams = nid.get_bygeom((-69.77, 45.07, -69.31, 45.45), "epsg:4326")
      >>> print(dams.name.iloc[0])
      Little Moose


   .. py:method:: get_suggestions(self, text, context_key = '')

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
      >>> dams, contexts = nid.get_suggestions("texas", "huc2")
      >>> print(contexts.loc["HUC2", "value"])
      12


   .. py:method:: inventory_byid(self, dam_ids)

      Get extra attributes for dams based on their dam ID.

      .. rubric:: Notes

      This function is meant to be used for getting extra attributes for dams.
      For example, first you need to use either ``get_bygeom`` or ``get_byfilter``
      to get basic attributes of the target dams. Then you can use this function
      to get extra attributes using the ``id`` column of the ``GeoDataFrame``
      that ``get_bygeom`` or ``get_byfilter`` returns.

      :Parameters: **dam_ids** (:class:`list` of :class:`int` or :class:`str`) -- List of the target dam IDs (digists only). Note that the dam IDs are not the
                   same as the NID IDs.

      :returns: :class:`pandas.DataFrame` -- Dams with extra attributes in addition to the standard NID fields
                that other ``NID`` methods return.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams = nid.inventory_byid([514871, 459170, 514868, 463501, 463498])
      >>> print(dams.damHeight.max())
      120.0



.. py:function:: cover_statistics(ds)

   Percentages of the categorical NLCD cover data.

   :Parameters: **ds** (:class:`xarray.DataArray`) -- Cover DataArray from a LULC Dataset from the ``nlcd`` function.

   :returns: :class:`dict` -- Statistics of NLCD cover data


.. py:function:: nlcd(geometry, resolution, years = None, region = 'L48', geo_crs = DEF_CRS, crs = DEF_CRS)

   Get data from NLCD database (2019).

   .. deprecated:: 0.11.5
       Use :func:`nlcd_bygeom` or :func:`nlcd_bycoords`  instead.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry or bounding box (west, south, east, north) for extracting the data.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to ``L48``. Valid values are ``L48`` (for CONUS),
                  ``HI`` (for Hawaii), ``AK`` (for Alaska), and ``PR`` (for Puerto Rico).
                  Both lower and upper cases are acceptable.
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.

   :returns: :class:`xarray.Dataset` -- NLCD within a geometry


.. py:function:: nlcd_bycoords(coords, years = None, region = 'L48', expire_after = EXPIRE, disable_caching = False)

   Get data from NLCD database (2019).

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- List of coordinates in the form of (longitude, latitude).
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to ``L48``. Valid values are ``L48`` (for CONUS),
                  ``HI`` (for Hawaii), ``AK`` (for Alaska), and ``PR`` (for Puerto Rico).
                  Both lower and upper cases are acceptable.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame with the NLCD data and the coordinates.


.. py:function:: nlcd_bygeom(geometry, resolution, years = None, region = 'L48', crs = DEF_CRS, expire_after = EXPIRE, disable_caching = False)

   Get data from NLCD database (2019).

   :Parameters: * **geometry** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with the geometry to query. The indices are used
                  as keys in the output dictionary.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to ``L48``. Valid values are ``L48`` (for CONUS),
                  ``HI`` (for Hawaii), ``AK`` (for Alaska), and ``PR`` (for Puerto Rico).
                  Both lower and upper cases are acceptable.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`dict` of :class:`xarray.Dataset` or :class:`xarray.Dataset` -- A single or a ``dict`` of NLCD datasets. If dict, the keys are indices
             of the input ``GeoDataFrame``.


.. py:function:: ssebopeta_bycoords(coords, dates, crs = DEF_CRS)

   Daily actual ET for a dataframe of coords from SSEBop database in mm/day.

   :Parameters: * **coords** (:class:`pandas.DataFrame`) -- A dataframe with ``id``, ``x``, ``y`` columns.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, *optional*) -- The CRS of the input coordinates, defaults to epsg:4326.

   :returns: :class:`xarray.Dataset` -- Daily actual ET in mm/day as a dataset with ``time`` and ``location_id`` dimensions.
             The ``location_id`` dimension is the same as the ``id`` column in the input dataframe.


.. py:function:: ssebopeta_bygeom(geometry, dates, geo_crs = DEF_CRS)

   Get daily actual ET for a region from SSEBop database.

   .. rubric:: Notes

   Since there's still no web service available for subsetting SSEBop, the data first
   needs to be downloaded for the requested period then it is masked by the
   region of interest locally. Therefore, it's not as fast as other functions and
   the bottleneck could be the download speed.

   :Parameters: * **geometry** (:class:`shapely.geometry.Polygon` or :class:`tuple`) -- The geometry for downloading clipping the data. For a tuple bbox,
                  the order should be (west, south, east, north).
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.

   :returns: :class:`xarray.DataArray` -- Daily actual ET within a geometry in mm/day at 1 km resolution


.. py:function:: ssebopeta_byloc(coords, dates)

   Daily actual ET for a location from SSEBop database in mm/day.

   .. deprecated:: 0.11.5
       Use :func:`ssebopeta_bycoords` instead. For now, this function calls
       :func:`ssebopeta_bycoords` but retains the same functionality, i.e.,
       returns a dataframe and accepts only a single coordinate. Whereas the
       new function returns a ``xarray.Dataset`` and accepts a dataframe
       containing coordinates.

   :Parameters: * **coords** (:class:`tuple`) -- Longitude and latitude of a single location as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].

   :returns: :class:`pandas.Series` -- Daily actual ET for a location


