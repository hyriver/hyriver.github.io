pygeohydro.nlcd
===============

.. py:module:: pygeohydro.nlcd

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.





Module Contents
---------------

.. py:function:: cover_statistics(cover_da)

   Percentages of the categorical NLCD cover data.

   :Parameters: **cover_da** (:class:`xarray.DataArray`) -- Land cover DataArray from a LULC Dataset from the ``nlcd_bygeom`` function.

   :returns: :class:`Stats` -- A named tuple with the percentages of the cover classes and categories.


.. py:function:: nlcd_area_percent(geo_df, year = 2019, region = 'L48')

   Compute the area percentages of the natural, developed, and impervious areas.

   .. rubric:: Notes

   This function uses imperviousness and land use/land cover data from NLCD
   to compute the area percentages of the natural, developed, and impervious areas.
   It considers land cover classes of 21 to 24 as urban and the rest as natural.
   Then, uses imperviousness percentage to partition the urban area into developed
   and impervious areas. So, ``urban = developed + impervious`` and always
   ``natural + urban = natural + developed + impervious = 100``.

   :Parameters: * **geo_df** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with the geometry to query. The indices are used
                  as keys in the output dictionary.
                * **year** (:class:`int`, *optional*) -- Year of the NLCD data, defaults to 2019. Available years are 2021, 2019, 2016,
                  2013, 2011, 2008, 2006, 2004, and 2001.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.

   :returns: :class:`pandas.DataFrame` -- A dataframe with the same index as input ``geo_df`` and columns are the area
             percentages of the natural, developed, impervious, and urban
             (sum of developed and impervious) areas. Sum of urban and natural percentages
             is always 100, as well as the sum of natural, developed, and impervious
             percentages.


.. py:function:: nlcd_bycoords(coords, years = None, region = 'L48', ssl = True)

   Get data from NLCD database (2019).

   :Parameters: * **coords** (:class:`list` of :class:`tuple`) -- List of coordinates in the form of (longitude, latitude).
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.
                * **ssl** (:class:`bool`, *optional*) -- Whether to use SSL for the connection, defaults to ``True``.

   :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame with the NLCD data and the coordinates.


.. py:function:: nlcd_bygeom(geometry, resolution = 30, years = None, region = 'L48', crs = 4326, ssl = True)

   Get data from NLCD database (2019).

   :Parameters: * **geometry** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with the geometry to query. The indices are used
                  as keys in the output dictionary.
                * **resolution** (:class:`float`, *optional*) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution. The default is 30 m which is the
                  native resolution of NLCD data.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD layers as a dictionary, defaults to
                  ``{'impervious': [2019], 'cover': [2019], 'canopy': [2019], "descriptor": [2019]}``.
                  Layers that are not in years are ignored, e.g., ``{'cover': [2016, 2019]}`` returns
                  land cover data for 2016 and 2019.
                * **region** (:class:`str`, *optional*) -- Region in the US that the input geometries are located, defaults to ``L48``.
                  Valid values are ``L48`` (for CONUS), ``HI`` (for Hawaii), ``AK`` (for Alaska),
                  and ``PR`` (for Puerto Rico). Both lower and upper cases are acceptable.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  ``epsg:4326``.
                * **ssl** (:class:`bool`, *optional*) -- Whether to use SSL for the connection, defaults to ``True``.

   :returns: :class:`dict` of :class:`xarray.Dataset` or :class:`xarray.Dataset` -- A single or a ``dict`` of NLCD datasets. If dict, the keys are indices
             of the input ``GeoDataFrame``.


.. py:function:: overland_roughness(cover_da)

   Estimate overland roughness from land cover data.

   :Parameters: **cover_da** (:class:`xarray.DataArray`) -- Land cover DataArray from a LULC Dataset from the ``nlcd_bygeom`` function.

   :returns: :class:`xarray.DataArray` -- Overland roughness


