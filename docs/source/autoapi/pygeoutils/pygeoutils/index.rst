:mod:`pygeoutils.pygeoutils`
============================

.. py:module:: pygeoutils.pygeoutils

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.



Module Contents
---------------

.. py:class:: MatchCRS(in_crs: str, out_crs: str)

   Reproject a geometry to another CRS.

   :Parameters: * **in_crs** (:class:`str`) -- Spatial reference of the input geometry
                * **out_crs** (:class:`str`) -- Target spatial reference

   .. method:: bounds(self, geom: Tuple[float, float, float, float]) -> Tuple[float, float, float, float]

      Reproject a bounding box to the specified output CRS.

      :Parameters: **geometry** (:class:`tuple`) -- Input bounding box (xmin, ymin, xmax, ymax).

      :returns: :class:`tuple` -- Input bounding box in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoutils import MatchCRS
      >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
      >>> MatchCRS("epsg:3857", "epsg:4326").bounds(bbox)
      (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)


   .. method:: coords(self, geom: List[Tuple[float, float]]) -> List[Tuple[Any, ...]]

      Reproject a list of coordinates to the specified output CRS.

      :Parameters: **geometry** (:class:`list` of :class:`tuple`) -- Input coords [(x1, y1), ...].

      :returns: :class:`tuple` -- Input list of coords in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoutils import MatchCRS
      >>> coords = [(-7766049.665, 5691929.739)]
      >>> MatchCRS("epsg:3857", "epsg:4326").coords(coords)
      [(-69.7636111130079, 45.44549114818127)]


   .. method:: geometry(self, geom: Union[Polygon, MultiPolygon, Point, MultiPoint]) -> Union[Polygon, MultiPolygon, Point, MultiPoint]

      Reproject a geometry to the specified output CRS.

      :Parameters: **geometry** (:class:`Polygon`, :class:`MultiPolygon`, :class:`Point`, or :class:`MultiPoint`) -- Input geometry.

      :returns: :class:`Polygon`, :class:`MultiPolygon`, :class:`Point`, or :class:`MultiPoint` -- Input geometry in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoutils import MatchCRS
      >>> from shapely.geometry import Point
      >>> point = Point(-7766049.665, 5691929.739)
      >>> MatchCRS("epsg:3857", "epsg:4326").geometry(point).xy
      (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))



.. function:: arcgis2geojson(arcgis: Dict[str, Any], id_attr: Optional[str] = None) -> Dict[str, Any]

   Convert ESRIGeoJSON format to GeoJSON.

   .. rubric:: Notes

   Based on https://github.com/chris48s/arcgis2geojson

   :Parameters: * **arcgis** (:class:`str` or :class:`binary`) -- The ESRIGeoJSON format str (or binary)
                * **id_attr** (:class:`str`) -- ID of the attribute of interest

   :returns: :class:`dict` -- A GeoJSON file readable by GeoPandas


.. function:: geo2polygon(geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], geo_crs: str, crs: str) -> Polygon

   Convert a geometry to a Shapely's Polygon and transform to any CRS.

   :Parameters: * **geometry** (:class:`Polygon` or :class:`tuple` of :class:`length 4`) -- Polygon or bounding box (west, south, east, north).
                * **geo_crs** (:class:`str`) -- Spatial reference of the input geometry
                * **crs** (:class:`str`) -- Target spatial reference.

   :returns: :class:`Polygon` -- A Polygon in the target CRS.


.. function:: get_transform(ds: Union[xr.Dataset, xr.DataArray], ds_dims: Tuple[str, str] = ('y', 'x')) -> Tuple[affine.Affine, int, int]

   Get transform of a Polygon or bounding box.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **ds_dims** (:class:`tuple`, *optional*) -- Names of the coordinames in the dataset, defaults to ("y", "x")

   :returns: :class:`affine.Affine`, :class:`int`, :class:`int` -- The affine transform, width, and height


.. function:: gtiff2file(r_dict: Dict[str, bytes], geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], geo_crs: str, output: Union[str, Path] = '.', driver: str = 'GTiff') -> None

   Save responses from ``pygeoogc.wms_bybox`` to raster file(s).

   :Parameters: * **r_dict** (:class:`dict`) -- The output of ``wms_bybox`` function.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- The geometry to mask the data that should be in the same CRS as the r_dict.
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                * **output** (:class:`str`) -- Path to a folder saving files. File names are keys of the input dictionary, so
                  each layer becomes one file. Defaults to current directory.
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to GTiff. A list of the drivers
                  can be found here: https://gdal.org/drivers/raster/index.html


.. function:: gtiff2xarray(r_dict: Dict[str, bytes], geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], geo_crs: str, ds_dims: Tuple[str, str] = ('y', 'x'), driver: str = 'GTiff') -> Union[xr.DataArray, xr.Dataset]

   Convert responses from ``pygeoogc.wms_bybox`` to ``xarray.Dataset``.

   :Parameters: * **r_dict** (:class:`dict`) -- The output of ``wms_bybox`` function.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- The geometry to mask the data that should be in the same CRS as the r_dict.
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to ("y", "x").
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to GTiff. A list of the drivers
                  can be found here: https://gdal.org/drivers/raster/index.html

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataAraay` -- The dataset or data array based on the number of variables.


.. function:: json2geodf(content: Union[List[Dict[str, Any]], Dict[str, Any]], in_crs: str = DEF_CRS, crs: str = DEF_CRS) -> gpd.GeoDataFrame

   Create GeoDataFrame from (Geo)JSON.

   :Parameters: * **content** (:class:`dict` or :class:`list` of :class:`dict`) -- A (Geo)JSON dictionary e.g., r.json() or a list of them.
                * **in_crs** (:class:`str`) -- CRS of the content, defaults to ``epsg:4326``.
                * **crs** (:class:`str`, *optional*) -- The target CRS of the output GeoDataFrame, defaults to ``epsg:4326``.

   :returns: :class:`geopandas.GeoDataFrame` -- Generated geo-data frame from a GeoJSON


.. function:: xarray_geomask(ds: Union[xr.Dataset, xr.DataArray], geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], geo_crs: str, ds_dims: Tuple[str, str] = ('y', 'x')) -> Union[xr.Dataset, xr.DataArray]

   Mask a ``xarray.Dataset`` based on a geometry.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry or bounding box to mask the data
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the dataset, default to ("y", "x").

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataArray` -- The input dataset with a mask applied (np.nan)


