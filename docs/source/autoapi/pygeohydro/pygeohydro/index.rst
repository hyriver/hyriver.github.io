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

      Get the excel file that containes the dam data.



.. py:class:: NWIS

   Access NWIS web service.

   .. method:: get_info(self, query: Dict[str, str], expanded: bool = False) -> pd.DataFrame

      Get NWIS stations by a list of IDs or within a bounding box.

      Only stations that record(ed) daily streamflow data are returned.
      The following columns are included in the dataframe with expanded
      set to False:

      ==================  ==================================
      Name                Description
      ==================  ==================================
      site_no             Site identification number
      station_nm          Site name
      site_tp_cd          Site type
      dec_lat_va          Decimal latitude
      dec_long_va         Decimal longitude
      coord_acy_cd        Latitude-longitude accuracy
      dec_coord_datum_cd  Decimal Latitude-longitude datum
      alt_va              Altitude of Gage/land surface
      alt_acy_va          Altitude accuracy
      alt_datum_cd        Altitude datum
      huc_cd              Hydrologic unit code
      parm_cd             Parameter code
      stat_cd             Statistical code
      ts_id               Internal timeseries ID
      loc_web_ds          Additional measurement description
      medium_grp_cd       Medium group code
      parm_grp_cd         Parameter group code
      srs_id              SRS ID
      access_cd           Access code
      begin_date          Begin date
      end_date            End date
      count_nu            Record count
      hcdn_2009           Whether is in HCDN-2009 stations
      ==================  ==================================

      :Parameters: * **query** (:class:`dict`) -- A dictionary containing query by IDs or BBOX. Use ``query_byid`` or ``query_bbox``
                     class methods to generate the queries.
                   * **expanded** (:class:`bool`, *optional*) -- Whether to get expanded sit information for example drainage area.

      :returns: :class:`pandas.DataFrame` -- NWIS stations


   .. method:: get_streamflow(self, station_ids: Union[List[str], str], dates: Tuple[str, str], mmd: bool = False) -> pd.DataFrame

      Get daily streamflow observations from USGS.

      :Parameters: * **station_ids** (:class:`str`, :class:`list`) -- The gage ID(s)  of the USGS station.
                   * **dates** (:class:`tuple`) -- Start and end dates as a tuple (start, end).
                   * **mmd** (:class:`bool`) -- Convert cms to mm/day based on the contributing drainage area of the stations.

      :returns: :class:`pandas.DataFrame` -- Streamflow data observations in cubic meter per second (cms)


   .. method:: query_bybox(bbox: Tuple[float, float, float, float]) -> Dict[str, str]
      :staticmethod:

      Generate the geometry keys and values of an ArcGISRESTful query.


   .. method:: query_byid(ids: Union[str, List[str]]) -> Dict[str, str]
      :staticmethod:

      Generate the geometry keys and values of an ArcGISRESTful query.



.. function:: cover_statistics(ds: xr.Dataset) -> Dict[str, Union[np.ndarray, Dict[str, float]]]

   Percentages of the categorical NLCD cover data.

   :Parameters: **ds** (:class:`xarray.Dataset`) -- Cover dataarray of a LULC dataset from the `nlcd` function.

   :returns: :class:`dict` -- Statistics of NLCD cover data


.. function:: get_nid() -> gpd.GeoDataFrame

   Get all dams in the US (over 91K) from National Inventory of Dams 2019.

   .. rubric:: Notes

   This function downloads a 25 MB `xlsx` file and convert it into a
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


.. function:: interactive_map(bbox: Tuple[float, float, float, float]) -> folium.Map

   Generate an interactive map including all USGS stations within a bounding box.

   .. rubric:: Notes

   Only stations that record(ed) daily streamflow data are included.

   :Parameters: **bbox** (:class:`tuple`) -- List of corners in this order (west, south, east, north)

   :returns: :class:`folium.Map` -- Interactive map within a bounding box.


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


