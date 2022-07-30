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


.. py:function:: get_nodata(src)

   Get the nodata value of a GTiff byte response.


.. py:function:: transform2tuple(transform)

   Convert an affine transform to a tuple.

   :Parameters: **transform** (:class:`rio.Affine`) -- The affine transform to be converted

   :returns: :class:`tuple` -- The affine transform as a tuple (a, b, c, d, e, f)


