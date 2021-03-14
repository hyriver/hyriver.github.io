.. highlight:: bash

============
Installation
============

Dependencies
------------

Dependencies of HyRiver packages are as follows:

* PyGeoOGC_:

  - ``aiodns``
  - ``aiohttp``
  - ``brotlipy``
  - ``chardet``
  - ``cytoolz``
  - ``defusedxml``
  - ``nest-asyncio``
  - ``orjson``
  - ``owslib``
  - ``pyproj``
  - ``requests``
  - ``setuptools``
  - ``shapely``
  - ``simplejson``

* PyGeoUtils_:

  - ``pygeoogc``
  - ``geopandas``
  - ``netCDF4``
  - ``rasterio``
  - ``xarray``

* Py3DEP_:

  - ``pygeoogc``
  - ``pygeoutils``

* PyNHD_:

  - ``pygeoogc``
  - ``pygeoutils``
  - ``networkx``
  - ``pyarrow``

* PyGeoHydro_:

  - ``pygeoogc``
  - ``pygeoutils``
  - ``pynhd``
  - ``folium``
  - ``lxml``
  - ``matplotlib``
  - ``openpyxl``

* PyDaymet_:

  - ``pygeoogc``
  - ``pygeoutils``
  - ``py3dep``
  - ``dask``
  - ``lxml``
  - ``scipy``

The following optional libraries are recommended to improve performance of ``xarray``:

- ``bottleneck``
- ``numbagg``

You can also install ``pygeos`` to improve performance of ``geopandas``. Additionally,
`CartoPy`_ can be installed to support more projections when plotting geospatial data with
``matplotlib``. This library is specifically useful for plotting Daymet data.

Stable release
--------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install pygeoogc pygeoutils py3dep pynhd pygeohydro pydaymet

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can use ``conda`` or ``mamba`` to install these packages from ``conda-forge``:

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

.. _CartoPy: http://scitools.org.uk/cartopy
.. _repo: https://github.com/cheginit/pygeohydro
.. _tarball: https://github.com/cheginit/pygeohydro/tarball/master
.. _PyGeoHydro: https://github.com/cheginit/pygeohydro
.. _PyGeoOGC: https://github.com/cheginit/pygeoogc
.. _PyGeoUtils: https://github.com/cheginit/pygeoutils
.. _PyNHD: https://github.com/cheginit/pynhd
.. _Py3DEP: https://github.com/cheginit/py3dep
.. _PyDaymet: https://github.com/cheginit/pydaymet
