:py:mod:`pygeohydro.helpers`
============================

.. py:module:: pygeohydro.helpers

.. autoapi-nested-parse::

   Some helper function for PyGeoHydro.



Module Contents
---------------

.. py:function:: get_us_states(subset_key = None)

   Get US states as a GeoDataFrame from Census' TIGERLine 2022 database.

   :Parameters: **subset_key** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Key to subset the geometries instead of returning all states, by default
                all states are returned. Valid keys are:

                - ``contiguous`` or ``conus``
                - ``continental``
                - ``commonwealths``
                - ``territories``
                - Two letter state codes, e.g., ``["TX", "CA", "FL", ...]``

   :returns: :class:`geopandas.GeoDataFrame` -- GeoDataFrame of requested US states.


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


.. py:function:: states_lookup_table()

   Get codes and names of US states and their counties.

   .. rubric:: Notes

   This function is based on a file prepared by developers of
   an R package called `dataRetrieval <https://github.com/USGS-R/dataRetrieval>`__.

   :returns: :class:`pandas.DataFrame` -- State codes and name as a dataframe.


