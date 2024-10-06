hydrosignatures.baseflow
========================

.. py:module:: hydrosignatures.baseflow

.. autoapi-nested-parse::

   Function for computing hydrologic signature.





Module Contents
---------------

.. py:function:: baseflow(discharge, alpha = 0.925, n_passes = 1, pad_width = 10)

   Extract baseflow using the Lyne and Hollick filter (Ladson et al., 2013).

   :Parameters: * **discharge** (:class:`numpy.ndarray` or :class:`pandas.DataFrame` or :class:`pandas.Series` or :class:`xarray.DataArray`) -- Discharge time series that must not have any missing values. It can also be a 2D array
                  where each row is a time series.
                * **n_passes** (:class:`int`, *optional*) -- Number of filter passes, defaults to 1.
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


.. py:function:: baseflow_recession(streamflow, freq = 1.0, recession_length = 15, n_start = 0, eps = 0, start_of_recession = 'baseflow', fit_method = 'nonparametric_analytic', lyne_hollick_smoothing = 0.925)

   Calculate baseflow recession constant and master recession curve.

   .. rubric:: Notes

   This function is ported from the TOSSH Matlab toolbox, which is based on the
   following publication:

   Gnann, S.J., Coxon, G., Woods, R.A., Howden, N.J.K., McMillan H.K., 2021.
   TOSSH: A Toolbox for Streamflow Signatures in Hydrology.
   Environmental Modelling & Software.
   https://doi.org/10.1016/j.envsoft.2021.104983

   This function calculates baseflow recession constant assuming exponential
   recession behaviour (Safeeq et al., 2013). Master recession curve (MRC) is
   constructed using the adapted matching strip method (Posavec et al.,
   2006).

   According to Safeeq et al. (2013), :math:`K < 0.065` represent groundwater
   dominated slow-draining systems, :math:`K >= 0.065` represent shallow subsurface
   flow dominated fast draining systems.

   :Parameters: * **streamflow** (:class:`numpy.ndarray`) -- Streamflow as a 1D array.
                * **freq** (:class:`float`, *optional*) -- Frequency of steamflow in number of days. Default is 1, i.e., daily streamflow.
                * **recession_length** (:class:`int`, *optional*) -- Minimum length of recessions [days]. Default is 15.
                * **n_start** (:class:`int`, *optional*) -- Days to be removed after start of recession. Default is 0.
                * **eps** (:class:`float`, *optional*) -- Allowed increase in flow during recession period. Default is 0.
                * **start_of_recession** (``{'baseflow', 'peak'}``, *optional*) -- Define start of recession. Default is 'baseflow'.
                * **fit_method** (``{'nonparametric_analytic', 'exponential'}``, *optional*) -- Method to fit mrc. Default is 'nonparametric_analytic'.
                * **lyne_hollick_smoothing** (:class:`float`, *optional*) -- Smoothing parameter of Lyne-Hollick filter. Default is 0.925.

   :returns: * **mrc** (:class:`numpy.ndarray`) -- Master Recession Curve as 2D array of [time, flow].
             * **bf_recession_k** (:class:`float`) -- Baseflow Recession Constant [1/day].

   :raises ValueError: If no recession segments are found or if a complex BaseflowRecessionK is calculated.


