:py:mod:`py3dep.utils`
======================

.. py:module:: py3dep.utils

.. autoapi-nested-parse::

   Utilities for Py3DEP.



Module Contents
---------------

.. py:function:: deg2mpm(slope)

   Convert slope from degrees to meter/meter.

   :Parameters: **da** (:class:`xarray.DataArray`) -- Slope in degrees.

   :returns: :class:`xarray.DataArray` -- Slope in meter/meter. The name is set to ``slope`` and the ``units`` attribute
             is set to ``m/m``.


.. py:function:: fill_depressions(dem)

   Fill depressions and adjust flat areas in a DEM using `RichDEM <https://richdem.readthedocs.io>`__.

   :Parameters: **dem** (:class:`xarray.DataArray` or :class:`numpy.ndarray`) -- Digital Elevation Model.

   :returns: :class:`xarray.DataArray` -- Conditioned DEM after applying
             `depression filling <https://richdem.readthedocs.io/en/latest/depression_filling.html>`__
             and
             `flat area resolution <https://richdem.readthedocs.io/en/latest/flat_resolution.html>`__
             operations.


