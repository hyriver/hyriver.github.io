:py:mod:`pydaymet.pet`
======================

.. py:module:: pydaymet.pet

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:function:: potential_et(clm, coords, crs, method = ..., params = ...)
                 potential_et(clm: xarray.Dataset, coords: None = None, crs: None = None, method: str = ..., params: dict[str, float] | None = ...) -> xarray.Dataset

   Compute Potential EvapoTranspiration for both gridded and a single location.

   :Parameters: * **clm** (:class:`pandas.DataFrame` or :class:`xarray.Dataset`) -- The dataset must include at least the following variables:

                  * Minimum temperature in degree celsius
                  * Maximum temperature in degree celsius
                  * Solar radiation in in W/m2
                  * Daylight duration in seconds

                  Optionally, for ``penman_monteith``, wind speed at 2-m level
                  will be used if available, otherwise, default value of 2 m/s
                  will be assumed. Table below shows the variable names
                  that the function looks for in the input data.

                  ==================== ==================
                  ``pandas.DataFrame`` ``xarray.Dataset``
                  ==================== ==================
                  ``tmin (degrees C)`` ``tmin``
                  ``tmax (degrees C)`` ``tmax``
                  ``srad (W/m2)``      ``srad``
                  ``dayl (s)``         ``dayl``
                  ``u2m (m/s)``        ``u2m``
                  ==================== ==================
                * **coords** (:class:`tuple` of :class:`floats`, *optional*) -- Coordinates of the daymet data location as a tuple, (x, y). This is required when ``clm``
                  is a ``DataFrame``.
                * **crs** (:class:`str`, :class:`int`, or :class:`pyproj.CRS`, *optional*) -- The spatial reference of the input coordinate, defaults to ``EPSG:4326``. This is only used
                  when ``clm`` is a ``DataFrame``.
                * **method** (:class:`str`, *optional*) -- Method for computing PET. Supported methods are
                  ``penman_monteith``, ``priestley_taylor``, and ``hargreaves_samani``.
                  The ``penman_monteith`` method is based on
                  :footcite:t:`Allen_1998` assuming that soil heat flux density is zero.
                  The ``priestley_taylor`` method is based on
                  :footcite:t:`Priestley_1972` assuming that soil heat flux density is zero.
                  The ``hargreaves_samani`` method is based on :footcite:t:`Hargreaves_1982`.
                  Defaults to ``hargreaves_samani``.
                * **params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary, defaults to ``None``. Valid
                  parameters are:

                  * ``penman_monteith``: ``soil_heat_flux``, ``albedo``, ``alpha``,
                    and ``arid_correction``.
                  * ``priestley_taylor``: ``soil_heat_flux``, ``albedo``, and ``arid_correction``.
                  * ``hargreaves_samani``: None.

                  Default values for the parameters are: ``soil_heat_flux`` = 0, ``albedo`` = 0.23,
                  ``alpha`` = 1.26, and ``arid_correction`` = False.
                  An important parameter for ``priestley_taylor`` and ``penman_monteith`` methods
                  is ``arid_correction`` which is used to correct the actual vapor pressure
                  for arid regions. Since relative humidity is not provided by Daymet, the actual
                  vapor pressure is computed assuming that the dewpoint temperature is equal to
                  the minimum temperature. However, for arid regions, FAO 56 suggests subtracting
                  minimum temperature by 2-3 °C to account for the fact that in arid regions,
                  the air might not be saturated when its temperature is at its minimum. For such
                  areas, you can pass ``{"arid_correction": True, ...}`` to subtract 2 °C from the
                  minimum temperature for computing the actual vapor pressure.

   :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- The input DataFrame/Dataset with an additional variable named ``pet (mm/day)`` for
             ``pandas.DataFrame`` and ``pet`` for ``xarray.Dataset``.

   .. rubric:: References

   .. footbibliography::


