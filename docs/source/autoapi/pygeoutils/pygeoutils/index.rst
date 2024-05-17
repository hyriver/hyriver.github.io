:py:mod:`pygeoutils.pygeoutils`
===============================

.. py:module:: pygeoutils.pygeoutils

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.



Module Contents
---------------

.. py:function:: arcgis2geojson(arcgis, id_attr = None)

   Convert ESRIGeoJSON format to GeoJSON.

   .. rubric:: Notes

   Based on `arcgis2geojson <https://github.com/chris48s/arcgis2geojson>`__.

   :Parameters: * **arcgis** (:class:`str` or :class:`binary`) -- The ESRIGeoJSON format str (or binary)
                * **id_attr** (:class:`str`, *optional*) -- ID of the attribute of interest, defaults to ``None``.

   :returns: :class:`dict` -- A GeoJSON file readable by GeoPandas.


.. py:function:: geodf2xarray(geodf, resolution, attr_col = None, fill = 0, projected_crs = 5070)

   Rasterize a ``geopandas.GeoDataFrame`` to ``xarray.DataArray``.

   :Parameters: * **geodf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- GeoDataFrame or GeoSeries to rasterize.
                * **resolution** (:class:`float`) -- Target resolution of the output raster in the ``projected_crs`` unit. Since
                  the default ``projected_crs`` is ``EPSG:5070``, the default unit for the
                  resolution is meters.
                * **attr_col** (:class:`str`, *optional*) -- Column name of the attribute to use as variable., defaults to ``None``,
                  i.e., the variable will be a boolean mask where 1 indicates the presence of
                  a geometry. Also, note that the attribute must be numeric and have one of the
                  following ``numpy`` types: ``int16``, ``int32``, ``uint8``, ``uint16``,
                  ``uint32``, ``float32``, and ``float64``.
                * **fill** (:class:`int` or :class:`float`, *optional*) -- Value to use for filling the missing values (mask) of the output raster,
                  defaults to ``0``.
                * **projected_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- A projected CRS to use for the output raster, defaults to ``EPSG:5070``.

   :returns: :class:`xarray.Dataset` -- The xarray Dataset with a single variable.


.. py:function:: gtiff2vrt(file_list, vrt_path)

   Create a VRT file from a list of (Geo)Tiff files.

   .. note::

       This function requires ``gdal`` to be installed.

   :Parameters: * **file_list** (:class:`list`) -- List of paths to the GeoTiff files.
                * **vrt_path** (:class:`str` or :class:`Path`) -- Path to the output VRT file.


.. py:function:: gtiff2xarray(r_dict, geometry = None, geo_crs = None, ds_dims = None, driver = None, all_touched = False, nodata = None, drop = True)

   Convert (Geo)Tiff byte responses to ``xarray.Dataset``.

   :Parameters: * **r_dict** (:class:`dict`) -- Dictionary of (Geo)Tiff byte responses where keys are some names
                  that are used for naming each responses, and values are bytes.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`, *optional*) -- The geometry to mask the data that should be in the same CRS
                  as the ``r_dict``. Defaults to ``None``.
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the input geometry, defaults to ``None``.
                  This argument should be given when ``geometry`` is given.
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to None. If None, dimension names are
                  determined from a list of common names.
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to automatic
                  detection. A list of the drivers can be found
                  `here <https://gdal.org/drivers/raster/index.html>`__.
                * **all_touched** (:class:`bool`, *optional*) -- Include a pixel in the mask if it touches any of the shapes.
                  If False (default), include a pixel only if its center is within one
                  of the shapes, or if it is selected by Bresenham's line algorithm.
                * **nodata** (:class:`float` or :class:`int`, *optional*) -- The nodata value of the raster, defaults to ``None``, i.e., it is
                  determined from the raster.
                * **drop** (:class:`bool`, *optional*) -- If True, drop the data outside of the extent of the mask geometries.
                  Otherwise, it will return the same raster with the data masked.
                  Default is True.

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataAraay` -- Requested dataset or dataarray.


.. py:function:: json2geodf(content, in_crs = 4326, crs = 4326)

   Create GeoDataFrame from (Geo)JSON.

   :Parameters: * **content** (:class:`dict` or :class:`list` of :class:`dict`) -- A (Geo)JSON dictionary or a list of them.
                * **in_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- CRS of the content, defaults to ``epsg:4326``. If the content has no CRS,
                  it will be set to this CRS, otherwise, ``in_crs`` will be ignored.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- The target CRS of the output GeoDataFrame, defaults to ``epsg:4326``.

   :returns: :class:`geopandas.GeoDataFrame` -- Generated geo-data frame from a GeoJSON


.. py:function:: xarray2geodf(da, dtype, mask_da = None, connectivity = 8)

   Vectorize a ``xarray.DataArray`` to a ``geopandas.GeoDataFrame``.

   :Parameters: * **da** (:class:`xarray.DataArray`) -- The dataarray to vectorize.
                * **dtype** (:class:`type`) -- The data type of the dataarray. Valid types are ``int16``, ``int32``,
                  ``uint8``, ``uint16``, and ``float32``.
                * **mask_da** (:class:`xarray.DataArray`, *optional*) -- The dataarray to use as a mask, defaults to ``None``.
                * **connectivity** (:class:`int`, *optional*) -- Use 4 or 8 pixel connectivity for grouping pixels into features,
                  defaults to 8.

   :returns: :class:`geopandas.GeoDataFrame` -- The vectorized dataarray.


.. py:function:: xarray_geomask(ds, geometry, crs, all_touched = False, drop = True, from_disk = False)

   Mask a ``xarray.Dataset`` based on a geometry.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry to mask the data
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- The spatial reference of the input geometry
                * **all_touched** (:class:`bool`, *optional*) -- Include a pixel in the mask if it touches any of the shapes.
                  If False (default), include a pixel only if its center is within one
                  of the shapes, or if it is selected by Bresenham's line algorithm.
                * **drop** (:class:`bool`, *optional*) -- If True, drop the data outside of the extent of the mask geometries.
                  Otherwise, it will return the same raster with the data masked.
                  Default is True.
                * **from_disk** (:class:`bool`, *optional*) -- If True, it will clip from disk using rasterio.mask.mask if possible.
                  This is beneficial when the size of the data is larger than memory.
                  Default is False.

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataArray` -- The input dataset with a mask applied (np.nan)


