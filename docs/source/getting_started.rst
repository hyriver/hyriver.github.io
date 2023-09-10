.. highlight:: bash

===============
Getting Started
===============

Why HyRiver?
------------

Some major capabilities of HyRiver are as follows:

* Easy access to many web services for subsetting data on server-side and returning the requests
  as masked Datasets or GeoDataFrames.
* Splitting large requests into smaller chunks, under-the-hood, since web services often limit
  the number of features per request. So the only bottleneck for subsetting the data
  is your local machine memory.
* Navigating and subsetting NHDPlus database (both medium- and high-resolution) using web services.
* Cleaning up the vector NHDPlus data, fixing some common issues, and computing vector-based
  accumulation through a river network.
* A URL inventory for some popular (and tested) web services.
* Some utilities for manipulating the obtained data and their visualization.

Installation
------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install py3dep pynhd pygeohydro pydaymet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can install them using ``conda``:

.. code-block:: console

    $ conda install -c conda-forge py3dep pynhd pygeohydro pydaymet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

or ``mambaforge`` (recommended):

.. code-block:: console

    $ mamba install py3dep pynhd pygeohydro pydaymet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

Additionally, you can create a new environment, named ``hyriver`` with all the packages
and optional dependencies installed with ``mambaforge`` using the provided
``environment.yml`` file:

.. code-block:: console

    $ mamba env create -f ./environment.yml

Dependencies
------------

.. include:: dependencies.txt

Additionally, you can also install ``bottleneck`` and ``numba`` to improve
the performance of some computations. Installing ``pyogrio`` is highly recommended
for improving the performance of working with vector data. For NHDPlus, ``py7zr``
and ``pyogrio`` are required dependencies. For retrieving soil
data, you should install ``planetary-computer`` and ``pystac-client``.
