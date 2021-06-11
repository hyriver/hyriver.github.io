:mod:`pygeohydro.pygeohydro`
============================

.. py:module:: pygeohydro.pygeohydro

.. autoapi-nested-parse::

   Accessing data from the supported databases through their APIs.



Module Contents
---------------

.. py:class:: NID

   Retrieve data from the National Inventory of Dams.

   .. method:: get_attrs(self, variables: List[str]) -> Dict[str, str]

      Get descriptions of the NID variables.


   .. method:: get_codes(self) -> str

      Get the definitions of letter codes in NID database.


   .. method:: get_xlsx(self) -> io.BytesIO

      Get the excel file that contains the dam data.



.. py:class:: NWIS

   Access NWIS web service.

   .. method:: get_info(self, queries: Union[Dict[str, str], List[Dict[str, str]]], expanded: bool = False) -> pd.DataFrame

      Send multiple queries to USGS Site Web Service.

      :Parameters: * **queries** (:class:`dict` or :class:`list` of :class:`dict`) -- A single or a list of valid queries.
                   * **expanded** (:class:`bool`, *optional*) -- Whether to get expanded sit information for example drainage area, default to False.

      :returns: :class:`pandas.DataFrame` -- A typed dataframe containing the site information.


   .. method:: get_streamflow(self, station_ids: Union[Sequence[str], str], dates: Tuple[str, str], mmd: bool = False) -> pd.DataFrame

      Get mean daily streamflow observations from USGS.

      :Parameters: * **station_ids** (:class:`str`, :class:`list`) -- The gage ID(s)  of the USGS station.
                   * **dates** (:class:`tuple`) -- Start and end dates as a tuple (start, end).
                   * **mmd** (:class:`bool`) -- Convert cms to mm/day based on the contributing drainage area of the stations.

      :returns: :class:`pandas.DataFrame` -- Streamflow data observations in cubic meter per second (cms). The stations that
                don't provide mean daily discharge in the target period will be dropped.


   .. method:: query_bybox(bbox: Tuple[float, float, float, float]) -> Dict[str, str]
      :staticmethod:

      Generate the geometry keys and values of an ArcGISRESTful query.


   .. method:: query_byid(ids: Iterable[str]) -> Dict[str, str]
      :staticmethod:

      Generate the geometry keys and values of an ArcGISRESTful query.


   .. method:: retrieve_rdb(self, service: str, payloads: List[Dict[str, str]]) -> pd.DataFrame

      Retrieve and process requests with RDB format.

      :Parameters: * **service** (:class:`str`) -- Name of USGS REST service, valid values are ``site``, ``dv``, ``iv``,
                     ``gwlevels``, and ``stat``. Please consult USGS documentation
                     `here <https://waterservices.usgs.gov/rest>`__ for more information.
                   * **payloads** (:class:`list` of :class:`dict`) -- List of target payloads.

      :returns: :class:`pandas.DataFrame` -- Requested features as a pandas's DataFrame.



.. function:: cover_statistics(ds: xr.Dataset) -> Dict[str, Union[np.ndarray, Dict[str, float]]]

   Percentages of the categorical NLCD cover data.

   :Parameters: **ds** (:class:`xarray.Dataset`) -- Cover DataArray from a LULC Dataset from the ``nlcd`` function.

   :returns: :class:`dict` -- Statistics of NLCD cover data


.. function:: get_nid() -> gpd.GeoDataFrame

   Get all dams in the US (over 91K) from National Inventory of Dams 2019.

   .. rubric:: Notes

   This function downloads a 25 MB excel file and convert it into a
   GeoDataFrame. So, your net speed might be a bottleneck. Another
   bottleneck is data loading since the dataset has more than 91K rows,
   it might take sometime for Pandas to load the data into memory.

   :returns: :class:`geopandas.GeoDataFrame` -- A GeoDataFrame containing all the available dams in the database. This dataframe
             has an ``attrs`` property that contains definitions of all the NID variables including
             their units. You can access this dictionary by, for example, ``nid.attrs`` assuming
             that ``nid`` is the dataframe. For example, ``nli.attrs["VOLUME"]`` returns the definition
             of the ``VOLUME`` column in NID.


.. function:: get_nid_codes() -> pd.DataFrame

   Get the definitions of letter codes in NID database.

   :returns: :class:`pandas.DataFrame` -- A multi-index dataframe where the first index is code categories and the second one is
             letter codes. For example, ``tables.loc[('Core Type',  'A')]`` returns Bituminous Concrete.


.. function:: interactive_map(bbox: Tuple[float, float, float, float], crs: str = DEF_CRS, dv: bool = False, iv: bool = False, param_cd: Optional[str] = None) -> folium.Map

   Generate an interactive map including all USGS stations within a bounding box.

   :Parameters: * **bbox** (:class:`tuple`) -- List of corners in this order (west, south, east, north)
                * **crs** (:class:`str`, *optional*) -- CRS of the input bounding box, defaults to EPSG:4326.
                * **dv** (:class:`bool`, *optional*) -- Only include stations that record daily values, default to False.
                * **iv** (:class:`bool`, *optional*) -- Only include stations that record instantaneous/real-time values, default to False.
                * **param_cd** (:class:`str`, *optional*) -- Parameter code for further filtering the stations, defaults to None.
                  A list of parameter codes can be found
                  `here <https://help.waterdata.usgs.gov/codes-and-parameters/parameters>`__.

   :returns: :class:`folium.Map` -- Interactive map within a bounding box.

   .. rubric:: Examples

   >>> import pygeohydro as gh
   >>> m = gh.interactive_map((-69.77, 45.07, -69.31, 45.45), dv=True, iv=True)
   >>> n_stations = len(m.to_dict()["children"]) - 1
   >>> n_stations
   10


.. function:: nlcd(geometry: Union[Polygon, MultiPolygon, Tuple[float, float, float, float]], resolution: float, years: Optional[Dict[str, Optional[int]]] = None, geo_crs: str = DEF_CRS, crs: str = DEF_CRS) -> xr.Dataset

   Get data from NLCD database (2016).

   Download land use/land cover data from NLCD (2016) database within
   a given geometry in epsg:4326.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`tuple` of :class:`length 4`) -- The geometry or bounding box (west, south, east, north) for extracting the data.
                * **resolution** (:class:`float`) -- The data resolution in meters. The width and height of the output are computed in pixel
                  based on the geometry bounds and the given resolution.
                * **years** (:class:`dict`, *optional*) -- The years for NLCD data as a dictionary, defaults to
                  {'impervious': 2016, 'cover': 2016, 'canopy': 2016}. Set the value of a layer to None,
                  to ignore it.
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **crs** (:class:`str`, *optional*) -- The spatial reference system to be used for requesting the data, defaults to
                  epsg:4326.

   :returns: :class:`xarray.DataArray` -- NLCD within a geometry


.. function:: ssebopeta_bygeom(geometry: Union[Polygon, Tuple[float, float, float, float]], dates: Union[Tuple[str, str], Union[int, List[int]]], geo_crs: str = DEF_CRS) -> xr.DataArray

   Get daily actual ET for a region from SSEBop database.

   .. rubric:: Notes

   Since there's still no web service available for subsetting SSEBop, the data first
   needs to be downloaded for the requested period then it is masked by the
   region of interest locally. Therefore, it's not as fast as other functions and
   the bottleneck could be the download speed.

   :Parameters: * **geometry** (:class:`shapely.geometry.Polygon` or :class:`tuple`) -- The geometry for downloading clipping the data. For a tuple bbox,
                  the order should be (west, south, east, north).
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **geo_crs** (:class:`str`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.

   :returns: :class:`xarray.DataArray` -- Daily actual ET within a geometry in mm/day at 1 km resolution


.. function:: ssebopeta_byloc(coords: Tuple[float, float], dates: Union[Tuple[str, str], Union[int, List[int]]]) -> pd.DataFrame

   Daily actual ET for a location from SSEBop database in mm/day.

   :Parameters: * **coords** (:class:`tuple`) -- Longitude and latitude of the location of interest as a tuple (lon, lat)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].

   :returns: :class:`pandas.DataFrame` -- Daily actual ET for a location


