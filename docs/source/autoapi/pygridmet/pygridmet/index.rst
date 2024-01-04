:py:mod:`pygridmet.pygridmet`
=============================

.. py:module:: pygridmet.pygridmet

.. autoapi-nested-parse::

   Access the GridMET database for both single single pixel and gridded queries.



Module Contents
---------------

.. py:function:: get_bycoords(coords, dates, coords_id = None, crs = 4326, variables = None, snow = False, snow_params = None, ssl = True, to_xarray = False)

   Get point-data from the GridMET database at 1-km resolution.

   :Parameters: * **coords** (:class:`tuple` or :class:`list` of :class:`tuples`) -- Coordinates of the location(s) of interest as a tuple (x, y)
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years ``[2001, 2010, ...]``.
                * **coords_id** (:class:`list` of :class:`int` or :class:`str`, *optional*) -- A list of identifiers for the coordinates. This option only applies when ``to_xarray``
                  is set to ``True``. If not provided, the coordinates will be enumerated.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input coordinates, defaults to ``EPSG:4326``.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``pr``, ``rmax``, ``rmin``, ``sph``, ``srad``, ``th``, ``tmmn``, ``tmmx``, ``vs``,
                  ``bi``, ``fm100``, ``fm1000``, ``erc``, ``etr``, ``pet``, and ``vpd``.
                  Descriptions can be found `here <https://www.climatologylab.org/gridmet.html>`__.
                  Defaults to ``None``, i.e., all the variables are downloaded.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **ssl** (:class:`bool`, *optional*) -- Whether to verify SSL certification, defaults to ``True``.
                * **to_xarray** (:class:`bool`, *optional*) -- Return the data as an ``xarray.Dataset``. Defaults to ``False``.

   :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- Daily climate data for a single or list of locations.

   .. rubric:: Examples

   >>> import pygridmet as gridmet
   >>> coords = (-1431147.7928, 318483.4618)
   >>> dates = ("2000-01-01", "2000-01-31")
   >>> clm = gridmet.get_bycoords(
   ...     coords,
   ...     dates,
   ...     crs=3542,
   ... )
   >>> clm["pr (mm)"].mean()
   9.677


.. py:function:: get_bygeom(geometry, dates, crs = 4326, variables = None, snow = False, snow_params = None, ssl = True)

   Get gridded data from the GridMET database at 1-km resolution.

   :Parameters: * **geometry** (:class:`Polygon`, :class:`MultiPolygon`, or :class:`bbox`) -- The geometry of the region of interest.
                * **dates** (:class:`tuple` or :class:`list`, *optional*) -- Start and end dates as a tuple (start, end) or a list of years [2001, 2010, ...].
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The CRS of the input geometry, defaults to epsg:4326.
                * **variables** (:class:`str` or :class:`list`) -- List of variables to be downloaded. The acceptable variables are:
                  ``pr``, ``rmax``, ``rmin``, ``sph``, ``srad``, ``th``, ``tmmn``, ``tmmx``, ``vs``,
                  ``bi``, ``fm100``, ``fm1000``, ``erc``, ``etr``, ``pet``, and ``vpd``.
                  Descriptions can be found `here <https://www.climatologylab.org/gridmet.html>`__.
                  Defaults to ``None``, i.e., all the variables are downloaded.
                * **snow** (:class:`bool`, *optional*) -- Compute snowfall from precipitation and minimum temperature. Defaults to ``False``.
                * **snow_params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary that is passed to the snowfall function.
                  These parameters are only used if ``snow`` is ``True``. Two parameters are required:
                  ``t_rain`` (deg C) which is the threshold for temperature for considering rain and
                  ``t_snow`` (deg C) which is the threshold for temperature for considering snow.
                  The default values are ``{'t_rain': 2.5, 't_snow': 0.6}`` that are adopted from
                  https://doi.org/10.5194/gmd-11-1077-2018.
                * **ssl** (:class:`bool`, *optional*) -- Whether to verify SSL certification, defaults to ``True``.

   :returns: :class:`xarray.Dataset` -- Daily climate data within the target geometry.

   .. rubric:: Examples

   >>> from shapely import Polygon
   >>> import pygridmet as gridmet
   >>> geometry = Polygon(
   ...     [[-69.77, 45.07], [-69.31, 45.07], [-69.31, 45.45], [-69.77, 45.45], [-69.77, 45.07]]
   ... )
   >>> clm = gridmet.get_bygeom(geometry, 2010, variables="tmmn")
   >>> clm["tmmn"].mean().item()
   274.167


