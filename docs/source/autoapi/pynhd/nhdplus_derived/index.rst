:py:mod:`pynhd.nhdplus_derived`
===============================

.. py:module:: pynhd.nhdplus_derived

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:function:: nhd_fcode()

   Get all the NHDPlus FCodes.


.. py:function:: nhdplus_attrs(name = None, save_dir = None)

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: * **name** (:class:`str`, *optional*) -- Name of the NHDPlus attribute, defaults to None which returns a dataframe containing
                  metadata of all the available attributes in the database.
                * **save_dir** (:class:`str`, *optional*) -- Directory to save the staged data frame containing metadata for the database,
                  defaults to system's temp directory. The metadata dataframe is saved as a feather
                  file, nhdplus_attrs.feather, in save_dir that can be loaded with Pandas.

   :returns: :class:`pandas.DataFrame` -- Either a dataframe containing the database metadata or the requested attribute over CONUS.


.. py:function:: nhdplus_vaa(parquet_name = None)

   Get NHDPlus Value Added Attributes with ComID-level roughness and slope values.

   .. rubric:: Notes

   This downloads a 200 MB ``parquet`` file from
   `here <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726>`__ .
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_name** (:class:`str` or :class:`~~pathlib.Path`) -- Path to a file with ``.parquet`` extension for saving the processed to disk for
                later use.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.

   .. rubric:: Examples

   >>> vaa = nhdplus_vaa() # doctest: +SKIP
   >>> print(vaa.slope.max()) # doctest: +SKIP
   4.6


