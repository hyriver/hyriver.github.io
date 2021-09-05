:py:mod:`py3dep.cli`
====================

.. py:module:: py3dep.cli

.. autoapi-nested-parse::

   Command-line interface for Py3DEP.



Module Contents
---------------

.. py:function:: from_coords(coords, crs, query_source, csv_path)

   Get elevations of a set of coordinates in meter from airmap.


.. py:function:: from_geometry(layer, geometry, res, crs, nc_path)

   Get topographic data from 3DEP for a geometry.


.. py:function:: get_target_df(tdf, req_cols)

   Check if all required columns exists in the dataframe.

   It also re-orders the columns based on ``req_cols`` order.


.. py:function:: main(target, target_type, crs, query_source = 'airmap', layer = None, save_dir = 'topo_3dep')

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


