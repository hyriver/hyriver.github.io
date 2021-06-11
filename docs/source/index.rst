.. |async| image:: https://img.shields.io/pypi/v/async_retriever?label=AsyncRetriever&color=green
    :target: https://github.com/cheginit/async_retriever
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

.. |async_stat| image:: https://pepy.tech/badge/async_retriever
    :target: https://pepy.tech/project/async_retriever

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


Hydroclimate Data Retriever
===========================

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

.. image:: https://readthedocs.org/projects/hyriver/badge/?version=latest
    :target: https://hyriver.readthedocs.io/en/latest/?badge=latest
    :alt: ReadTheDocs

.. image:: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77/status.svg
    :target: https://joss.theoj.org/papers/b0df2f6192f0a18b9e622a3edff52e77
    :alt: JOSS

|

`HyRiver <https://hyriver.readthedocs.io>`__ (formerly named
`hydrodata <https://pypi.org/project/hydrodata>`__) is a software stack
consisting of seven Python libraries that are designed to aid in watershed
analysis through web services. Currently, this project only includes hydrology
and climatology data within the US.

You can watch this videos for a quick overview of ``HyRiver``:

* `Pangeo Showcase <https://discourse.pangeo.io/t/may-26-2021-accessing-hydrology-and-climatology-database-using-web-services-through-python/1521>`__

.. toctree::
    :maxdepth: 1
    :hidden:

    getting_started
    examples

.. toctree::
    :maxdepth: 1
    :hidden:

    autoapi/index
    history
    contributing
    authors
    license


.. panels::
    :column: col-lg-12 p-2

    **High-level APIs for accessing some pre-configured web services**
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. tabbed:: PyNHD

        Navigate and subset mid- and high-res NHD, NHDPlus, and NHDPlus VAA
        using WaterData, NLDI, ScienceBase, and The National Map web services.

        |pynhd| |pynhd_stat|

    .. tabbed:: PyGeoHydro

        Access NWIS, NID, HCDN 2009, NLCD, and SSEBop databases.

        |pygeohydro| |pygeohydro_stat|

    .. tabbed:: Py3DEP

        Access topographic data through The National Map's 3DEP web service.

        |py3dep| |py3dep_stat|

    .. tabbed:: PyDaymet

        Access Daymet for daily, monthly and annual summaries of climate data
        at 1-km scale for both single pixels and gridded.

        |pydaymet| |pydaymet_stat|

.. panels::
    :column: col-lg-12 p-2

    **Low-level APIs for connecting to supported web service protocols**
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. tabbed:: PyGeoOGC

        Send queries to and receive responses from any ArcGIS RESTful-, WMS-,
        and WFS-based services.

        |pygeoogc| |pygeoogc_stat|

    .. tabbed:: PyGeoUtils

        Convert responses from PyGeoOGC's supported web services protocols into
        geospatial and raster datasets.

        |pygeoutils| |pygeoutils_stat|

    .. tabbed:: AsyncRetriever

        Asynchronous send/receive requests with persistent caching.

        |async| |async_stat|
