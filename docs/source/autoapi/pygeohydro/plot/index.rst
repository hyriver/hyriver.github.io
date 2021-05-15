:mod:`pygeohydro.plot`
======================

.. py:module:: pygeohydro.plot

.. autoapi-nested-parse::

   Plot hydrological signatures.

   Plots includes  daily, monthly and annual hydrograph as well as regime
   curve (monthly mean) and flow duration curve.



Module Contents
---------------

.. py:class:: PlotDataType



   Data structure for plotting hydrologic signatures.


.. function:: cover_legends() -> Tuple[ListedColormap, BoundaryNorm, List[float]]

   Colormap (cmap) and their respective values (norm) for land cover data legends.


.. function:: exceedance(daily: Union[pd.DataFrame, pd.Series]) -> Union[pd.DataFrame, pd.Series]

   Compute Flow duration (rank, sorted obs).


.. function:: prepare_plot_data(daily: Union[pd.DataFrame, pd.Series]) -> PlotDataType

   Generae a structured data for plotting hydrologic signatures.

   :Parameters: **daily** (:class:`pandas.Series` or :class:`pandas.DataFrame`) -- The data to be processed

   :returns: :class:`PlotDataType` -- Containing ``daily, ``monthly``, ``annual``, ``mean_monthly``, ``ranked`` fields.


.. function:: signatures(daily: Union[pd.DataFrame, pd.Series], precipitation: Optional[pd.Series] = None, title: Optional[str] = None, title_ypos: float = 1.02, figsize: Tuple[int, int] = (14, 13), threshold: float = 0.001, output: Optional[Union[str, Path]] = None) -> None

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


