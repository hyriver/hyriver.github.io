:py:mod:`pygeoutils.pygeoutils`
===============================

.. py:module:: pygeoutils.pygeoutils

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.



Module Contents
---------------

.. py:class:: Coordinates

   Generate validated and normalized coordinates in WGS84.

   :Parameters: * **lon** (:class:`float` or :class:`list` of :class:`floats`) -- Longitude(s) in decimal degrees.
                * **lat** (:class:`float` or :class:`list` of :class:`floats`) -- Latitude(s) in decimal degrees.
                * **bounds** (:class:`tuple` of :class:`length 4`, *optional*) -- The bounding box to check of the input coordinates fall within.
                  Defaults to WGS84 bounds.

   .. rubric:: Examples

   >>> from pygeoutils import Coordinates
   >>> c = Coordinates([460, 20, -30], [80, 200, 10])
   >>> c.points.x.tolist()
   [100.0, -30.0]

   .. py:property:: points
      :type: geopandas.GeoSeries

      Get validate coordinate as a ``geopandas.GeoSeries``.


.. py:class:: GeoBSpline(points, npts_sp, degree = 3)

   Create B-spline from a geo-dataframe of points.

   :Parameters: * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Input points as a ``GeoDataFrame`` or ``GeoSeries`` in a projected CRS.
                * **npts_sp** (:class:`int`) -- Number of points in the output spline curve.
                * **degree** (:class:`int`, *optional*) -- Degree of the spline. Should be less than the number of points and
                  greater than 1. Default is 3.

   .. rubric:: Examples

   >>> from pygeoutils import GeoBSpline
   >>> import geopandas as gpd
   >>> xl, yl = zip(
   ...     *[
   ...         (-97.06138, 32.837),
   ...         (-97.06133, 32.836),
   ...         (-97.06124, 32.834),
   ...         (-97.06127, 32.832),
   ...     ]
   ... )
   >>> pts = gpd.GeoSeries(gpd.points_from_xy(xl, yl, crs=4326))
   >>> sp = GeoBSpline(pts.to_crs("epsg:3857"), 5).spline
   >>> pts_sp = gpd.GeoSeries(gpd.points_from_xy(sp.x, sp.y, crs="epsg:3857"))
   >>> pts_sp = pts_sp.to_crs("epsg:4326")
   >>> list(zip(pts_sp.x, pts_sp.y))
   [(-97.06138, 32.837),
   (-97.06135, 32.83629),
   (-97.06131, 32.83538),
   (-97.06128, 32.83434),
   (-97.06127, 32.83319)]

   .. py:property:: spline
      :type: Spline

      Get the spline as a ``Spline`` object.


.. py:function:: arcgis2geojson(arcgis, id_attr = None)

   Convert ESRIGeoJSON format to GeoJSON.

   .. rubric:: Notes

   Based on `arcgis2geojson <https://github.com/chris48s/arcgis2geojson>`__.

   :Parameters: * **arcgis** (:class:`str` or :class:`binary`) -- The ESRIGeoJSON format str (or binary)
                * **id_attr** (:class:`str`, *optional*) -- ID of the attribute of interest, defaults to ``None``.

   :returns: :class:`dict` -- A GeoJSON file readable by GeoPandas.


.. py:function:: break_lines(lines, points, tol = 0.0)

   Break lines at specified points at given direction.

   :Parameters: * **lines** (:class:`geopandas.GeoDataFrame`) -- Lines to break at intersection points.
                * **points** (:class:`geopandas.GeoDataFrame`) -- Points to break lines at. It must contain a column named ``direction``
                  with values ``up`` or ``down``. This column is used to determine which
                  part of the lines to keep, i.e., upstream or downstream of points.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  The default is 0.0.

   :returns: :class:`geopandas.GeoDataFrame` -- Original lines except for the parts that have been broken at the specified
             points.


.. py:function:: geo2polygon(geometry, geo_crs = None, crs = None)

   Convert a geometry to a Shapely's Polygon and transform to any CRS.

   :Parameters: * **geometry** (:class:`Polygon` or :class:`tuple` of :class:`length 4`) -- Polygon or bounding box (west, south, east, north).
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- Spatial reference of the input geometry, defaults to ``None``.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`) -- Target spatial reference, defaults to ``None``.

   :returns: :class:`shapely.Polygon` or :class:`shapely.MultiPolygon` -- A (Multi)Polygon in the target CRS, if different from the input CRS.


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


.. py:function:: geometry_list(geometry)

   Get a list of polygons, points, and lines from a geometry.


.. py:function:: get_transform(ds, ds_dims = ('y', 'x'))

   Get transform of a ``xarray.Dataset`` or ``xarray.DataArray``.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **ds_dims** (:class:`tuple`, *optional*) -- Names of the coordinames in the dataset, defaults to ``("y", "x")``.
                  The order of the dimension names must be (vertical, horizontal).

   :returns: :class:`rasterio.Affine`, :class:`int`, :class:`int` -- The affine transform, width, and height


.. py:function:: gtiff2xarray(r_dict, geometry = None, geo_crs = None, ds_dims = None, driver = None, all_touched = False, nodata = None, drop = True)

   Convert (Geo)Tiff byte responses to ``xarray.Dataset``.

   :Parameters: * **r_dict** (:class:`dict`) -- Dictionary of (Geo)Tiff byte responses where keys are some names that are used
                  for naming each responses, and values are bytes.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`, *optional*) -- The geometry to mask the data that should be in the same CRS as the r_dict.
                  Defaults to ``None``.
                * **geo_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the input geometry, defaults to ``None``. This
                  argument should be given when ``geometry`` is given.
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to None. If None, dimension names are determined
                  from a list of common names.
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to automatic detection. A list of
                  the drivers can be found here: https://gdal.org/drivers/raster/index.html
                * **all_touched** (:class:`bool`, *optional*) -- Include a pixel in the mask if it touches any of the shapes.
                  If False (default), include a pixel only if its center is within one
                  of the shapes, or if it is selected by Bresenham's line algorithm.
                * **nodata** (:class:`float` or :class:`int`, *optional*) -- The nodata value of the raster, defaults to None, i.e., is determined from the raster.
                * **drop** (:class:`bool`, *optional*) -- If True, drop the data outside of the extent of the mask geometries.
                  Otherwise, it will return the same raster with the data masked.
                  Default is True.

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataAraay` -- Parallel (with dask) dataset or dataarray.


.. py:function:: json2geodf(content, in_crs = 4326, crs = 4326)

   Create GeoDataFrame from (Geo)JSON.

   :Parameters: * **content** (:class:`dict` or :class:`list` of :class:`dict`) -- A (Geo)JSON dictionary e.g., response.json() or a list of them.
                * **in_crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- CRS of the content, defaults to ``epsg:4326``.
                * **crs** (:class:`int`, :class:`str`, or :class:`pyproj.CRS`, *optional*) -- The target CRS of the output GeoDataFrame, defaults to ``epsg:4326``.

   :returns: :class:`geopandas.GeoDataFrame` -- Generated geo-data frame from a GeoJSON


.. py:function:: nested_polygons(gdf)

   Get nested polygons in a GeoDataFrame.

   :Parameters: **gdf** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- A GeoDataFrame or GeoSeries with (multi)polygons.

   :returns: :class:`dict` -- A dictionary where keys are indices of larger ploygons and
             values are a list of indices of smaller polygons that are
             contained within the larger polygons.


.. py:function:: snap2nearest(lines, points, tol)

   Find the nearest points on a line to a set of points.

   :Parameters: * **lines** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Lines.
                * **points** (:class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries`) -- Points to snap to lines.
                * **tol** (:class:`float`, *optional*) -- Tolerance for snapping points to the nearest lines in meters.
                  It must be greater than 0.0.

   :returns: :class:`geopandas.GeoDataFrame` or :class:`geopandas.GeoSeries` -- Points snapped to lines.


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


