pygeohydro.nid
==============

.. py:module:: pygeohydro.nid

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

      Download the entire NID inventory data and save to a parquet file.

      :Parameters: **fname** (:class:`str`, :class:`pathlib.Path`, *optional*) -- The path to the file to save the data to, defaults to
                   ``./cache/full_nid_inventory.parquet``.



   .. py:property:: df
      Entire NID inventory (``csv`` version) as a ``pandas.DataFrame``.


   .. py:property:: gdf
      Entire NID inventory (``gpkg`` version) as a ``geopandas.GeoDataFrame``.


   .. py:property:: nid_inventory_path
      :type: pathlib.Path

      Path to the NID inventory parquet file.


