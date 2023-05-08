.. |async| image:: https://img.shields.io/pypi/v/async-retriever?label=AsyncRetriever&color=green
    :target: https://github.com/cheginit/async-retriever
    :alt: PyPi Version

.. |pygeohydro| image:: https://img.shields.io/pypi/v/pygeohydro?label=PyGeoHydro&color=green
    :target: https://github.com/cheginit/pygeohydro
    :alt: PyPi Version

.. |pygeoogc| image:: https://img.shields.io/pypi/v/pygeoogc?label=PyGeoOGC&color=green
    :target: https://github.com/cheginit/pygeoogc
    :alt: PyPi Version

.. |pygeoutils| image:: https://img.shields.io/pypi/v/pygeoutils?label=PyGeoUtils&color=green
    :target: https://github.com/cheginit/pygeoutils
    :alt: PyPi Version

.. |pynhd| image:: https://img.shields.io/pypi/v/pynhd?label=PyNHD&color=green
    :target: https://github.com/cheginit/pynhd
    :alt: PyPi Version

.. |py3dep| image:: https://img.shields.io/pypi/v/py3dep?label=Py3DEP&color=green
    :target: https://github.com/cheginit/py3dep
    :alt: PyPi Version

.. |pydaymet| image:: https://img.shields.io/pypi/v/pydaymet?label=PyDaymet&color=green
    :target: https://github.com/cheginit/pydaymet
    :alt: PyPi Version

.. |pynldas2| image:: https://img.shields.io/pypi/v/pynldas2?label=PyDaymet&color=green
    :target: https://github.com/cheginit/pynldas2
    :alt: PyPi Version

.. |signatures| image:: https://img.shields.io/pypi/v/hydrosignatures?label=HydroSignatures&color=green
    :target: https://github.com/cheginit/hydrosignatures
    :alt: PyPi Version

.. |async_stat| image:: https://pepy.tech/badge/async-retriever
    :target: https://pepy.tech/project/async-retriever

.. |pygeohydro_stat| image:: https://pepy.tech/badge/pygeohydro
    :target: https://pepy.tech/project/pygeohydro
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

.. |pynldas2_stat| image:: https://pepy.tech/badge/pynldas2
    :target: https://pepy.tech/project/pynldas2
    :alt: Download Stat

.. |sig_stat| image:: https://static.pepy.tech/personalized-badge/hydrosignatures?period=total&left_color=blue&right_color=yellowgreen&left_text=HydroSignatures
    :target: https://github.com/hyriver/hydrosignatures
    :alt: Download Stat

Hydroclimate Data Retriever
===========================

.. image:: https://img.shields.io/pypi/pyversions/pygeoogc.svg
    :target: https://pypi.python.org/pypi/pygeoogc
    :alt: Python Versions

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

.. image:: https://github.com/hyriver/hyriver.github.io/actions/workflows/gh-pages.yml/badge.svg
    :target: https://github.com/hyriver/hyriver.github.io/actions/workflows/gh-pages.yml
    :alt: Build Website

.. image:: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77/status.svg
    :target: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77
    :alt: JOSS

|

`HyRiver <https://hyriver.readthedocs.io>`__ (formerly named
`hydrodata <https://pypi.org/project/hydrodata>`__) is a suite of Python packages
that provides a unified API for retrieving geospatial/temporal data from various
web services. HyRiver includes two categories of packages:

- Low-level APIs for accessing any of the supported web services, i.e., ArcGIS RESTful,
  WMS, and WFS.
- High-level APIs for accessing some of the most commonly used datasets in hydrology and
  climatology studies. Currently, this project only includes hydrology and climatology data
  within the US.

You can watch these videos for a quick overview of HyRiver capabilities:

.. include:: videos-gallery.txt

Citation
========

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

.. grid::

    .. grid-item-card:: High-level APIs for accessing some pre-configured web services

        .. tab-set::

            .. tab-item:: PyNHD

                Navigate and subset mid- and high-res NHD, NHDPlus, and NHDPlus VAA
                using WaterData, NLDI, ScienceBase, and The National Map web services.

                |pynhd| |pynhd_stat|

            .. tab-item:: PyGeoHydro

                Access NWIS, NID, HCDN 2009, NLCD, and SSEBop databases.

                |pygeohydro| |pygeohydro_stat|

            .. tab-item:: Py3DEP

                Access topographic data through The National Map's 3DEP web service.

                |py3dep| |py3dep_stat|

            .. tab-item:: PyDaymet

                Access Daymet for daily, monthly and annual summaries of climate data
                at 1-km scale for both single pixels and gridded.

                |pydaymet| |pydaymet_stat|

            .. tab-item:: PyNLDAS2

                Access hourly NLDAS-2 forcing data.

                |pynldas2| |pynldas2_stat|

            .. tab-item:: HydroSignatures

                A collection of tools for computing hydrological signatures

                |signatures| |sig_stat|

.. grid::

    .. grid-item-card:: Low-level APIs for connecting to supported web service protocols

        .. tab-set::

            .. tab-item:: PyGeoOGC

                Send queries to and receive responses from any ArcGIS RESTful-, WMS-,
                and WFS-based services.

                |pygeoogc| |pygeoogc_stat|

            .. tab-item:: PyGeoUtils

                Convert responses from PyGeoOGC's supported web services protocols into
                geospatial and raster datasets.

                |pygeoutils| |pygeoutils_stat|

            .. tab-item:: AsyncRetriever

                Asynchronous send/receive requests with persistent caching.

                |async| |async_stat|

.. toctree::
    :maxdepth: 1
    :hidden:

    getting_started
    readmes
    examples

.. toctree::
    :maxdepth: 1
    :hidden:

    autoapi/index
    changelogs
    contributing
    authors
    license
