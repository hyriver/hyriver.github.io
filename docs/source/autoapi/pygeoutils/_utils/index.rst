:orphan:

:py:mod:`pygeoutils._utils`
===========================

.. py:module:: pygeoutils._utils

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.



Module Contents
---------------

.. py:class:: Attrs



   Attributes of a GTiff byte response.


.. py:class:: Convert

   Functions to Convert an ArcGIS JSON object to a GeoJSON object.

   .. py:method:: attributes(arcgis, geojson)

      Get the attributes from an ArcGIS JSON object.


   .. py:method:: coords(arcgis, geojson)

      Get the bounds from an ArcGIS JSON object.


   .. py:method:: features(arcgis, geojson)

      Get the features from an ArcGIS JSON object.


   .. py:method:: geometry(arcgis, geojson)
      :staticmethod:

      Get the geometry from an ArcGIS JSON object.


   .. py:method:: get_outer_rings(rings)
      :staticmethod:

      Get outer rings and holes in a list of rings.


   .. py:method:: get_uncontained_holes(outer_rings, holes)
      :staticmethod:

      Get all the uncontstrained holes.


   .. py:method:: isnumber(nums)
      :staticmethod:

      Check if all items in a list are numbers.


   .. py:method:: paths(arcgis, geojson)
      :staticmethod:

      Get the paths from an ArcGIS JSON object.


   .. py:method:: points(arcgis, geojson)
      :staticmethod:

      Get the points from an ArcGIS JSON object.


   .. py:method:: rings(arcgis, _)

      Get the rings from an ArcGIS JSON object.


   .. py:method:: xy(arcgis, geojson)

      Get the xy coordinates from an ArcGIS JSON object.



.. py:function:: convert(arcgis, id_attr = None)

   Convert an ArcGIS JSON object to a GeoJSON object.


.. py:function:: get_bounds(ds, ds_dims = ('y', 'x'))

   Get bounds of a ``xarray.Dataset`` or ``xarray.DataArray``.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **ds_dims** (:class:`tuple`, *optional*) -- Names of the coordinames in the dataset, defaults to ``("y", "x")``.
                  The order of the dimension names must be (vertical, horizontal).

   :returns: :class:`tuple` -- The bounds in the order of (left, bottom, right, top)


.. py:function:: get_dim_names(ds)

   Get vertical and horizontal dimension names.


.. py:function:: get_gtiff_attrs(resp, ds_dims = None, driver = None, nodata = None)

   Get nodata, CRS, and dimension names in (vertical, horizontal) order from raster in bytes.

   :Parameters: * **resp** (:class:`bytes`) -- Raster response returned from a wed service request such as WMS
                * **ds_dims** (:class:`tuple` of :class:`str`, *optional*) -- The names of the vertical and horizontal dimensions (in that order)
                  of the target dataset, default to None. If None, dimension names are determined
                  from a list of common names.
                * **driver** (:class:`str`, *optional*) -- A GDAL driver for reading the content, defaults to automatic detection. A list of
                  the drivers can be found here: https://gdal.org/drivers/raster/index.html
                * **nodata** (:class:`float` or :class:`int`, *optional*) -- The nodata value of the raster, defaults to None, i.e., is determined from the raster.

   :returns: :class:`Attrs` -- No data, CRS, and dimension names for vertical and horizontal directions or
             a list of the existing dimensions if they are not in a list of common names.


.. py:function:: get_nodata(src)

   Get the nodata value of a GTiff byte response.


.. py:function:: transform2tuple(transform)

   Convert an affine transform to a tuple.

   :Parameters: **transform** (:class:`rio.Affine`) -- The affine transform to be converted

   :returns: :class:`tuple` -- The affine transform as a tuple (a, b, c, d, e, f)


.. py:function:: write_crs(ds)

   Write geo reference info into a dataset or dataarray.


