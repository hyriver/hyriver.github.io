:orphan:

:py:mod:`pygeoutils._utils`
===========================

.. py:module:: pygeoutils._utils

.. autoapi-nested-parse::

   Some utilities for manipulating GeoSpatial data.



Module Contents
---------------

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


.. py:function:: get_transform(ds, ds_dims = ('y', 'x'))

   Get transform of a ``xarray.Dataset`` or ``xarray.DataArray``.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- The dataset(array) to be masked
                * **ds_dims** (:class:`tuple`, *optional*) -- Names of the coordinames in the dataset, defaults to ``("y", "x")``.
                  The order of the dimension names must be (vertical, horizontal).

   :returns: :class:`rasterio.Affine`, :class:`int`, :class:`int` -- The affine transform, width, and height


.. py:function:: transform2tuple(transform)

   Convert an affine transform to a tuple.

   :Parameters: **transform** (:class:`rio.Affine`) -- The affine transform to be converted

   :returns: :class:`tuple` -- The affine transform as a tuple (a, b, c, d, e, f)


.. py:function:: xd_write_crs(ds, crs = None, grid_mapping_name = None)

   Write geo reference info into a dataset or dataarray.

   :Parameters: * **ds** (:class:`xarray.Dataset` or :class:`xarray.DataArray`) -- Input dataset(array)
                * **crs** (:class:`pyproj.CRS` or :class:`str` or :class:`int`, *optional*) -- Target CRS to be written, defaults to ``ds.rio.crs``
                * **grid_mapping_name** (:class:`str`, *optional*) -- Target grid mapping, defaults to ``ds.rio.grid_mapping``

   :returns: :class:`xarray.Dataset` or :class:`xarray.DataArray` -- The dataset(array) with CRS info written.


