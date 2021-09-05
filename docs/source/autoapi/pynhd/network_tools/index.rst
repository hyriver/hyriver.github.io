:py:mod:`pynhd.network_tools`
=============================

.. py:module:: pynhd.network_tools

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:function:: prepare_nhdplus(flowlines, min_network_size, min_path_length, min_path_size = 0, purge_non_dendritic = False, verbose = False)

   Clean up and fix common issues of NHDPlus flowline database.

   Ported from `nhdplusTools <https://github.com/USGS-R/nhdplusTools>`__.

   :Parameters: * **flowlines** (:class:`geopandas.GeoDataFrame`) -- NHDPlus flowlines with at least the following columns:
                  ``comid``, ``lengthkm``, ``ftype``, ``terminalfl``, ``fromnode``, ``tonode``,
                  ``totdasqkm``, ``startflag``, ``streamorde``, ``streamcalc``, ``terminalpa``,
                  ``pathlength``, ``divergence``, ``hydroseq``, ``levelpathi``.
                * **min_network_size** (:class:`float`) -- Minimum size of drainage network in sqkm
                * **min_path_length** (:class:`float`) -- Minimum length of terminal level path of a network in km.
                * **min_path_size** (:class:`float`, *optional*) -- Minimum size of outlet level path of a drainage basin in km.
                  Drainage basins with an outlet drainage area smaller than
                  this value will be removed. Defaults to 0.
                * **purge_non_dendritic** (:class:`bool`, *optional*) -- Whether to remove non dendritic paths, defaults to False
                * **verbose** (:class:`bool`, *optional*) -- Whether to show a message about the removed features, defaults to True.

   :returns: :class:`geopandas.GeoDataFrame` -- Cleaned up flowlines. Note that all column names are converted to lower case.


.. py:function:: topoogical_sort(flowlines, edge_attr = None)

   Topological sorting of a river network.

   :Parameters: * **flowlines** (:class:`pandas.DataFrame`) -- A dataframe with columns ID and toID
                * **edge_attr** (:class:`str` or :class:`list`, *optional*) -- Names of the columns in the dataframe to be used as edge attributes, defaults to None.

   :returns: :class:`(list`, dict , :class:`networkx.DiGraph)` -- A list of topologically sorted IDs, a dictionary
             with keys as IDs and values as its upstream nodes,
             and the generated networkx object. Note that the
             terminal node ID is set to pd.NA.


.. py:function:: vector_accumulation(flowlines, func, attr_col, arg_cols, id_col = 'comid', toid_col = 'tocomid')

   Flow accumulation using vector river network data.

   :Parameters: * **flowlines** (:class:`pandas.DataFrame`) -- A dataframe containing comid, tocomid, attr_col and all the columns
                  that ara required for passing to ``func``.
                * **func** (:class:`function`) -- The function that routes the flow in a single river segment.
                  Positions of the arguments in the function should be as follows:
                  ``func(qin, *arg_cols)``
                  ``qin`` is computed in this function and the rest are in the order
                  of the ``arg_cols``. For example, if ``arg_cols = ["slope", "roughness"]``
                  then the functions is called this way:
                  ``func(qin, slope, roughness)``
                  where slope and roughness are elemental values read from the flowlines.
                * **attr_col** (:class:`str`) -- The column name of the attribute being accumulated in the network.
                  The column should contain the initial condition for the attribute for
                  each river segment. It can be a scalar or an array (e.g., time series).
                * **arg_cols** (:class:`list` of :class:`strs`) -- List of the flowlines columns that contain all the required
                  data for a routing a single river segment such as slope, length,
                  lateral flow, etc.
                * **id_col** (:class:`str`, *optional*) -- Name of the flowlines column containing IDs, defaults to ``comid``
                * **toid_col** (:class:`str`, *optional*) -- Name of the flowlines column containing ``toIDs``, defaults to ``tocomid``

   :returns: :class:`pandas.Series` -- Accumulated flow for all the nodes. The dataframe is sorted from upstream
             to downstream (topological sorting). Depending on the given initial
             condition in the ``attr_col``, the outflow for each river segment can be
             a scalar or an array.


