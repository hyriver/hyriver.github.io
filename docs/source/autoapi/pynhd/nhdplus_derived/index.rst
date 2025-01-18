pynhd.nhdplus_derived
=====================

.. py:module:: pynhd.nhdplus_derived

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.







Module Contents
---------------

.. py:class:: StreamCat(lakes_only = False)

   Get StreamCat API's properties.

   :Parameters: **lakes_only** (:class:`bool`, *optional*) -- If ``True``, only return metrics for lakes and their associated catchments
                from the LakeCat dataset.

   .. attribute:: base_url

      The base URL of the API.

      :type: :class:`str`

   .. attribute:: valid_names

      The valid names of the metrics.

      :type: :class:`list` of :class:`str`

   .. attribute:: alt_names

      The alternative names of some metrics.

      :type: :class:`dict` of :class:`str`

   .. attribute:: valid_regions

      The valid hydro regions.

      :type: :class:`list` of :class:`str`

   .. attribute:: valid_states

      The valid two letter states' abbreviations.

      :type: :class:`pandas.DataFrame`

   .. attribute:: valid_counties

      The valid counties' FIPS codes.

      :type: :class:`pandas.DataFrame`

   .. attribute:: valid_aois

      The valid types of areas of interest.

      :type: :class:`list` of :class:`str`

   .. attribute:: metrics_df

      The metrics' metadata such as description and units.

      :type: :class:`pandas.DataFrame`

   .. attribute:: valid_years

      A dictionary of the valid years for annual metrics.

      :type: :class:`dict`


.. py:function:: enhd_attrs(parquet_path = None)

   Get updated NHDPlus attributes from ENHD V2.0.

   .. rubric:: Notes

   This function downloads a 160 MB ``parquet`` file from
   `here <https://doi.org/10.5066/P976XCVT>`__.
   Although this dataframe does not include geometry, it can be
   linked to other geospatial NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_path** (:class:`str` or :class:`pathlib.Pathlib.Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file,
                defaults to ``./cache/enhd_attrs.parquet``.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for
             2.7 million NHDPlus flowlines.


.. py:function:: epa_nhd_catchments(comids, feature)

   Get NHDPlus catchment-scale data from EPA's HMS REST API.

   .. rubric:: Notes

   For more information about curve number please refer to the project's
   webpage on the EPA's
   `website <https://cfpub.epa.gov/si/si_public_record_Report.cfm?Lab=CEMM&dirEntryId=351307>`__.

   :Parameters: * **comids** (:class:`int` or :class:`list` of :class:`int`) -- ComID(s) of NHDPlus catchments.
                * **feature** (:class:`str`) -- The feature of interest. Available options are:

                  - ``curve_number``: 16-day average Curve Number.
                  - ``comid_info``: ComID information.

   :returns: :class:`dict` of :class:`pandas.DataFrame` or :class:`geopandas.GeoDataFrame` -- A dict of the requested dataframes. A ``comid_info`` dataframe is
             always returned.

   .. rubric:: Examples

   >>> import pynhd
   >>> data = pynhd.epa_nhd_catchments(9533477, "curve_number")
   >>> data["curve_number"].mean(axis=1).item()
   75.576


.. py:function:: nhd_fcode()

   Get all the NHDPlus FCodes.


.. py:function:: nhdplus_attrs(attr_name = None)

   Stage the NHDPlus Attributes database and save to nhdplus_attrs.parquet.

   .. rubric:: Notes

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`__.

   :Parameters: **attr_names** (*str , *optional**) -- Name of NHDPlus attribute to return, defaults to None, i.e.,
                only return a metadata dataframe that includes the attribute names
                and their description and units.

   :returns: :class:`pandas.DataFrame` -- The staged data as a DataFrame.


.. py:function:: nhdplus_attrs_s3(attr_names = None, pyarrow_filter = None, nodata = False)

   Access NHDPlus V2.1 derived attributes over CONUS.

   .. rubric:: Notes

   More info can be found `here <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`__.

   :Parameters: * **attr_names** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Names of NHDPlus attribute(s) to return, defaults to None, i.e.,
                  only return a metadata dataframe that includes the attribute names
                  and their description and units.
                * **pyarrow_filter** (:class:`pyarrow.compute.Expression`, *optional*) -- A filter expression to apply to the dataset, defaults to None. Please
                  refer to the PyArrow documentation for more information
                  `here <https://arrow.apache.org/docs/python/generated/pyarrow.dataset.Expression.html>`__.
                * **nodata** (:class:`bool`) -- Whether to include NODATA percentages, default is False.

   :returns: :class:`pandas.DataFrame` -- A dataframe of requested NHDPlus attributes.


.. py:function:: nhdplus_h12pp(gpkg_path = None)

   Access HUC12 Pour Points for NHDPlus V2.1 L48 (CONUS).

   .. rubric:: Notes

   More info can be found
   `here <https://www.sciencebase.gov/catalog/item/60cb5edfd34e86b938a373f4>`__.

   :Parameters: **gpkg_path** (:class:`str` or :class:`pathlib.Pathlib.Path`, *optional*) -- Path to the geopackage file, defaults to None, i.e., download
                the file to the cache directory as ``102020wbd_outlets.gpkg``.

   :returns: :class:`geopandas.GeoDataFrame` -- A geodataframe of HUC12 pour points.


.. py:function:: nhdplus_vaa(parquet_path = None)

   Get NHDPlus Value Added Attributes including roughness.

   .. rubric:: Notes

   This function downloads a 245 MB ``parquet`` file from
   `here <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726>`__.
   Although this dataframe does not include geometry, it can be linked
   to other geospatial NHDPlus dataframes through ComIDs.

   :Parameters: **parquet_path** (:class:`str` or :class:`pathlib.Pathlib.Path`, *optional*) -- Path to a file with ``.parquet`` extension for storing the file, defaults to
                ``./cache/nldplus_vaa.parquet``.

   :returns: :class:`pandas.DataFrame` -- A dataframe that includes ComID-level attributes for 2.7 million
             NHDPlus flowlines.


.. py:function:: streamcat(metric_names = None, metric_areas = None, comids = None, regions = None, states = None, counties = None, conus = False, percent_full = False, area_sqkm = False, lakes_only = False)

   Get various metrics for NHDPlusV2 catchments from EPA's StreamCat.

   .. rubric:: Notes

   For more information about the service check its webpage
   at https://www.epa.gov/national-aquatic-resource-surveys/streamcat-dataset.

   :Parameters: * **metric_names** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Metric name(s) to retrieve. There are 567 metrics available.
                  to get a full list check out :meth:`StreamCat.valid_names`.
                  To get a description of each metric, check out
                  :meth:`StreamCat.metrics_df`. Some metrics require year and/or slope
                  to be specified, which have ``[Year]`` and/or ``[Slope]`` in their name.
                  For convenience all these variables and their years/slopes are converted
                  to a dict that can be accessed via :meth:`StreamCat.valid_years` and
                  :meth:`StreamCat.valid_slopes`. Defaults to ``None``, which will return
                  a dataframe of the metrics metadata.
                * **metric_areas** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Areas to return the metrics for, defaults to ``None``, i.e. all areas.
                  Valid options are: ``cat`` for catchment, ``catrp100`` for 100-m riparian
                  catchment, ``ws`` for watershed, ``wsrp100`` for 100-m riparian watershed,
                * **comids** (:class:`int` or :class:`list` of :class:`int`, *optional*) -- NHDPlus COMID(s), defaults to ``None``. Either ``comids``, ``regions``,
                  ``states``, ``counties``, or ``conus`` must be passed. They are
                  mutually exclusive.
                * **regions** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Hydro region(s) to retrieve metrics for, defaults to ``None``. For a
                  full list of valid regions check out :meth:`StreamCat.valid_regions`
                  Either ``comids``, ``regions``, ``states``, ``counties``, or ``conus``
                  must be passed. They are mutually exclusive.
                * **states** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- Two letter state abbreviation(s) to retrieve metrics for, defaults to
                  ``None``. For a full list of valid states check out
                  :meth:`StreamCat.valid_states` Either ``comids``, ``regions``,
                  ``states``, ``counties``, or ``conus`` must be passed. They are
                  mutually exclusive.
                * **counties** (:class:`str` or :class:`list` of :class:`str`, *optional*) -- County FIPS codes(s) to retrieve metrics for, defaults to ``None``. For
                  a full list of valid county codes check out :meth:`StreamCat.valid_counties`
                  Either ``comids``, ``regions``, ``states``, ``counties``, or ``conus`` must
                  be passed. They are mutually exclusive.
                * **conus** (:class:`bool`, *optional*) -- If ``True``, ``metric_names`` of all NHDPlus COMIDs are retrieved,
                  defaults ``False``. Either ``comids``, ``regions``,
                  ``states``, ``counties``, or ``conus`` must be passed. They are mutually
                  exclusive.
                * **percent_full** (:class:`bool`, *optional*) -- If ``True``, return the percent of each area of interest covered by
                  the metric.
                * **area_sqkm** (:class:`bool`, *optional*) -- If ``True``, return the area in square kilometers.
                * **lakes_only** (:class:`bool`, *optional*) -- If ``True``, only return metrics for lakes and their associated catchments
                  from the LakeCat dataset.

   :returns: :class:`pandas.DataFrame` -- A dataframe with the requested metrics.


