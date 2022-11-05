:py:mod:`pygeohydro.plot`
=========================

.. py:module:: pygeohydro.plot

.. autoapi-nested-parse::

   Plot hydrological signatures.

   Plots include daily, monthly and annual hydrograph as well as regime
   curve (monthly mean) and flow duration curve.



Module Contents
---------------

.. py:function:: prepare_plot_data(daily)

   Generae a structured data for plotting hydrologic signatures.

   :Parameters: **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame`) -- The data to be processed

   :returns: :class:`PlotDataType` -- Containing ``daily, ``mean_monthly``, ``ranked``, ``titles``,
             and ``units`` fields.


.. py:function:: signatures(discharge, precipitation = None, title = None, figsize = None, output = None, close = False)

   Plot hydrological signatures with w/ or w/o precipitation.

   Plots includes daily hydrograph, regime curve (mean monthly) and
   flow duration curve. The input discharges are converted from cms
   to mm/day based on the watershed area, if provided.

   :Parameters: * **discharge** (:class:`pd.DataFrame` or :class:`pd.Series`) -- The streamflows in mm/day. The column names are used as labels
                  on the plot and the column values should be daily streamflow.
                * **precipitation** (:class:`pd.Series`, *optional*) -- Daily precipitation time series in mm/day. If given, the data is
                  plotted on the second x-axis at the top.
                * **title** (:class:`str`, *optional*) -- The plot supertitle.
                * **figsize** (:class:`tuple`, *optional*) -- The figure size in inches, defaults to (9, 5).
                * **output** (:class:`str`, *optional*) -- Path to save the plot as png, defaults to ``None`` which means
                  the plot is not saved to a file.
                * **close** (:class:`bool`, *optional*) -- Whether to close the figure.


