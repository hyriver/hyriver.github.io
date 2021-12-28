:py:mod:`pynhd.nhdplus_derived`
===============================

.. py:module:: pynhd.nhdplus_derived

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:function:: enhd_attrs(parquet_path = None, expire_after = EXPIRE, disable_caching = False)

   Get updated NHDPlus attributes from ENHD.

   .. rubric:: Notes

   This downloads a 140 MB ``parquet`` file from
   `here <https://www.sciencebase.gov/catalog/item/60c92503d34e86b9389df1c9>`__ .
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: * **parquet_path** (:class:`str` or :class:`~~pathlib.Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file, defaults to
                  ``./cache/enhd_attrs.parquet``.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.


.. py:function:: nhd_fcode()

   Get all the NHDPlus FCodes.


.. py:function:: nhdplus_attrs(name = None, parquet_path = None, expire_after = EXPIRE, disable_caching = False)

   Access NHDPlus V2.1 Attributes from ScienceBase over CONUS.

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: * **name** (:class:`str`, *optional*) -- Name of the NHDPlus attribute, defaults to None which returns a dataframe containing
                  metadata of all the available attributes in the database.
                * **parquet_path** (:class:`str` or :class:`~~pathlib.Path`, *optional*) -- Path to a file with ``.parquet`` extension for saving the processed to disk for
                  later use. Defaults to ``./cache/nhdplus_attrs.parquet``.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`pandas.DataFrame` -- Either a dataframe containing the database metadata or the requested attribute over CONUS.


.. py:function:: nhdplus_vaa(parquet_path = None, expire_after = EXPIRE, disable_caching = False)

   Get NHDPlus Value Added Attributes with ComID-level roughness and slope values.

   .. rubric:: Notes

   This downloads a 200 MB ``parquet`` file from
   `here <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726>`__ .
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: * **parquet_path** (:class:`str` or :class:`~~pathlib.Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file, defaults to
                  ``./cache/nldplus_vaa.parquet``.
                * **expire_after** (:class:`int`, *optional*) -- Expiration time for response caching in seconds, defaults to -1 (never expire).
                * **disable_caching** (:class:`bool`, *optional*) -- If ``True``, disable caching requests, defaults to False.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.

   .. rubric:: Examples

   >>> vaa = nhdplus_vaa() # doctest: +SKIP
   >>> print(vaa.slope.max()) # doctest: +SKIP
   4.6


