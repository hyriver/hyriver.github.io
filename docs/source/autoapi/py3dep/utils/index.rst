py3dep.utils
============

.. py:module:: py3dep.utils

.. autoapi-nested-parse::

   Utilities for Py3DEP.





Module Contents
---------------

.. py:function:: deg2mpm(slope)

   Convert slope from degrees to meter/meter.

   :Parameters: **slope** (:class:`xarray.DataArray`) -- Slope in degrees.

   :returns: :class:`xarray.DataArray` -- Slope in meter/meter. The name is set to ``slope`` and the ``units`` attribute
             is set to ``m/m``.


.. py:function:: fill_depressions(elevtn, outlets = 'min', idxs_pit = None, nodata = np.nan, max_depth = -1.0, elv_max = None, connectivity = 8)

   Fill local depressions in elevation data based on Wang and Liu (2006).

   .. note::

       This function is based on the ``fill_depressions`` function from the
       `pyflwdir <https://github.com/Deltares/pyflwdir>`__ package. This function
       improves the performance of the original function by a factor of up to 2 and
       adds more input checks. Additionally, it works with ``xarray.DataArray`` objects.

       Outlets are assumed to occur at the edge of valid elevation cells ``outlets='edge'``;
       at the lowest valid edge cell to create one single outlet ``outlets='min'``;
       or at user provided outlet cells ``idxs_pit``.

       Depressions elsewhere are filled based on its lowest pour point elevation.
       If the pour point depth is larger than the maximum pour point depth ``max_depth``
       a pit is set at the depression local minimum elevation.

       Wang, L., & Liu, H. (2006). https://doi.org/10.1080/13658810500433453

   :Parameters: * **elevtn** (:class:`numpy.ndarray` or :class:`xarray.DataArray`) -- elevation raster as a 2D ``numpy.ndarray`` or ``xarray.DataArray``.
                * **outlets** (``{"edge", "min}``, *optional*) -- Initial basin outlet(s) at the edge of all cells ('edge')
                  or only the minimum elevation edge cell ('min'; default)
                * **idxs_pit** (:class:`1D array` of :class:`int`, *optional*) -- Linear indices of outlet cells, in any, defaults to None.
                * **nodata** (:class:`float`, *optional*) -- nodata value, defaults to ``numpy.nan``.
                * **max_depth** (:class:`float`, *optional*) -- Maximum pour point depth. Depressions with a larger pour point
                  depth are set as pit. A negative value (default) equals an infitely
                  large pour point depth causing all depressions to be filled.
                  Defaults to -1.0.
                * **elv_max, float, optional** -- Maximum elevation for outlets, only in combination with ``outlets='edge'``.
                  By default ``None``.
                * **connectivity** (``{4, 8}``, *optional*) -- Number of neighboring cells to consider, defaults to 8.

   :returns: **elevtn_out** (:class:`numpy.ndarray`) -- Depression filled elevation with type float32.


