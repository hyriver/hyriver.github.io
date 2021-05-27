:mod:`py3dep.cli`
=================

.. py:module:: py3dep.cli

.. autoapi-nested-parse::

   Command-line interface for Py3DEP.



Module Contents
---------------

.. function:: from_coords(coords: List[Tuple[float, float]], crs: str, csv_path: Union[str, Path]) -> None

   Get elevations of a set of coordinates in meter from airmap.


.. function:: from_geometry(layer: str, geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], res: float, crs: str, nc_path: Union[str, Path]) -> None

   Get topographic data from 3DEP for a geometry.


.. function:: get_target_df(tdf: Union[pd.DataFrame, gpd.GeoDataFrame], req_cols: List[str]) -> Union[pd.DataFrame, gpd.GeoDataFrame]

   Check if all required columns exists in the dataframe.

   It also re-orders the columns based on req_cols order.


.. function:: main(target: Path, target_type: str, crs: str, layer: Optional[str] = None, save_dir: Union[str, Path] = 'topo_3dep')

   Retrieve topographic data within geometries or elevations for a list of coordinates.

   TARGET: Path to a geospatial file (any file that geopandas.read_file can open) or a csv file.

   The geospatial file should have three columns:

       - id: Feature identifiers that py3dep uses as the output netcdf/csv filenames.

       - res: Target resolution in meters.

       - geometry: A Polygon or MultiPloygon.

   The csv file should have two column: x and y.

   TARGET_TYPE: Type of input file: "coords" for csv and "geometry" for geospatial.

   CRS: CRS of the input data.

   Examples:

       $ py3dep ny_coords.csv coords epsg:4326

       $ py3dep ny_geom.gpkg geometry epsg:3857 --layer "Slope Map"


