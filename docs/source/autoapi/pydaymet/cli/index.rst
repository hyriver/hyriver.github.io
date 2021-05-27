:mod:`pydaymet.cli`
===================

.. py:module:: pydaymet.cli

.. autoapi-nested-parse::

   Command-line interface for PyDaymet.



Module Contents
---------------

.. function:: get_target_df(tdf: Union[pd.DataFrame, gpd.GeoDataFrame], req_cols: List[str]) -> Union[pd.DataFrame, gpd.GeoDataFrame]

   Check if all required columns exists in the dataframe.

   It also re-orders the columns based on req_cols order.


.. function:: main(target: Path, target_type: str, crs: str, variables: Optional[Union[List[str], str]] = None, time_scale: str = 'daily', pet: bool = False, save_dir: Union[str, Path] = 'clm_daymet')

   Retrieve cliamte data within geometries or elevations for a list of coordinates.

   TARGET: Path to a geospatial file (any file that geopandas.read_file can open) or a csv file.

   The input files should have three columns:

       - id: Feature identifiers that daymet uses as the output netcdf filenames.

       - start: Starting time.

       - end: Ending time.

       - region: Target region (na for CONUS, hi for Hawaii, and pr for Puerto Rico.

   If target_type is geometry, an additional geometry column is required.
   If it is coords, two additional columns are needed: x and y.

   TARGET_TYPE: Type of input file: "coords" for csv and "geometry" for geospatial.

   CRS: CRS of the input data.

   Examples:

       $ pydaymet ny_coords.csv coords epsg:4326 -v prcp -v tmin -p -t monthly

       $ pydaymet ny_geom.gpkg geometry epsg:3857 -v prcp


