:py:mod:`pynhd.network_tools`
=============================

.. py:module:: pynhd.network_tools

.. autoapi-nested-parse::

   Access NLDI and WaterData databases.



Module Contents
---------------

.. py:class:: NHDTools(flowlines)

   Prepare NHDPlus data for downstream analysis.

   .. rubric:: Notes

   Some of these tools are ported from
   `nhdplusTools <https://github.com/USGS-R/nhdplusTools>`__.

   :Parameters: **flowlines** (:class:`geopandas.GeoDataFrame`) -- NHDPlus flowlines with at least the following columns:
                ``comid``, ``lengthkm``, ``ftype``, ``terminalfl``, ``fromnode``, ``tonode``,
                ``totdasqkm``, ``startflag``, ``streamorde``, ``streamcalc``, ``terminalpa``,
                ``pathlength``, ``divergence``, ``hydroseq``, and ``levelpathi``.

   .. py:method:: add_tocomid()

      Find the downstream comid(s) of each comid in NHDPlus flowline database.

      .. rubric:: Notes

      This functions requires the following columns:
          ``comid``, ``terminalpa``, ``fromnode``, ``tonode``


   .. py:method:: check_requirements(reqs, cols)
      :staticmethod:

      Check for all the required data.

      :Parameters: * **reqs** (:term:`iterable`) -- A list of required data names (str)
                   * **cols** (:class:`list`) -- A list of variable names (str)


   .. py:method:: clean_flowlines(use_enhd_attrs, terminal2nan)

      Clean up flowlines.

      :Parameters: * **use_enhd_attrs** (:class:`bool`) -- Use attributes from the ENHD database.
                   * **terminal2nan** (:class:`bool`) -- Convert terminal flowlines to ``NaN``.


   .. py:method:: remove_isolated()

      Remove isolated flowlines.


   .. py:method:: remove_tinynetworks(min_path_size, min_path_length, min_network_size)

      Remove small paths in NHDPlus flowline database.

      .. rubric:: Notes

      This functions requires the following columns:
      ``levelpathi``, ``hydroseq``, ``totdasqkm``, ``terminalfl``, ``startflag``,
      ``pathlength``, and ``terminalpa``.

      :Parameters: * **min_network_size** (:class:`float`) -- Minimum size of drainage network in sqkm.
                   * **min_path_length** (:class:`float`) -- Minimum length of terminal level path of a network in km.
                   * **min_path_size** (:class:`float`) -- Minimum size of outlet level path of a drainage basin in km.
                     Drainage basins with an outlet drainage area smaller than
                     this value will be removed.


   .. py:method:: to_linestring()

      Convert flowlines to shapely LineString objects.



.. py:function:: enhd_flowlines_nx()

   Get a ``networkx.DiGraph`` of the entire NHD flowlines.

   .. rubric:: Notes

   The graph is directed and has the all the attributes of the flowlines
   in `ENHD <https://www.sciencebase.gov/catalog/item/63cb311ed34e06fef14f40a3>`__.
   Note that COMIDs are based on the 2020 snapshot of the NHDPlusV2.1.

   :returns: :class:`tuple` of :class:`networkx.DiGraph`, :class:`dict`, and :class:`list` -- The first element is the graph, the second element is a dictionary
             mapping the COMIDs to the node IDs in the graph, and the third element
             is a topologically sorted list of the COMIDs.


.. py:function:: flowline_resample(flw, spacing, id_col = 'comid')

   Resample a flowline based on a given spacing.

   :Parameters: * **flw** (:class:`geopandas.GeoDataFrame`) -- A dataframe with ``geometry`` and ``id_col`` columns and CRS attribute.
                  The flowlines should be able to merged to a single ``LineString``.
                  Otherwise, you should use the :func:`network_resample` function.
                * **spacing** (:class:`float`) -- Spacing between the sample points in meters.
                * **id_col** (:class:`str`, *optional*) -- Name of the flowlines column containing IDs, defaults to ``comid``.

   :returns: :class:`geopandas.GeoDataFrame` -- Resampled flowline.


.. py:function:: flowline_xsection(flw, distance, width, id_col = 'comid')

   Get cross-section of a river network at a given spacing.

   :Parameters: * **flw** (:class:`geopandas.GeoDataFrame`) -- A dataframe with ``geometry`` and ``id_col`` columns and CRS attribute.
                * **distance** (:class:`float`) -- The distance between two consecutive cross-sections.
                * **width** (:class:`float`) -- The width of the cross-section.
                * **id_col** (:class:`str`, *optional*) -- Name of the flowlines column containing IDs, defaults to ``comid``.

   :returns: :class:`geopandas.GeoDataFrame` -- A dataframe with two columns: ``geometry`` and ``comid``. The ``geometry``
             column contains the cross-section of the river network and the ``comid``
             column contains the corresponding ``comid`` from the input dataframe.
             Note that each ``comid`` can have multiple cross-sections depending on
             the given spacing distance.


.. py:function:: mainstem_huc12_nx()

   Get a ``networkx.DiGraph`` of the entire mainstem HUC12s.

   .. rubric:: Notes

   The directed graph is generated from the ``nhdplusv2wbd.csv`` file with all
   attributes that can be found in
   `Mainstem <https://www.sciencebase.gov/catalog/item/63cb38b2d34e06fef14f40ad>`__.
   Note that HUC12s are based on the 2020 snapshot of the NHDPlusV2.1.

   :returns: * :class:`networkx.DiGraph` -- The mainstem as a ``networkx.DiGraph`` with all the attributes of the
               mainstems.
             * :class:`dict` -- A mapping of the HUC12s to the node IDs in the graph.
             * :class:`list` -- A topologically sorted list of the HUC12s which strings of length 12.


.. py:function:: network_resample(flw, spacing)

   Get cross-section of a river network at a given spacing.

   :Parameters: * **flw** (:class:`geopandas.GeoDataFrame`) -- A dataframe with ``geometry`` and ``comid`` columns and CRS attribute.
                * **spacing** (:class:`float`) -- The spacing between the points.

   :returns: :class:`geopandas.GeoDataFrame` -- Resampled flowlines.


.. py:function:: network_xsection(flw, distance, width)

   Get cross-section of a river network at a given spacing.

   :Parameters: * **flw** (:class:`geopandas.GeoDataFrame`) -- A dataframe with ``geometry`` and ``comid`` columns and CRS attribute.
                * **distance** (:class:`float`) -- The distance between two consecutive cross-sections.
                * **width** (:class:`float`) -- The width of the cross-section.

   :returns: :class:`geopandas.GeoDataFrame` -- A dataframe with two columns: ``geometry`` and ``comid``. The ``geometry``
             column contains the cross-section of the river network and the ``comid``
             column contains the corresponding ``comid`` from the input dataframe.
             Note that each ``comid`` can have multiple cross-sections depending on
             the given spacing distance.


.. py:function:: nhdflw2nx(flowlines, id_col = 'comid', toid_col = 'tocomid', edge_attr = None)

   Convert NHDPlus flowline database to networkx graph.

   :Parameters: * **flowlines** (:class:`geopandas.GeoDataFrame`) -- NHDPlus flowlines.
                * **id_col** (:class:`str`, *optional*) -- Name of the column containing the node ID, defaults to "comid".
                * **toid_col** (:class:`str`, *optional*) -- Name of the column containing the downstream node ID, defaults to "tocomid".
                * **edge_attr** (:class:`str`, *optional*) -- Name of the column containing the edge attributes, defaults to ``None``.
                  If ``True``, all remaining columns will be used as edge attributes.

   :returns: :class:`nx.DiGraph` -- Networkx directed graph of the NHDPlus flowlines. Note that all elements of
             the ``toid_col`` are replaced with negative values of their corresponding
             ``id_cl`` values if they are ``NaN`` or 0. This is to ensure that the generated
             nodes in the graph are unique.


.. py:function:: nhdplus_l48(layer = None, data_dir = 'cache', **kwargs)

   Get the entire NHDPlus dataset.

   .. rubric:: Notes

   The entire NHDPlus dataset for CONUS (Lower 48) is downloaded from
   `here <https://www.epa.gov/waterdata/nhdplus-national-data>`__.
   This 7.3 GB file will take a while to download, depending on your internet
   connection. The first time you run this function, the file will be downloaded
   and stored in the ``./cache`` directory. Subsequent calls will use the cached
   file. Moreover, there are two additional dependencies required to read the
   file: ``pyogrio`` and ``py7zr``. These dependencies can be installed using
   ``pip install pyogrio py7zr`` or ``conda install -c conda-forge pyogrio py7zr``.

   :Parameters: * **layer** (:class:`str`, *optional*) -- The layer name to be returned. Either ``layer`` should be provided or
                  ``sql``. Defaults to ``None``.
                  The available layers are:

                  - ``Gage``
                  - ``BurnAddLine``
                  - ``BurnAddWaterbody``
                  - ``LandSea``
                  - ``Sink``
                  - ``Wall``
                  - ``Catchment``
                  - ``CatchmentSP``
                  - ``NHDArea``
                  - ``NHDWaterbody``
                  - ``HUC12``
                  - ``NHDPlusComponentVersions``
                  - ``PlusARPointEvent``
                  - ``PlusFlowAR``
                  - ``NHDFCode``
                  - ``DivFracMP``
                  - ``BurnLineEvent``
                  - ``NHDFlowline_Network``
                  - ``NHDFlowline_NonNetwork``
                  - ``GeoNetwork_Junctions``
                  - ``PlusFlow``
                  - ``N_1_Desc``
                  - ``N_1_EDesc``
                  - ``N_1_EStatus``
                  - ``N_1_ETopo``
                  - ``N_1_FloDir``
                  - ``N_1_JDesc``
                  - ``N_1_JStatus``
                  - ``N_1_JTopo``
                  - ``N_1_JTopo2``
                  - ``N_1_Props``
                * **data_dire** (:class:`str` or :class:`pathlib.Path`) -- Directory to store the downloaded file and use in subsequent calls,
                  defaults to ``./cache``.
                * **\*\*kwargs** -- Keyword arguments are passed to ``pyogrio.read_dataframe``.
                  For more information, visit
                  `pyogrio <https://pyogrio.readthedocs.io/en/latest/introduction.html>`__.

   :returns: :class:`geopandas.GeoDataFrame` -- A dataframe with all the NHDPlus data.


.. py:function:: prepare_nhdplus(flowlines, min_network_size, min_path_length, min_path_size = 0, purge_non_dendritic = False, remove_isolated = False, use_enhd_attrs = False, terminal2nan = True)

   Clean up and fix common issues of NHDPlus MR and HR flowlines.

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
                * **purge_non_dendritic** (:class:`bool`, *optional*) -- Whether to remove non dendritic paths, defaults to ``False``.
                * **remove_isolated** (:class:`bool`, *optional*) -- Whether to remove isolated flowlines, i.e., keep only the largest
                  connected component of the flowlines. Defaults to ``False``.
                * **use_enhd_attrs** (:class:`bool`, *optional*) -- Whether to replace the attributes with the ENHD attributes, defaults
                  to ``False``. Note that this only works for NHDPlus mid-resolution (MR) and
                  does not work for NHDPlus high-resolution (HR). For more information, see
                  `this <https://www.sciencebase.gov/catalog/item/60c92503d34e86b9389df1c9>`__.
                * **terminal2nan** (:class:`bool`, *optional*) -- Whether to replace the COMID of the terminal flowline of the network with NaN,
                  defaults to ``True``. If ``False``, the terminal COMID will be set from the
                  ENHD attributes i.e. ``use_enhd_attrs`` will be set to ``True`` which is only
                  applicable to NHDPlus mid-resolution (MR).

   :returns: :class:`geopandas.GeoDataFrame` -- Cleaned up flowlines. Note that all column names are converted to lower case.


.. py:function:: topoogical_sort(flowlines, edge_attr = None, largest_only = False, id_col = 'ID', toid_col = 'toID')

   Topological sorting of a river network.

   :Parameters: * **flowlines** (:class:`pandas.DataFrame`) -- A dataframe with columns ID and toID
                * **edge_attr** (:class:`str` or :class:`list`, *optional*) -- Names of the columns in the dataframe to be used as edge attributes, defaults to None.
                * **largest_only** (:class:`bool`, *optional*) -- Whether to return only the largest network, defaults to ``False``.
                * **id_col** (:class:`str`, *optional*) -- Name of the column containing the node ID, defaults to ``ID``.
                * **toid_col** (:class:`str`, *optional*) -- Name of the column containing the downstream node ID, defaults to ``toID``.

   :returns: :class:`(list`, dict , :class:`networkx.DiGraph)` -- A list of topologically sorted IDs, a dictionary
             with keys as IDs and values as a list of its upstream nodes,
             and the generated ``networkx.DiGraph`` object. Note that node
             IDs are associated with the input flow line IDs, but there might
             be some negative IDs in the output garph that are not present in
             the input flow line IDs. These "artificial" nodes are used to represent the
             graph outlet (the most downstream nodes) in the graph.


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


