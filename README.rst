.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/hyriver_logo_text.png
    :target: https://github.com/hyriver/HyRiver-examples

|

.. |geoh_stat| image:: https://static.pepy.tech/personalized-badge/pygeohydro?period=total&left_color=blue&right_color=yellowgreen&left_text=PyGeoHydro
    :target: https://github.com/hyriver/pygeohydro
    :alt: Download Stat

.. |ogc_stat| image:: https://static.pepy.tech/personalized-badge/pygeoogc?period=total&left_color=blue&right_color=yellowgreen&left_text=PyGeoOGC
    :target: https://github.com/hyriver/pygeoogc
    :alt: Download Stat

.. |utils_stat| image:: https://static.pepy.tech/personalized-badge/pygeoutils?period=total&left_color=blue&right_color=yellowgreen&left_text=PyGeoUtils
    :target: https://github.com/hyriver/pygeoutils
    :alt: Download Stat

.. |nhd_stat| image:: https://static.pepy.tech/personalized-badge/pynhd?period=total&left_color=blue&right_color=yellowgreen&left_text=PyNHD
    :target: https://github.com/hyriver/pynhd
    :alt: Download Stat

.. |3dep_stat| image:: https://static.pepy.tech/personalized-badge/py3dep?period=total&left_color=blue&right_color=yellowgreen&left_text=Py3DEP
    :target: https://github.com/hyriver/py3dep
    :alt: Download Stat

.. |day_stat| image:: https://static.pepy.tech/personalized-badge/pydaymet?period=total&left_color=blue&right_color=yellowgreen&left_text=PyDaymet
    :target: https://github.com/hyriver/pydaymet
    :alt: Download Stat

.. |grid_stat| image:: https://static.pepy.tech/personalized-badge/pygridmet?period=total&left_color=blue&right_color=yellowgreen&left_text=PyGridMET
    :target: https://github.com/hyriver/pygridmet
    :alt: Download Stat

.. |nldas_stat| image:: https://static.pepy.tech/personalized-badge/pynldas2?period=total&left_color=blue&right_color=yellowgreen&left_text=PyNLDAS2
    :target: https://github.com/hyriver/pynldas2
    :alt: Download Stat

.. |async_stat| image:: https://static.pepy.tech/personalized-badge/async-retriever?period=total&left_color=blue&right_color=yellowgreen&left_text=AsyncRetriever
    :target: https://github.com/hyriver/async-retriever
    :alt: Download Stat

.. |sig_stat| image:: https://static.pepy.tech/personalized-badge/hydrosignatures?period=total&left_color=blue&right_color=yellowgreen&left_text=HydroSignatures
    :target: https://github.com/hyriver/hydrosignatures
    :alt: Download Stat

.. _PyGeoHydro: https://github.com/hyriver/pygeohydro
.. _PyGeoOGC: https://github.com/hyriver/pygeoogc
.. _PyGeoUtils: https://github.com/hyriver/pygeoutils
.. _PyNHD: https://github.com/hyriver/pynhd
.. _Py3DEP: https://github.com/hyriver/py3dep
.. _PyDaymet: https://github.com/hyriver/pydaymet
.. _PyGridMET: https://github.com/hyriver/pygridmet
.. _PyNLDAS2: https://github.com/hyriver/pynldas2
.. _HydroSignatures: https://github.com/hyriver/hydrosignatures

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

.. image:: https://github.com/hyriver/hyriver.github.io/actions/workflows/gh-pages.yml/badge.svg
    :target: https://github.com/hyriver/hyriver.github.io/actions/workflows/gh-pages.yml
    :alt: Build Website

.. image:: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77/status.svg
    :target: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77
    :alt: JOSS

=============== ====================================================================
Package         Description
=============== ====================================================================
|nhd_stat|      Navigate and subset NHDPlus (MR and HR) using web services
|3dep_stat|     Access topographic data through National Map's 3DEP web service
|geoh_stat|     Access NWIS, NID, WQP, eHydro, NLCD, CAMELS, and SSEBop databases
|day_stat|      Access daily, monthly, and annual climate data via Daymet
|grid_stat|     Access daily climate data via GridMet
|nldas_stat|    Access hourly NLDAS-2 data via web services
|sig_stat|      A collection of tools for computing hydrological signatures
|async_stat|    High-level API for asynchronous requests with persistent caching
|ogc_stat|      Send queries to any ArcGIS RESTful-, WMS-, and WFS-based services
|utils_stat|    Utilities for manipulating geospatial, (Geo)JSON, and (Geo)TIFF data
=============== ====================================================================


HyRiver: Hydroclimate Data Retriever
====================================

Features
--------

`HyRiver <https://docs.hyriver.io>`__ is a software stack consisting of ten
Python libraries that are designed to aid in hydroclimate analysis through web services.
Currently, this project only includes hydrology and climatology data
within the US. Some major capabilities of HyRiver are:

* Easy access to many web services for subsetting data on server-side and returning the requests
  as masked Datasets or GeoDataFrames.
* Splitting large requests into smaller chunks, under-the-hood, since web services often limit
  the number of features per request. So the only bottleneck for subsetting the data
  is your local machine memory.
* Navigating and subsetting NHDPlus database (both medium- and high-resolution) using web services.
* Cleaning up the vector NHDPlus data, fixing some common issues, and computing vector-based
  accumulation through a river network.
* A URL inventory for many popular (and tested) web services.
* Some utilities for manipulating the obtained data and their visualization.

.. image:: https://docs.hyriver.io/_images/hyriver_deps.png
    :target: https://docs.hyriver.io

Please visit `examples <https://docs.hyriver.io/examples.html>`__
webpage to see some example notebooks. You can also watch these videos for a quick overview
of ``HyRiver`` capabilities:

* `Pangeo Showcase <https://discourse.pangeo.io/t/may-26-2021-accessing-hydrology-and-climatology-database-using-web-services-through-python/1521>`__
* `ESIP IT&I <https://youtu.be/Wz8Y5G9oy-M?t=1838>`__
* `WaterHackWeek 2020 <https://www.youtube.com/watch?v=VRQ_Tk49s5Y>`__
* `UH Seminar <https://www.youtube.com/watch?v=RSyFv9AfUb8>`__

You can also try this project without installing it on your system by clicking on the binder
badge. A Jupyter Lab instance with the HyRiver software stack pre-installed will be launched
in your web browser, and you can start coding!

Please note that this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional databases and functionalities can be submitted via issue trackers
of packages.

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

You can install all the packages using ``pip``:

.. code-block:: console

    $ pip install py3dep pynhd pygeohydro pydaymet pygridmet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

Please note that installation with ``pip`` fails if ``libgdal`` is not installed on your system.
You should install this package manually beforehand. For example, on Ubuntu-based distros
the required package is ``libgdal-dev``. If this package is installed on your system
you should be able to run ``gdal-config --version`` successfully.

Alternatively, you can install them using ``conda``:

.. code-block:: console

    $ conda install -c conda-forge py3dep pynhd pygeohydro pydaymet pygridmet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

or ``micromamba`` (recommended):

.. code-block:: console

    $ micromamba install py3dep pynhd pygeohydro pydaymet pygridmet pynldas2 hydrosignatures pygeoogc pygeoutils async-retriever

Additionally, you can create a new environment, named ``hyriver`` with all the packages
and optional dependencies installed with ``micromamba`` using the provided
``environment.yml`` file:

.. code-block:: console

    $ mamba env create -f ./environment.yml

.. image:: https://raw.githubusercontent.com/hyriver/HyRiver-examples/main/notebooks/_static/flow_accumulation.png
    :target: https://github.com/hyriver/HyRiver-examples
