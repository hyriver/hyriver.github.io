:py:mod:`pydaymet.pet`
======================

.. py:module:: pydaymet.pet

.. autoapi-nested-parse::

   Core class for the Daymet functions.



Module Contents
---------------

.. py:function:: potential_et(clm, coords = None, crs = 'epsg:4326', alt_unit = False, method = 'fao56')

   Compute Potential EvapoTranspiration for both gridded and a single location.

   .. rubric:: Notes

   The method is based on
   `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm>`__
   assuming that soil heat flux density is zero.

   :Parameters: * **clm** (:class:`pandas.DataFrame` or :class:`xarray.Dataset`) -- The dataset must include at least the following variables:

                  * Minimum temperature in degree celsius
                  * Maximum temperature in degree celsius
                  * Solar radiation in in W/m^2
                  * Daylight duration in seconds

                  Optionally, relative humidity and wind speed at 2-m level will be used if available.

                  Table below shows the variable names that the function looks for in the input data.

                  ================ ========
                  DataFrame        Dataset
                  ================ ========
                  ``tmin (deg c)`` ``tmin``
                  ``tmax (deg c)`` ``tmax``
                  ``srad (W/m^2)`` ``srad``
                  ``dayl (s)``     ``dayl``
                  ``rh (-)``       ``rh``
                  ``u2 (m/s)``     ``u2``
                  ================ ========

                  If relative humidity and wind speed at 2-m level are not available,
                  actual vapour pressure is assumed to be saturation vapour pressure at daily minimum
                  temperature and 2-m wind speed is considered to be 2 m/s.
                * **coords** (:class:`tuple` of :class:`floats`, *optional*) -- Coordinates of the daymet data location as a tuple, (x, y). This is required when ``clm``
                  is a ``DataFrame``.
                * **crs** (:class:`str`, *optional*) -- The spatial reference of the input coordinate, defaults to ``epsg:4326``. This is only used
                  when ``clm`` is a ``DataFrame``.
                * **alt_unit** (:class:`str`, *optional*) -- Whether to use alternative units rather than the official ones, defaults to False.
                * **method** (:class:`str`, *optional*) -- Method for computing PET. At the moment only ``fao56`` is supported which is based on
                  `FAO Penman-Monteith equation <http://www.fao.org/3/X0490E/x0490e06.htm>`__ assuming that
                  soil heat flux density is zero.

   :returns: :class:`pandas.DataFrame` or :class:`xarray.Dataset` -- The input DataFrame/Dataset with an additional variable named ``pet (mm/day)`` for
             DataFrame and ``pet`` for Dataset.


