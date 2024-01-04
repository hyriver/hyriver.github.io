:py:mod:`py3dep.utils`
======================

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


.. py:function:: fill_depressions(dem, outlets = 'min')

   Hydrocondition the DEM.

   This function uses `pyflwdir <https://deltares.github.io/pyflwdir/latest/>`__.
   It can be installed using ``pip install pyflwdir`` or
   ``conda install -c conda-forge pyflwdir``.

   :Parameters: * **dem_da** (:class:`xarray.DataArray` or :class:`numpy.ndarray`) -- Digital Elevation Model.
                * **outlets** (:class:`str`, *optional*) -- Initial basin outlet(s) at the edge of all cells
                  (``edge``) or only the minimum elevation edge cell (``min``; default).

   :returns: :class:`xarray.DataArray` -- Conditioned DEM after applying ``fill_depressions`` function from
             `pyflwdir <https://deltares.github.io/pyflwdir/latest/>`__.


