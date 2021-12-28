:py:mod:`pygeohydro.plot`
=========================

.. py:module:: pygeohydro.plot

.. autoapi-nested-parse::

   Plot hydrological signatures.

   Plots includes  daily, monthly and annual hydrograph as well as regime
   curve (monthly mean) and flow duration curve.



Module Contents
---------------

.. py:class:: PlotDataType



   Data structure for plotting hydrologic signatures.


.. py:function:: cover_legends()

   Colormap (cmap) and their respective values (norm) for land cover data legends.


.. py:function:: descriptor_legends()

   Colormap (cmap) and their respective values (norm) for land cover data legends.


.. py:function:: exceedance(daily)

   Compute Flow duration (rank, sorted obs).


.. py:function:: prepare_plot_data(daily)

   Generae a structured data for plotting hydrologic signatures.

   :Parameters: **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame`) -- The data to be processed

   :returns: :class:`PlotDataType` -- Containing ``daily, ``monthly``, ``annual``, ``mean_monthly``, ``ranked`` fields.


.. py:function:: signatures(daily, precipitation = None, title = None, title_ypos = 1.02, figsize = (14, 13), threshold = 0.001, output = None)

   Plot hydrological signatures with w/ or w/o precipitation.

   Plots includes daily, monthly and annual hydrograph as well as
   regime curve (mean monthly) and flow duration curve. The input
   discharges are converted from cms to mm/day based on the watershed
   area, if provided.

   :Parameters: * **daily** (:class:`pd.DataFrame` or :class:`pd.Series`) -- The streamflows in mm/day. The column names are used as labels
                  on the plot and the column values should be daily streamflow.
                * **precipitation** (:class:`pd.Series`, *optional*) -- Daily precipitation time series in mm/day. If given, the data is
                  plotted on the second x-axis at the top.
                * **title** (:class:`str`, *optional*) -- The plot supertitle.
                * **title_ypos** (:class:`float`) -- The vertical position of the plot title, default to 1.02
                * **figsize** (:class:`tuple`, *optional*) -- Width and height of the plot in inches, defaults to (14, 13) inches.
                * **threshold** (:class:`float`, *optional*) -- The threshold for cutting off the discharge for the flow duration
                  curve to deal with log 0 issue, defaults to :math:`1^{-3}` mm/day.
                * **output** (:class:`str`, *optional*) -- Path to save the plot as png, defaults to ``None`` which means
                  the plot is not saved to a file.


