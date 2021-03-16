.. highlight:: bash

============
Installation
============

Dependencies
------------

Dependencies of HyRiver packages are as follows:

================ ============= ============== ============== ============== ==========
PyGeoOGC         PyGeoUtils    PyNHD          PyGeoHydro     Py3DEP         PyDaymet
================ ============= ============== ============== ============== ==========
``aiodns``       ``pygeoogc``  ``pygeoutils`` ``pynhd``      ``pygeoutils`` ``py3dep``
``aiohttp``      ``geopandas`` ``networkx``   ``folium``                    ``dask``
``brotlipy``     ``netCDF4``   ``pyarrow``    ``lxml``                      ``lxml``
``chardet``      ``rasterio``                 ``matplotlib``                ``scipy``
``cytoolz``      ``xarray``                   ``openpyxl``
``defusedxml``
``nest-asyncio``
``orjson``
``owslib``
``pyproj``
``requests``
``setuptools``
``shapely``
``simplejson``
================ ============= ============== ============== ============== ==========

Additionally, you can also install ``bottleneck`` and ``pygeos`` to improve performance of
``xarray`` and ``geopandas``, respectively. For handling vector and raster data projections,
``cartopy`` and ``rioxarray`` are useful.

Stable release
--------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install pygeoogc pygeoutils py3dep pynhd pygeohydro pydaymet

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can use ``conda`` or ``mamba`` (recommended) to install these packages from
``conda-forge``:

.. code-block:: console

    $ conda install -c conda-forge pygeoogc pygeoutils py3de pynhd pygeohydro pydaymet

or:

.. code-block:: console

    $ mamba install -c conda-forge --strict-channel-priority pygeoogc pygeoutils py3de pynhd pygeohydro pydaymet

From sources
------------

You can install each package from its source. For example, you can install
PyGeoHydro from its Github `repo`_ by either cloning its repository:

.. code-block:: console

    $ git clone https://github.com/cheginit/pygeohydro.git

Or downloading the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/cheginit/pygeohydro/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python -m pip install .

Please refer to the note for installation with ``pip`` above, regarding the
``libgdal`` requirement.

.. _repo: https://github.com/cheginit/pygeohydro
.. _tarball: https://github.com/cheginit/pygeohydro/tarball/master
.. _PyGeoHydro: https://github.com/cheginit/pygeohydro
.. _PyGeoOGC: https://github.com/cheginit/pygeoogc
.. _PyGeoUtils: https://github.com/cheginit/pygeoutils
.. _PyNHD: https://github.com/cheginit/pynhd
.. _Py3DEP: https://github.com/cheginit/py3dep
.. _PyDaymet: https://github.com/cheginit/pydaymet
