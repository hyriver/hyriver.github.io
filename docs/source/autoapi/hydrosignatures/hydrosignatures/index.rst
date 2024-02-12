:py:mod:`hydrosignatures.hydrosignatures`
=========================================

.. py:module:: hydrosignatures.hydrosignatures

.. autoapi-nested-parse::

   Function for computing hydrologic signature.



Module Contents
---------------

.. py:class:: HydroSignatures


   Hydrological signatures.

   :Parameters: * **q_mmpt** (:class:`pandas.Series`) -- Discharge in mm per unit time (the same timescale as precipitation).
                * **p_mmpt** (:class:`pandas.Series`) -- Precipitation in mm per unit time (the same timescale as discharge).
                * **si_method** (:class:`str`, *optional*) -- Seasonality index method. Either ``walsh`` or ``markham``. Default is ``walsh``.
                * **fdc_slope_bins** (:class:`tuple` of :class:`int`, *optional*) -- The percentage bins between 1-100 to compute the slope of FDC within it,
                  defaults to ``(33, 67)``.
                * **bfi_alpha** (:class:`float`, *optional*) -- Alpha parameter for baseflow separation filter using Lyne and Hollick method.
                  Default is ``0.925``.

   .. py:property:: signature_names
      :type: dict[str, str]

      Return a dictionary with the hydrological signatures.

   .. py:property:: values
      :type: SignaturesFloat

      Return a dictionary with the hydrological signatures.

   .. py:method:: bfi()

      Compute Baseflow Index.


   .. py:method:: diff(other)

      Compute absolute difference between two hydrological signatures.


   .. py:method:: fdc()

      Compute exceedance probability (for flow duration curve).


   .. py:method:: fdc_slope()

      Compute FDC slopes between a list of lower and upper percentiles.


   .. py:method:: isclose(other)

      Check if the signatures are close between with a tolerance of 1e-3.


   .. py:method:: mean_annual_flood()

      Compute mean annual flood.


   .. py:method:: mean_monthly()

      Compute mean monthly flow (for regime curve).


   .. py:method:: runoff_ratio()

      Compute total runoff ratio.


   .. py:method:: seasonality_index()

      Compute seasonality index.


   .. py:method:: streamflow_elasticity()

      Compute streamflow elasticity.


   .. py:method:: to_dict()

      Return a dictionary with the hydrological signatures.


   .. py:method:: to_json()

      Return a JSON string with the hydrological signatures.



.. py:function:: aridity_index(pet: pandas.Series, prcp: pandas.Series) -> numpy.float64
                 aridity_index(pet: pandas.DataFrame, prcp: pandas.DataFrame) -> pandas.Series
                 aridity_index(pet: xarray.DataArray, prcp: xarray.DataArray) -> xarray.DataArray

   Compute (Budyko) aridity index (PET/Prcp).

   :Parameters: * **pet** (:class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray`) -- Potential evapotranspiration time series. Each column can
                  correspond to PET a different location. Note that ``pet`` and ``prcp``
                  must have the same shape.
                * **prcp** (:class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray`) -- Precipitation time series. Each column can
                  correspond to PET a different location. Note that ``pet`` and ``prcp``
                  must have the same shape.

   :returns: :class:`float` or :class:`pandas.Series` or :class:`xarray.DataArray` -- The aridity index.


.. py:function:: baseflow(discharge, alpha = 0.925, n_passes = 3, pad_width = 10)

   Extract baseflow using the Lyne and Hollick filter (Ladson et al., 2013).

   :Parameters: * **discharge** (:class:`numpy.ndarray` or :class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray`) -- Discharge time series that must not have any missing values. It can also be a 2D array
                  where each row is a time series.
                * **n_passes** (:class:`int`, *optional*) -- Number of filter passes, defaults to 3. It must be an odd number greater than 3.
                * **alpha** (:class:`float`, *optional*) -- Filter parameter that must be between 0 and 1, defaults to 0.925.
                * **pad_width** (:class:`int`, *optional*) -- Padding width for extending the data from both ends to address the warm up issue.

   :returns: :class:`numpy.ndarray` or :class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray` -- Same discharge input array-like but values replaced with computed baseflow values.


.. py:function:: baseflow_index(discharge, alpha = 0.925, n_passes = 3, pad_width = 10)

   Compute the baseflow index using the Lyne and Hollick filter (Ladson et al., 2013).

   :Parameters: * **discharge** (:class:`numpy.ndarray` or :class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray`) -- Discharge time series that must not have any missing values. It can also be a 2D array
                  where each row is a time series.
                * **n_passes** (:class:`int`, *optional*) -- Number of filter passes, defaults to 3. It must be an odd number greater than 3.
                * **alpha** (:class:`float`, *optional*) -- Filter parameter that must be between 0 and 1, defaults to 0.925.
                * **pad_width** (:class:`int`, *optional*) -- Padding width for extending the data from both ends to address the warm up issue.

   :returns: :class:`numpy.float64` -- The baseflow index.


.. py:function:: exceedance(daily, threshold = 0.001)

   Compute exceedance probability from daily data.

   :Parameters: * **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame`) -- The data to be processed
                * **threshold** (:class:`float`, *optional*) -- The threshold to compute exceedance probability, defaults to 1e-3.

   :returns: :class:`pandas.Series` or :class:`pandas.DataFrame` -- Exceedance probability.


.. py:function:: extract_extrema(ts, var_name, n_pts)

   Get local extrema in a time series.

   :Parameters: * **ts** (:class:`pandas.Series`) -- Variable time series.
                * **var_name** (:class:`str`) -- Variable name.
                * **n_pts** (:class:`int`) -- Number of points to consider for detecting local extrema on both
                  sides of each point.

   :returns: :class:`pandas.DataFrame` -- A dataframe with three columns: ``var_name``, ``peak`` (bool)
             and ``trough`` (bool).


.. py:function:: flashiness_index(daily)

   Compute flashiness index from daily data following Baker et al. (2004).

   :Parameters: **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame` or :class:`numpy.ndarray` or :class:`xarray.DataArray`) -- The data to be processed

   :returns: :class:`numpy.ndarray` -- Flashiness index.

   .. rubric:: References

   Baker, D.B., Richards, R.P., Loftus, T.T. and Kramer, J.W., 2004. A new
   flashiness index: Characteristics and applications to midwestern rivers
   and streams 1. JAWRA Journal of the American Water Resources
   Association, 40(2), pp.503-522.


.. py:function:: flood_moments(streamflow)

   Compute flood moments (MAF, CV, CS) from streamflow.

   :Parameters: **streamflow** (:class:`pandas.DataFrame`) -- The streamflow data to be processed

   :returns: :class:`pandas.DataFrame` -- Flood moments; mean annual flood (MAF), coefficient
             of variation (CV), and coefficient of skewness (CS).


.. py:function:: flow_duration_curve_slope(discharge, bins, log)

   Compute FDC slopes between the given lower and upper percentiles.

   :Parameters: * **discharge** (:class:`pandas.Series` or :class:`pandas.DataFrame` or :class:`numpy.ndarray` or :class:`xarray.DataArray`) -- The discharge data to be processed.
                * **bins** (:class:`tuple` of :class:`int`) -- Percentile bins for computing FDC slopes between., e.g., (33, 67)
                  returns the slope between the 33rd and 67th percentiles.
                * **log** (:class:`bool`) -- Whether to use log-transformed data.

   :returns: :class:`numpy.ndarray` -- The slopes between the given percentiles.


.. py:function:: mean_monthly(daily, index_abbr = False, cms = False)

   Compute mean monthly summary from daily data.

   :Parameters: * **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame`) -- The data to be processed
                * **index_abbr** (:class:`bool`, *optional*) -- Whether to use abbreviated month names as index instead of
                  numbers, defaults to False.
                * **cms** (:class:`bool`, *optional*) -- Whether the input data is in cubic meters per second (cms),
                  defaults to False. If True, the mean monthly summary will be
                  computed by taking the mean of the daily data, otherwise the
                  sum of the daily data will be used.

   :returns: :class:`pandas.Series` or :class:`pandas.DataFrame` -- Mean monthly summary.


.. py:function:: rolling_mean_monthly(daily)

   Compute rolling mean monthly.


.. py:function:: seasonality_index_markham(data)

   Compute seasonality index based on Markham, 1970.


.. py:function:: seasonality_index_walsh(data)

   Compute seasonality index based on Walsh and Lawler, 1981 method.


