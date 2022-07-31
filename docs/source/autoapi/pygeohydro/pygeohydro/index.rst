:py:mod:`pygeohydro.pygeohydro`
===============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NID

   Retrieve data from the National Inventory of Dams web service.

   .. py:method:: get_byfilter(query_list)

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
      ...    {"drainageArea": ["[200 500]"]},
      ...    {"nidId": ["CA01222"]},
      ... ]
      >>> dam_dfs = nid.get_byfilter(query_list)
      >>> print(dam_dfs[0].loc[dam_dfs[0].name == "Prairie Portage"].id.item())
      496613


   .. py:method:: get_bygeom(geometry, geo_crs)

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


   .. py:method:: get_suggestions(text, context_key = '')

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
      >>> dams, contexts = nid.get_suggestions("texas", "city")
      >>> print(contexts.loc["CITY", "value"])
      Texas City


   .. py:method:: inventory_byid(dam_ids, stage_nid = False)

      Get extra attributes for dams based on their dam ID.

      .. rubric:: Notes

      This function is meant to be used for getting extra attributes for dams.
      For example, first you need to use either ``get_bygeom`` or ``get_byfilter``
      to get basic attributes of the target dams. Then you can use this function
      to get extra attributes using the ``id`` column of the ``GeoDataFrame``
      that ``get_bygeom`` or ``get_byfilter`` returns.

      :Parameters: * **dam_ids** (:class:`list` of :class:`int` or :class:`str`) -- List of the target dam IDs (digists only). Note that the dam IDs are not the
                     same as the NID IDs.
                   * **stage_nid** (:class:`bool`, *optional*) -- Whether to get the entire NID and then query locally or query from the
                     NID web service which tends to be very slow for large number of requests.
                     Defaults to ``False``. The staged NID database is saved as a `feather` file
                     in `./cache/nid_inventory.feather`.

      :returns: :class:`pandas.DataFrame` -- Dams with extra attributes in addition to the standard NID fields
                that other ``NID`` methods return.

      .. rubric:: Examples

      >>> from pygeohydro import NID
      >>> nid = NID()
      >>> dams = nid.inventory_byid([514871, 459170, 514868, 463501, 463498])
      >>> print(dams.damHeight.max())
      120.0


   .. py:method:: stage_nid_inventory(fname = None)

      Download the entire NID inventory data and save to a feather file.

      :Parameters: **fname** (:class:`str`, :class:`pathlib.Path`, *optional*) -- The path to the file to save the data to, defaults to
                   ``./cache/nid_inventory.feather``.



.. py:class:: WBD(layer, outfields = '*', crs = DEF_CRS)



   Access Watershed Boundary Dataset (WBD).

   .. rubric:: Notes

   This file contains Hydrologic Unit (HU) polygon boundaries for the United States,
   Puerto Rico, and the U.S. Virgin Islands.
   For more info visit: https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. Valid layers are:

                  - ``wbdline``
                  - ``huc2``
                  - ``huc4``
                  - ``huc6``
                  - ``huc8``
                  - ``huc10``
                  - ``huc12``
                  - ``huc14``
                  - ``huc16``
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, *optional*) -- Target spatial reference, default to ``EPSG:4326``.


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


.. py:function:: nlcd_bycoords(coords, years = None, region = 'L48', ssl = None)

   Get data from NLCD database (2019).

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- List of coordinates in the form of (longitude, latitude).
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US, defaults to ``L48``. Valid values are ``L48`` (for CONUS),
                  ``HI`` (for Hawaii), ``AK`` (for Alaska), and ``PR`` (for Puerto Rico).
                  Both lower and upper cases are acceptable.
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to ``False`` to disable
                  SSL certification verification.

   :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame with the NLCD data and the coordinates.


.. py:function:: nlcd_bygeom(geometry, resolution, years = None, region = 'L48', crs = DEF_CRS, ssl = None)

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
                * **ssl** (:class:`bool` or :class:`SSLContext`, *optional*) -- SSLContext to use for the connection, defaults to None. Set to ``False`` to disable
                  SSL certification verification.

   :returns: :class:`dict` of :class:`xarray.Dataset` or :class:`xarray.Dataset` -- A single or a ``dict`` of NLCD datasets. If dict, the keys are indices
             of the input ``GeoDataFrame``.


.. py:function:: overland_roughness(cover_da)

   Estimate overland roughness from land cover data.

   :Parameters: **cover_da** (:class:`xarray.DataArray`) -- Land cover DataArray from a LULC Dataset from the ``nlcd_bygeom`` function.

   :returns: :class:`xarray.DataArray` -- Overland roughness


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


