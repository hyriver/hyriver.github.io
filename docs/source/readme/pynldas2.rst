
PyNLDAS2: Hourly NLDAS-2 Forcing Data
-------------------------------------

.. image:: https://img.shields.io/pypi/v/pynldas2.svg
    :target: https://pypi.python.org/pypi/pynldas2
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pynldas2.svg
    :target: https://anaconda.org/conda-forge/pynldas2
    :alt: Conda Version

.. image:: https://codecov.io/gh/hyriver/pynldas2/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/hyriver/pynldas2
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pynldas2.svg
    :target: https://pypi.python.org/pypi/pynldas2
    :alt: Python Versions

.. image:: https://github.com/hyriver/pynldas2/actions/workflows/test.yml/badge.svg
    :target: https://github.com/hyriver/pynldas2/actions/workflows/test.yml
    :alt: Github Actions

|

.. image:: https://img.shields.io/badge/security-bandit-green.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security Status

.. image:: https://www.codefactor.io/repository/github/hyriver/pynldas2/badge
   :target: https://www.codefactor.io/repository/github/hyriver/pynldas2
   :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

|

Features
--------

PyNLDAS2 is a part of `HyRiver <https://github.com/hyriver/HyRiver>`__ software stack that
is designed to aid in hydroclimate analysis through web services. This package
provides access `NLDAS-2 Forcing dataset <https://ldas.gsfc.nasa.gov/nldas/v2/forcing>`__
via `Hydrology Data Rods <https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods>`__.
Currently, only hourly data is supported. There are three main functions:

- ``get_bycoords``: Forcing data for a list of coordinates as a ``pandas.DataFrame`` or
  ``xarray.Dataset``,
- ``get_bygeom``: Forcing data within a geometry as a ``xarray.Dataset``,
- ``get_grid_mask``: NLDAS2
  `land/water grid mask <https://ldas.gsfc.nasa.gov/nldas/specifications>`__
  as a ``xarray.Dataset``.

PyNLDAS2 only provides access to the hourly NLDAS2 dataset, so if you need to access
other NASA climate datasets you can check out
`tsgettoolbox <https://pypi.org/project/tsgettoolbox/>`__ developed by
`Tim Cera <https://github.com/timcera>`__.

PyNLDAS2 uses AsyncRetriever for requesting data from the NLDAS web service efficiently
and reliably. You can control the request/response caching behavior and its verbosity
by setting the following environment variables:

* ``HYRIVER_CACHE_NAME``: Path to the caching SQLite database. It defaults to
  ``./cache/aiohttp_cache.sqlite``
* ``HYRIVER_CACHE_EXPIRE``: Expiration time for cached requests in seconds. It defaults to
  -1 (never expire).
* ``HYRIVER_CACHE_DISABLE``: Disable reading/writing from/to the cache. The default is false.
* ``HYRIVER_VERBOSE``: Enable verbose mode. The default is false.

For example, in your code before making any requests you can do:

.. code-block:: python

    import os

    os.environ["HYRIVER_CACHE_NAME"] = "path/to/file.sqlite"
    os.environ["HYRIVER_CACHE_EXPIRE"] = "3600"
    os.environ["HYRIVER_CACHE_DISABLE"] = "true"
    os.environ["HYRIVER_VERBOSE"] = "true"

You can find some example notebooks `here <https://github.com/hyriver/HyRiver-examples>`__.

You can also try using PyNLDAS2 without installing
it on your system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser, and you
can start coding!

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/hyriver/pynldas2/issues>`__.

Citation
--------
If you use any of HyRiver packages in your research, we appreciate citations:

.. code-block:: bibtex

    @article{Chegini_2021,
        author = {Chegini, Taher and Li, Hong-Yi and Leung, L. Ruby},
        doi = {10.21105/joss.03175},
        journal = {Journal of Open Source Software},
        month = {10},
        number = {66},
        pages = {1--3},
        title = {{HyRiver: Hydroclimate Data Retriever}},
        volume = {6},
        year = {2021}
    }

Installation
------------

You can install ``pynldas2`` using ``pip``:

.. code-block:: console

    $ pip install pynldas2

Alternatively, ``pynldas2`` can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pynldas2

Quick start
-----------

The NLDAS2 database provides forcing data at 1/8th-degree grid spacing and range
from 01 Jan 1979 to present. Let's take a look at NLDAS2 grid mask that includes
land, water, soil, and vegetation masks:


.. code-block:: python

    import pynldas2 as nldas

    grid = nldas.get_grid_mask()

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/nldas_grid.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/nldas.ipynb

Next, we use `PyGeoHydro <https://github.com/hyriver/pygeohydro>`__ to get the
geometry of a HUC8 with ID of 1306003, then we get the forcing data within the
obtained geometry.

.. code-block:: python

    from pygeohydro import WBD

    huc8 = WBD("huc8")
    geometry = huc8.byids("huc8", "13060003").geometry[0]
    clm = nldas.get_bygeom(geometry, "2010-01-01", "2010-01-31", 4326)

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/nldas_humidity.png
    :target: https://github.com/hyriver/HyRiver-examples/blob/main/notebooks/nldas.ipynb

Road Map
--------

- [ ] Add PET calculation functions similar to
  `PyDaymet <https://github.com/hyriver/pydaymet>`__ but at hourly timescale.
- [ ] Add a command line interfaces.
