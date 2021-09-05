:py:mod:`pydaymet.cli`
======================

.. py:module:: pydaymet.cli

.. autoapi-nested-parse::

   Command-line interface for PyDaymet.



Module Contents
---------------

.. py:function:: get_target_df(tdf, req_cols)

   Check if all required columns exists in the dataframe.

   It also re-orders the columns based on req_cols order.


.. py:function:: main(target, target_type, crs, variables = None, time_scale = 'daily', pet = False, save_dir = 'clm_daymet')

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


