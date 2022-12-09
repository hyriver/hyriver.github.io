:py:mod:`pynhd.nhdplus_derived`
===============================

.. py:module:: pynhd.nhdplus_derived

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:function:: enhd_attrs(parquet_path = None)

   Get updated NHDPlus attributes from ENHD.

   .. rubric:: Notes

   This downloads a 160 MB ``parquet`` file from
   `here <https://www.sciencebase.gov/catalog/item/60c92503d34e86b9389df1c9>`__.
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_path** (:class:`str` or :class:`~~Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file, defaults to
                ``./cache/enhd_attrs.parquet``.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.


.. py:function:: epa_nhd_catchments(comids, feature)

   Get NHDPlus catchment-scale data from EPA's HMS REST API.

   .. rubric:: Notes

   For more information about curve number please refer to the project's
   webpage on the EPA's
   `website <https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CEMM&dirEntryId=351307>`__.

   :Parameters: * **comids** (:class:`int` or :class:`list` of :class:`int`) -- ComID(s) of NHDPlus catchments.
                * **feature** (:class:`str`) -- The feature of interest. Available options are:

                  - ``catchment_metrics``: 414 catchment-scale metrics.
                  - ``curve_number``: 16-day average Curve Number.
                  - ``comid_info``: ComID information.

   :returns: :class:`dict` of :class:`pandas.DataFrame` or :class:`geopandas.GeoDataFrame` -- A dict of the requested dataframes. A ``comid_info`` dataframe is
             always returned.

   .. rubric:: Examples

   >>> import pynhd
   >>> data = nhd.epa_nhd_catchments(1440291, "catchment_metrics")
   >>> data["catchment_metrics"].loc[1440291, "AvgWetIndxCat"]
   579.532


.. py:function:: nhd_fcode()

   Get all the NHDPlus FCodes.


.. py:function:: nhdplus_attrs(attr_name = None)

   Stage the NHDPlus Attributes database and save to nhdplus_attrs.parquet.

   .. rubric:: Notes

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: **attr_names** (*str , *optional**) -- Name of NHDPlus attribute to return, defaults to None, i.e.,
                only return a metadata dataframe that includes the attribute names
                and their description and units.

   :returns: :class:`pandas.DataFrame` -- The staged data as a DataFrame.


.. py:function:: nhdplus_attrs_s3(attr_names = None, nodata = False)

   Access NHDPlus V2.1 derived attributes over CONUS.

   .. rubric:: Notes

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.

   :Parameters: * **attr_names** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Names of NHDPlus attribute(s) to return, defaults to None, i.e.,
                  only return a metadata dataframe that includes the attribute names
                  and their description and units.
                * **nodata** (:class:`bool`) -- Whether to include NODATA percentages, default is False.

   :returns: :class:`pandas.DataFrame` -- A dataframe of requested NHDPlus attributes.


.. py:function:: nhdplus_vaa(parquet_path = None)

   Get NHDPlus Value Added Attributes with ComID-level roughness and slope values.

   .. rubric:: Notes

   This function downloads a 245 MB ``parquet`` file from
   `here <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726>`__ .
   Although this dataframe does not include geometry, it can be linked to other geospatial
   NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_path** (:class:`str` or :class:`~~Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file, defaults to
                ``./cache/nldplus_vaa.parquet``.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million NHDPlus flowlines.

   .. rubric:: Examples

   >>> vaa = nhdplus_vaa() # doctest: +SKIP
   >>> print(vaa.slope.max()) # doctest: +SKIP
   4.6


