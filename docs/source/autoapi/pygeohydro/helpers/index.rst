:mod:`pygeohydro.helpers`
=========================

.. py:module:: pygeohydro.helpers

.. autoapi-nested-parse::

   Some helper function for PyGeoHydro.



Module Contents
---------------

.. function:: nlcd_helper() -> Dict[str, Any]

   Get legends and properties of the NLCD cover dataset.

   .. rubric:: Notes

   The following references have been used:
       - https://github.com/jzmiller1/nlcd
       - https://www.mrlc.gov/data-services-page
       - https://www.mrlc.gov/data/legends/national-land-cover-database-2016-nlcd2016-legend

   :returns: :class:`dict` -- Years where data is available and cover classes and categories, and roughness estimations.


.. function:: nwis_errors() -> pd.DataFrame

   Get error code lookup table for USGS sites that have daily values.


