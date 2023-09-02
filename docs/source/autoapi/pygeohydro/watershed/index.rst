:py:mod:`pygeohydro.watershed`
==============================

.. py:module:: pygeohydro.watershed

.. autoapi-nested-parse::

   Accessing watershed boundary-level data through web services.



Module Contents
---------------

.. py:class:: WBD(layer, outfields = '*', crs = 4326)




   Access Watershed Boundary Dataset (WBD).

   .. rubric:: Notes

   This web service offers Hydrologic Unit (HU) polygon boundaries for
   the United States, Puerto Rico, and the U.S. Virgin Islands.
   For more info visit: https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer

   :Parameters: * **layer** (:class:`str`, *optional*) -- A valid service layer. Valid layers are:

                  - ``wbdline``
                  - ``huc2``
                  - ``huc4``
                  - ``huc6``
                  - ``huc8``
                  - ``huc10``
                  - ``huc12``
                  - ``huc14``
                  - ``huc16``
                * **outfields** (:class:`str` or :class:`list`, *optional*) -- Target field name(s), default to "*" i.e., all the fields.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- Target spatial reference, default to ``EPSG:4326``.


.. py:function:: huc_wb_full(huc_lvl)

   Get the full watershed boundary for a given HUC level.

   .. rubric:: Notes

   This function is designed for cases where the full watershed boundary is needed
   for a given HUC level. If only a subset of the HUCs is needed, then use
   the ``pygeohydro.WBD`` class. The full dataset is downloaded from the National Maps'
   `WBD staged products <https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Hydrography/WBD/HU2/Shape/>`__.

   :Parameters: **huc_lvl** (:class:`int`) -- HUC level, must be even numbers between 2 and 16.

   :returns: :class:`geopandas.GeoDataFrame` -- The full watershed boundary for the given HUC level.


.. py:function:: irrigation_withdrawals()

   Get monthly water use for irrigation at HUC12-level for CONUS.

   .. rubric:: Notes

   Dataset is retrieved from https://doi.org/10.5066/P9FDLY8P.


