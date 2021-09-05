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
                * **id_attr** (:class:`str`) -- ID of the attribute of interest

   :returns: :class:`dict` -- A GeoJSON file readable by GeoPandas.


.. py:function:: geo2polygon(geometry, geo_crs, crs)

   Convert a geometry to a Shapely's Polygon and transform to any CRS.

   :Parameters: * **geometry** (:class:`Polygon` or :class:`tuple` of :class:`length 4`) -- Polygon or bounding box (west, south, east, north).
                * **geo_crs** (:class:`str`) -- Spatial reference of the input geometry
                * **crs** (:class:`str`) -- Target spatial reference.

   :returns: :class:`Polygon` -- A Polygon in the target CRS.


.. py:function:: get_transform(ds, ds_dims = ('y', 'x'))

   Get transform of a ``xarray.Dataset`` or ``xarray.DataArray``.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **ds_dims** (:class:`tuple`, *optional*) -- Names of the coordinames in the dataset, defaults to ``("y", "x")``.

   :returns: :class:`affine.Affine`, :class:`int`, :class:`int` -- The affine transform, width, and height


.. py:function:: gtiff2xarray(r_dict, geometry, geo_crs, ds_dims = None, driver = None, all_touched = False)

   Convert (Geo)Tiff byte responses to ``xarray.Dataset``.

   :Parameters: * **r_dict** (:class:`dict`) -- Dictionary of (Geo)Tiff byte responses where keys are some names that are used
                  for naming each responses, and values are bytes.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- The geometry to mask the data that should be in the same CRS as the r_dict.
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to None. If None, dimension names are determined
                  from a list of common names.
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to automatic detection. A list of
                  the drivers can be found here: https://gdal.org/drivers/raster/index.html
                * **all_touched** (:class:`bool`, *optional*) -- Include a pixel in the mask if it touches any of the shapes.
                  If False (default), include a pixel only if its center is within one
                  of the shapes, or if it is selected by Bresenham’s line algorithm.

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataAraay` -- Parallel (with dask) dataset or dataarray.


.. py:function:: json2geodf(content, in_crs = DEF_CRS, crs = DEF_CRS)

   Create GeoDataFrame from (Geo)JSON.

   :Parameters: * **content** (:class:`dict` or :class:`list` of :class:`dict`) -- A (Geo)JSON dictionary e.g., r.json() or a list of them.
                * **in_crs** (:class:`str`) -- CRS of the content, defaults to ``epsg:4326``.
                * **crs** (:class:`str`, *optional*) -- The target CRS of the output GeoDataFrame, defaults to ``epsg:4326``.

   :returns: :class:`geopandas.GeoDataFrame` -- Generated geo-data frame from a GeoJSON


.. py:function:: xarray_geomask(ds, geometry, geo_crs, ds_dims = None, all_touched = False)

   Mask a ``xarray.Dataset`` based on a geometry.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry or bounding box to mask the data
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to None. If None, dimension names are determined
                  from a list of common names.
                * **all_touched** (:class:`bool`, *optional*) -- Include a pixel in the mask if it touches any of the shapes.
                  If False (default), include a pixel only if its center is within one
                  of the shapes, or if it is selected by Bresenham’s line algorithm.

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataArray` -- The input dataset with a mask applied (np.nan)


