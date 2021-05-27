.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/hyriver_logo_text.png
    :target: https://github.com/cheginit/HyRiver-examples

|

.. |pygeohydro| image:: https://github.com/cheginit/pygeohydro/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/pygeohydro/actions/workflows/test.yml
    :alt: Github Actions

.. |pygeoogc| image:: https://github.com/cheginit/pygeoogc/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/pygeoogc/actions/workflows/test.yml
    :alt: Github Actions

.. |pygeoutils| image:: https://github.com/cheginit/pygeoutils/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/pygeoutils/actions/workflows/test.yml
    :alt: Github Actions

.. |pynhd| image:: https://github.com/cheginit/pynhd/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/pynhd/actions/workflows/test.yml
    :alt: Github Actions

.. |py3dep| image:: https://github.com/cheginit/py3dep/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/py3dep/actions/workflows/test.yml
    :alt: Github Actions

.. |pydaymet| image:: https://github.com/cheginit/pydaymet/actions/workflows/test.yml/badge.svg
    :target: https://github.com/cheginit/pydaymet/actions/workflows/test.yml
    :alt: Github Actions

.. |pygeohydro_stat| image:: https://pepy.tech/badge/hydrodata
    :target: https://pepy.tech/project/hydrodata
    :alt: Download Stat

.. |pygeoogc_stat| image:: https://pepy.tech/badge/pygeoogc
    :target: https://pepy.tech/project/pygeoogc
    :alt: Download Stat

.. |pygeoutils_stat| image:: https://pepy.tech/badge/pygeoutils
    :target: https://pepy.tech/project/pygeoutils
    :alt: Download Stat

.. |pynhd_stat| image:: https://pepy.tech/badge/pynhd
    :target: https://pepy.tech/project/pynhd
    :alt: Download Stat

.. |py3dep_stat| image:: https://pepy.tech/badge/py3dep
    :target: https://pepy.tech/project/py3dep
    :alt: Download Stat

.. |pydaymet_stat| image:: https://pepy.tech/badge/pydaymet
    :target: https://pepy.tech/project/pydaymet
    :alt: Download Stat

.. _PyGeoHydro: https://github.com/cheginit/pygeohydro
.. _PyGeoOGC: https://github.com/cheginit/pygeoogc
.. _PyGeoUtils: https://github.com/cheginit/pygeoutils
.. _PyNHD: https://github.com/cheginit/pynhd
.. _Py3DEP: https://github.com/cheginit/py3dep
.. _PyDaymet: https://github.com/cheginit/pydaymet

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

.. image:: https://readthedocs.org/projects/hyriver/badge/?version=latest
    :target: https://hyriver.readthedocs.io/en/latest/?badge=latest
    :alt: ReadTheDocs

.. image:: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77/status.svg
    :target: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77
    :alt: JOSS

=========== ==================================================================== =================
Package     Description                                                          Status
=========== ==================================================================== =================
PyNHD_      Navigate and subset NHDPlus (MR and HR) using web services           |pynhd|
Py3DEP_     Access topographic data through National Map's 3DEP web service      |py3dep|
PyGeoHydro_ Access NWIS, NID, HCDN 2009, NLCD, and SSEBop databases              |pygeohydro|
PyDaymet_   Access Daymet for daily climate data both single pixel and gridded   |pydaymet|
PyGeoOGC_   Send queries to any ArcGIS RESTful-, WMS-, and WFS-based services    |pygeoogc|
PyGeoUtils_ Convert responses from PyGeoOGC's supported web services to datasets |pygeoutils|
=========== ==================================================================== =================


HyRiver: Hydroclimate Data Retriever
=====================================

.. note::

    This software stack was formerly named `hydrodata <https://pypi.org/project/hydrodata>`__.
    Since an `R <https://github.com/mikejohnson51/HydroData>`__ package with the same name
    already exists, we decided to renamed our project to
    HyRiver.

Features
--------

`HyRiver <https://hyriver.readthedocs.io>`__ is a software stack consisting of seven
Python libraries that are designed to aid in watershed analysis through web services.
Currently, this project only includes hydrology and climatology data
within the US. Some of the major capabilities of HyRiver are as follows:

* Easy access to many web services for subsetting data on server-side and returning the requests
  as masked Datasets or GeoDataFrames.
* Splitting large requests into smaller chunks, under-the-hood, since web services often limit
  the number of features per request. So the only bottleneck for subsetting the data
  is your local machine memory.
* Navigating and subsetting NHDPlus database (both medium- and high-resolution) using web services.
* Cleaning up the vector NHDPlus data, fixing some common issues, and computing vector-based
  accumulation through a river network.
* A URL inventory for some of the popular (and tested) web services.
* Some utilities for manipulating the obtained data and their visualization.

Please visit `examples <https://hyriver.readthedocs.io/en/latest/examples.html>`__
webpage to see some example notebooks. You can also try this project without installing
it on you system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver software stack pre-installed will be launched in your web browser
and you can start coding!

Please note that this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional databases and functionalities can be submitted via issue trackers
of packages.

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/flow_accumulation.png
    :target: https://github.com/cheginit/HyRiver-examples

Installation
------------

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install py3de pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever

or ``conda``:

.. code-block:: console

    $ conda install -c conda-forge py3de pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever

or ``mamba`` (recommended):

.. code-block:: console

    $ mamba install -c conda-forge --strict-channel-priority py3de pynhd pygeohydro pydaymet pygeoogc pygeoutils async_retriever
