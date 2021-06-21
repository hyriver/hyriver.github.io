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

      :Parameters: **geom** (:class:`tuple`) -- Input bounding box (xmin, ymin, xmax, ymax).

      :returns: :class:`tuple` -- Input bounding box in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoogc import MatchCRS
      >>> bbox = (-7766049.665, 5691929.739, -7763049.665, 5696929.739)
      >>> MatchCRS("epsg:3857", "epsg:4326").bounds(bbox)
      (-69.7636111130079, 45.44549114818127, -69.73666165448431, 45.47699468552394)


   .. method:: coords(self, geom: List[Tuple[float, float]]) -> List[Tuple[Any, ...]]

      Reproject a list of coordinates to the specified output CRS.

      :Parameters: **geom** (:class:`list` of :class:`tuple`) -- Input coords [(x1, y1), ...].

      :returns: :class:`tuple` -- Input list of coords in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoogc import MatchCRS
      >>> coords = [(-7766049.665, 5691929.739)]
      >>> MatchCRS("epsg:3857", "epsg:4326").coords(coords)
      [(-69.7636111130079, 45.44549114818127)]


   .. method:: geometry(self, geom: Union[Polygon, LineString, MultiLineString, MultiPolygon, Point, MultiPoint]) -> Union[Polygon, LineString, MultiLineString, MultiPolygon, Point, MultiPoint]

      Reproject a geometry to the specified output CRS.

      :Parameters: **geom** (:class:`LineString`, :class:`MultiLineString`, :class:`Polygon`, :class:`MultiPolygon`, :class:`Point`, or :class:`MultiPoint`) -- Input geometry.

      :returns: :class:`LineString`, :class:`MultiLineString`, :class:`Polygon`, :class:`MultiPolygon`, :class:`Point`, or :class:`MultiPoint` -- Input geometry in the specified CRS.

      .. rubric:: Examples

      >>> from pygeoogc import MatchCRS
      >>> from shapely.geometry import Point
      >>> point = Point(-7766049.665, 5691929.739)
      >>> MatchCRS("epsg:3857", "epsg:4326").geometry(point).xy
      (array('d', [-69.7636111130079]), array('d', [45.44549114818127]))



.. function:: arcgis2geojson(arcgis: Union[str, Dict[str, Any]], id_attr: Optional[str] = None) -> Dict[str, Any]

   Convert ESRIGeoJSON format to GeoJSON.

   .. rubric:: Notes

   Based on `arcgis2geojson <https://github.com/chris48s/arcgis2geojson>`__.

   :Parameters: * **arcgis** (:class:`str` or :class:`binary`) -- The ESRIGeoJSON format str (or binary)
                * **id_attr** (:class:`str`) -- ID of the attribute of interest

   :returns: :class:`dict` -- A GeoJSON file readable by GeoPandas.


.. function:: gtiff2xarray(r_dict: Dict[str, bytes], geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], geo_crs: str, ds_dims: Tuple[str, str] = ('y', 'x'), driver: str = 'GTiff') -> Union[xr.DataArray, xr.Dataset]

   Convert (Geo)Tiff byte responses to ``xarray.Dataset``.

   :Parameters: * **r_dict** (:class:`dict`) -- Dictionary of (Geo)Tiff byte responses where keys are some names that are used
                  for naming each responses, and values are bytes.
                * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple`) -- The geometry to mask the data that should be in the same CRS as the r_dict.
                * **geo_crs** (:class:`str`) -- The spatial reference of the input geometry.
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to ("y", "x").
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to GTiff. A list of the drivers
                  can be found here: https://gdal.org/drivers/raster/index.html

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataAraay` -- Parallel (with dask) dataset or dataarray.


.. function:: json2geodf(content: Union[List[Dict[str, Any]], Dict[str, Any]], in_crs: str = DEF_CRS, crs: str = DEF_CRS) -> gpd.GeoDataFrame

   Create GeoDataFrame from (Geo)JSON.

   :Parameters: * **content** (:class:`dict` or :class:`list` of :class:`dict`) -- A (Geo)JSON dictionary e.g., r.json() or a list of them.
                * **in_crs** (:class:`str`) -- CRS of the content, defaults to ``epsg:4326``.
                * **crs** (:class:`str`, *optional*) -- The target CRS of the output GeoDataFrame, defaults to ``epsg:4326``.

   :returns: :class:`geopandas.GeoDataFrame` -- Generated geo-data frame from a GeoJSON


