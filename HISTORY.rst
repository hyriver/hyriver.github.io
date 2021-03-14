=======
History
=======

0.10.1 (2021-03-06)
-------------------

PyGeoHydro
~~~~~~~~~~
- Add ``lxml`` to deps.

0.10.0 (2021-03-06)
-------------------

PyGeoHydro
~~~~~~~~~~
- The official first release of PyGeoHydro with a new name and logo.
- Replace cElementTree with ElementTree since it's been deprecated by ``defusedxml``.
- Make ``mypy`` checks more strict and fix all the errors and prevent possible
  bugs.
- Speed up CI testing by using ``mamba`` and caching.


0.9.2 (2021-03-02)
------------------

PyGeoHydro
~~~~~~~~~~
- Rename ``hydrodata`` package to ``pygeohydro`` for publication on JOSS.
- In ``NWIS.get_info``, drop rows that don't have mean daily discharge data instead of slicing.
- Add support for the National Inventory of Dams (NID) via ``get_nid`` function.
- Speed up Github Actions by using ``mamba`` and caching.
- Improve ``pip`` installation by adding ``pyproject.toml``.

0.9.1 (2021-02-22)
------------------

PyGeoHydro
~~~~~~~~~~
- Fix an issue with ``NWIS.get_info`` method where stations with False values as their
  ``hcdn_2009`` value were returned as ``None`` instead.

0.9.0 (2021-02-14)
------------------

- Bump versions of packages across the stack to the same version.

PyGeoHydro
~~~~~~~~~~
- Use the new pynhd function for getting basins, ``NLDI.get_basisn``.
- Made ``mypy`` checks more strict and added all the missing type annotations.

PyGeoOGC
~~~~~~~~
- Add support for query by point and multi-points to ``ArcGISRESTful.bygeom``.
- Add support for buffer distance to ``ArcGISRESTful.bygeom``.
- Add support for generating ESRI-based queries for points and multi-points
  to ``ESRIGeomQuery``.
- Add all the missing type annotations.
- Update the Daymet url to version 4. You can check the release information
  `here <https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html>`_
- Use ``cytoolz`` library for some of the operations for improving performance.
- Add ``extent`` property to ``ArcGISRESTful`` class that get the spatial extent
  of the service.
- Add url to ``airmap`` service for getting elevation data at 30 m resolution.

PyGeoUtils
~~~~~~~~~~
- Add ``gtiff2file`` for saving raster responses as ``geotiff`` file(s).
- Fix an error in ``_get_nodata_crs`` for handling nodata value when its value in the source
  is None.
- Fix the warning during the ``GeoDataFrame`` generation in ``json2geodf`` when there is
  no geometry column in the input json.

PyNHD
~~~~~
- Add a new function for getting basins geometries for a list of USGS station IDs.
  The function is a method of ``NLDI`` class called ``get_basins``. So, now
  ``NLDI.getfeature_byid`` function does not have a basin flag. This change
  makes getting geometries easier and faster.
- Remove ``characteristics_dataframe`` method from ``NLDI`` and made a standalone function
  called ``nhdplus_attrs`` for accessing NHDPlus attributes directly from ScienceBase.
- Add a new argument to ``topoogical_sort`` called ``edge_attr`` that allows to
  add attribute(s) to the returned Networkx Graph. By default it is ``None``.
- A new base class, ``AGRBase`` for connecting to ArcGISRESTful-based services such as National Map
  and EPA's WaterGEOS.
- Add support for setting the buffer distance for the input geometries to ``AGRBase.bygeom``.
- Add ``comid_byloc`` to ``NLDI`` class for getting ComIDs of the closest flowlines from a list of
  lon/lat coordinates.
- Add ``bydistance`` to ``WaterData`` for getting features within a given radius of a point.
- Add support for using `hydro <https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer>`_
  or `edits <https://edits.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/NHDPlus_HR/MapServer>`_
  webs services for getting NHDPlus High-Resolution using ``NHDPlusHR`` function. The new arguments
  are ``service`` which accepts ``hydro`` or ``edits``, and ``autos_switch`` flag for automatically
  switching to the other service if the ones passed by ``service`` fails.

Py3DEP
~~~~~~
- Add support for saving maps as ``geotiff`` file(s).
- Replace ``Elevation Point Query Service`` service with ``AirMap`` for getting
  elevations for a list of coordinates in bulk since ``AirMap`` is much faster.
  The resolution of ``AirMap`` is 30 m.
- Use ``cytoolz`` for some of the operations for improving performance.

PyDaymet
~~~~~~~~
- Update to version 4 of Daymet database. You can check the release information
  `here <https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html>`_
- Add a new function called ``get_bycoords`` that provides an alternative to ``get_byloc``
  for getting climate data at a single pixel. This new function uses THREDDS data server
  with NetCDF Subset Service (NCSS), and supports getting monthly and annual averages directly
  from the server. Note that this function will replace ``get_byloc`` in  the future.
  So consider migrating your code by replacing ``get_byloc`` with ``get_bycoords``. The
  input arguments of ``get_bycoords`` is very similar to ``get_bygeom``. Another difference
  between ``get_byloc`` and ``get_bycoords`` is column names where ``get_bycoords`` uses
  the units that are return by NCSS server.
- Add support for downloading mothly and annual summaries in addition to the daily
  time-scale. You can pass ``time_scale`` as ``daily``, ``monthly``, or ``annual``
  to ``get_bygeom`` or ``get_bycoords`` functions to download the respective summaries.
- Add support for getting climate data for Hawaii and Puerto Rico by passing ``region``
  to ``get_bygeom`` and ``get_bycoords`` functions. The acceptable values are ``na`` for
  CONUS, ``hi`` for Hawaii, and ``pr`` for Puerto Rico.

0.8.0 (2020-12-06)
------------------

- Fixed the issue with WaterData due to the recent changes on the server side.
- Updated the examples based on the latest changes across the stack.
- Add support for multipolygon.
- Remove the ``fill_hole`` argument.
- Fix a warning in ``nlcd`` regarding performing division on nan values.

0.7.2 (2020-8-18)
-----------------

Enhancements
~~~~~~~~~~~~
- Replaced ``simplejson`` with ``orjson`` to speed-up JSON operations.
- Explicitly sort the time dimension of the ``ssebopeta_bygeom`` function.

Bug fixes
~~~~~~~~~
- Fix an issue with the ``nlcd`` function where high resolution requests fail.

0.7.1 (2020-8-13)
-----------------

New Features
~~~~~~~~~~~~
- Added a new argument to ``plot.signatures`` for controlling the vertical position of the
  plot title, called ``title_ypos``. This could be useful for multi-line titles.

Bug fixes
~~~~~~~~~
- Fixed an issue with the ``nlcd`` function where none layers are not dropped and cause the
  function to fails.

0.7.0 (2020-8-12)
-----------------

This version divides PyGeoHydro into six standalone Python libraries. So many of the changes
listed below belong to the modules and functions that are now a separate package. This decision
was made for reducing the complexity of the code base and allow the users to only install
the packages that they need without having to install all the PyGeoHydro dependencies.

Breaking changes
~~~~~~~~~~~~~~~~
- The ``services`` module is now a separate package called PyGeoOGCC and is set as a requirement
  for PyGeoHydro. PyGeoOGC is a leaner package with much less dependencies and is suitable for
  people who might only need an interface to web services.
- Unified function names for getting feature by ID and by box.
- Combined ``start`` and ``end`` arguments into a ``tuple`` argument
  called ``dates`` across the code base.
- Rewrote NLDI function and moved most of its classmethods to Station
  so now Station class has more cohesion.
- Removed exploratory functionality of ``ArcGISREST``, since it's more convenient
  to do so from a browser. Now, ``base_url`` is a required arguments.
- Renamed ``in_crs`` in ``datasets`` and ``services`` functions to ``geo_crs`` for geometry and
  ``box_crs`` for bounding box inputs.
- Re-wrote the ``signatures`` function from scratch using ``NamedTuple`` to improve readability
  and efficiency. Now, the ``daily`` argument should be just a ``pandas.DataFrame`` or
  ``pandas.Series`` and the column names are used for legends.
- Removed ``utils.geom_mask`` function and replaced it with ``rasterio.mask.mask``.
- Removed ``width`` as an input in functions with raster output since ``resolution`` is almost
  always the preferred way to request for data. This change made the code more readable.
- Renamed two functions: ``ArcGISRESTful`` and ``wms_bybox``. These function now return
  ``requests.Response`` type output.
- ``onlyipv4`` is now a class method in ``RetrySession``.
- The ``plot.signatures`` function now assumes that the input time series are in mm/day.
- Added a flag to ``get_streamflow`` function in the ``NWIS`` class to convert from cms
  to mm/day which is useful for plotting hydrologic signatures using the ``signatures``
  functions.

Enhancements
~~~~~~~~~~~~
- Remove soft requirements from the env files.
- Refactored ``requests`` functions into a single class and a separate file.
- Made all the classes available directly from ``pygeohydro``.
- Added `CodeFactor <https://www.codefactor.io/>`_ to the Github pipeline and addressed
  the some of issues
  that CodeFactor found.
- Added `Bandit <https://bandit.readthedocs.io/en/latest/>`_ to check the code for
  secutiry issue.
- Improved docstrings and documentations.
- Added customized exceptions for better exception handling.
- Added ``pytest`` fixtures to improve the tests speed.
- Refactored ``daymet`` and ``nwis_siteinfo`` functions to reduce code complexity
  and improve readability.
- Major refactoring of the code base while adding type hinting.
- The input geometry (or bounding box) can be provided in any projection
  and the necessary re-projections are done under the hood.
- Refactored the method for getting object IDs in ``ArcGISREST`` class to improve
  robustness and efficiency.
- Refactored ``Daymet`` class to improve readability.
- Add `Deepsource <https://deepsource.io/>`_ for further code quality checking.
- Automatic handling of large WMS requests (more than 8 million pixel i.e., width x height)
- The ``json_togeodf`` function now accepts both a single (Geo)JSON or a list of them
- Refactored ``plot.signatures`` using ``add_gridspec`` for a much cleaner code.

New Features
~~~~~~~~~~~~
- Added access to WaterData's Geoserver databases.
- Added access to the remaining NLDI database (Water Quality Portal and Water Data Exchange).
- Created a Binder for launching a computing environment on the cloud and testing PyGeoHydro.
- Added a URL repository for the supported services called ``ServiceURL``
- Added support for `FEMA <https://hazards.fema.gov/femaportal/wps/portal/NFHLWMS>`_ web services
  for flood maps and `FWS <https://www.fws.gov/wetlands/Data/Web-Map-Services.html>`_ for wetlands.
- Added a new function called ``wms_toxarray`` for converting WMS request responses to
  ``xarray.DataArray`` or ``xarray.Dataset``.

Bug fixes
~~~~~~~~~
- Re-projection issues for function with input geometry.
- Start and end variables not being initialized when coords was used in ``Station``.
- Geometry mask for ``xarray.DataArray``
- WMS output re-projections

0.6.0 (2020-06-23)
------------------

- Refactor requests session
- Improve overall code quality based on CodeFactor suggestions
- Migrate to Github Actions from TravisCI

0.5.5 (2020-06-03)
------------------

- Add to conda-forge
- Remove pqdm and arcgis2geojson dependencies

0.5.3 (2020-06-07)
------------------

- Added threading capability to the flow accumulation function
- Generalized WFS to include both by bbox and by featureID
- Migrate RTD to pip from conda
- Changed HCDN database source to GagesII database
- Increased robustness of functions that need network connections
- Made the flow accumulation output a pandas Series for better handling of time
  series input
- Combined DEM, slope, and aspect in a class called NationalMap.
- Installation from pip installs all the dependencies

0.5.0 (2020-04-25)
------------------

- An almost complete re-writing of the code base and not backward-compatible
- New website design
- Added vector accumulation
- Added base classes and function accessing any ArcGIS REST, WMS, WMS service
- Standalone functions for creating datasets from responses and masking the data
- Added threading using pqdm to speed up the downloads
- Interactive map for exploring USGS stations
- Replaced OpenTopography with 3DEP
- Added HCDN database for identifying natural watersheds

0.4.4 (2020-03-12)
------------------

- Added new databases: NLDI, NHDPLus V2, OpenTopography, gridded Daymet, and SSEBop
- The gridded data are returned as xarray DataArrays
- Removed dependency on StreamStats and replaced it by NLDI
- Improved overall robustness and efficiency of the code
- Not backward comparable
- Added code style enforcement with isort, black, flake8 and pre-commit
- Added a new shiny logo!
- New installation method
- Changed OpenTopography base url to their new server
- Fixed NLCD legend and statistics bug

0.3.0 (2020-02-10)
------------------

- Clipped the obtained NLCD data using the watershed geometry
- Added support for specifying the year for getting NLCD
- Removed direct NHDPlus data download dependency buy using StreamStats and USGS APIs
- Renamed get_lulc function to get_nlcd

0.2.0 (2020-02-09)
------------------

- Simplified import method
- Changed usage from ``rst`` format to ``ipynb``
- Autoo-formatting with the black python package
- Change docstring format based on Sphinx
- Fixed pytest warnings and changed its working directory
- Added an example notebook with datafiles
- Added docstring for all the functions
- Added Module section to the documentation
- Fixed py7zr issue
- Changed 7z extractor from pyunpack to py7zr
- Fixed some linting issues.

0.1.0 (2020-01-31)
------------------

- First release on PyPI.
