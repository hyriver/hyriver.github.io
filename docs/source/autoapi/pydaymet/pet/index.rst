:py:mod:`pydaymet.pet`
======================

.. py:module:: pydaymet.pet

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:function:: potential_et(clm, coords = None, crs = 'epsg:4326', method = 'hargreaves_samani', params = None)

   Compute Potential EvapoTranspiration for both gridded and a single location.

   :Parameters: * **clm** (:class:`pandas.DataFrame` or :class:`xarray.Dataset`) -- The dataset must include at least the following variables:

                  * Minimum temperature in degree celsius
                  * Maximum temperature in degree celsius
                  * Solar radiation in in W/m2
                  * Daylight duration in seconds

                  Optionally, relative humidity and wind speed at 2-m level will be used if available.

                  Table below shows the variable names that the function looks for in the input data.

                  ==================== ========
                  DataFrame            Dataset
                  ==================== ========
                  ``tmin (degrees C)`` ``tmin``
                  ``tmax (degrees C)`` ``tmax``
                  ``srad (W/m2)``      ``srad``
                  ``dayl (s)``         ``dayl``
                  ``rh (-)``           ``rh``
                  ``u2 (m/s)``         ``u2``
                  ==================== ========

                  If relative humidity and wind speed at 2-m level are not available,
                  actual vapour pressure is assumed to be saturation vapour pressure at daily minimum
                  temperature and 2-m wind speed is considered to be 2 m/s.
                * **coords** (:class:`tuple` of :class:`floats`, *optional*) -- Coordinates of the daymet data location as a tuple, (x, y). This is required when ``clm``
                  is a ``DataFrame``.
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to ``epsg:4326``. This is only used
                  when ``clm`` is a ``DataFrame``.
                * **method** (:class:`str`, *optional*) -- Method for computing PET. Supported methods are
                  ``penman_monteith``, ``priestley_taylor``, ``hargreaves_samani``, and
                  None (don't compute PET). The ``penman_monteith`` method is based on
                  :footcite:t:`Allen_1998` assuming that soil heat flux density is zero.
                  The ``priestley_taylor`` method is based on
                  :footcite:t:`Priestley_1972` assuming that soil heat flux density is zero.
                  The ``hargreaves_samani`` method is based on :footcite:t:`Hargreaves_1982`.
                  Defaults to ``hargreaves_samani``.
                * **params** (:class:`dict`, *optional*) -- Model-specific parameters as a dictionary, defaults to ``None``.

   :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- The input DataFrame/Dataset with an additional variable named ``pet (mm/day)`` for
             DataFrame and ``pet`` for Dataset.

   .. rubric:: References

   .. footbibliography::


