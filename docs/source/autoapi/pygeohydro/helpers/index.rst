:py:mod:`pygeohydro.helpers`
============================

.. py:module:: pygeohydro.helpers

.. autoapi-nested-parse::

   Some helper function for PyGeoHydro.



Module Contents
---------------

.. py:function:: nlcd_helper()

   Get legends and properties of the NLCD cover dataset.

   .. rubric:: Notes

   The following references have been used:
       - https://github.com/jzmiller1/nlcd
       - https://www.mrlc.gov/data-services-page
       - https://www.mrlc.gov/data/legends/national-land-cover-database-2016-nlcd2016-legend
       - https://doi.org/10.1111/jfr3.12347

   :returns: :class:`dict` -- Years where data is available and cover classes and categories, and roughness estimations.


.. py:function:: nwis_errors()

   Get error code lookup table for USGS sites that have daily values.


