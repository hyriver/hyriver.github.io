PyGeoHydro: Retrieve Geospatial Hydrology Data
----------------------------------------------

.. image:: https://img.shields.io/pypi/v/pygeohydro.svg
    :target: https://pypi.python.org/pypi/pygeohydro
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pygeohydro.svg
    :target: https://anaconda.org/conda-forge/pygeohydro
    :alt: Conda Version

.. image:: https://codecov.io/gh/cheginit/pygeohydro/graph/badge.svg
    :target: https://codecov.io/gh/cheginit/pygeohydro
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pygeohydro.svg
    :target: https://pypi.python.org/pypi/pygeohydro
    :alt: Python Versions

.. image:: https://pepy.tech/badge/hydrodata
    :target: https://pepy.tech/project/hydrodata
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/cheginit/pygeohydro/badge/main
    :target: https://www.codefactor.io/repository/github/cheginit/pygeohydro/overview/main
    :alt: CodeFactor

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks
    :alt: Binder

|

Features
--------

PyGeoHydro (formerly named `hydrodata <https://pypi.org/project/hydrodata>`__) is a part of
`HyRiver <https://github.com/cheginit/HyRiver>`__ software stack that
is designed to aid in watershed analysis through web services. This package provides
access to some of the public web services that offer geospatial hydrology data. It has three
main modules: ``pygeohydro``, ``plot``, and ``helpers``.

The ``pygeohydro`` module can pull data from the following web services:

* `NWIS <https://nwis.waterdata.usgs.gov/nwis>`__ for daily mean streamflow observations,
* `NID <https://damsdev.net/>`__ for accessing the National Inventory of Dams in the US,
* `HCDN 2009 <https://www2.usgs.gov/science/cite-view.php?cite=2932>`__ for identifying sites
  where human activity affects the natural flow of the watercourse,
* `NLCD 2019 <https://www.mrlc.gov/>`__ for land cover/land use, imperviousness, imperviousness
  descriptor, and canopy data,
* `SSEBop <https://earlywarning.usgs.gov/ssebop/modis/daily>`__ for daily actual
  evapotranspiration, for both single pixel and gridded data.

Also, it has two other functions:

* ``interactive_map``: Interactive map for exploring NWIS stations within a bounding box.
* ``cover_statistics``: Categorical statistics of land use/land cover data.

The ``plot`` module includes two main functions:

* ``signatures``: Hydrologic signature graphs.
* ``cover_legends``: Official NLCD land cover legends for plotting a land cover dataset.
* ``descriptor_legends``: Color map and legends for plotting a imperviousness descriptor dataset.

The ``helpers`` module includes:

* ``nlcd_helper``: A roughness coefficients lookup table for each land cover and imperviousness
  descriptortype which is useful for overland flow routing among other applications.
* ``nwis_error``: A dataframe for finding information about NWIS requests' errors.

Moreover, requests for additional databases and functionalities can be submitted via
`issue tracker <https://github.com/cheginit/pygeohydro/issues>`__.

You can find some example notebooks `here <https://github.com/cheginit/HyRiver-examples>`__.

You can also try using PyGeoHydro without installing
it on you system by clicking on the binder badge. A Jupyter Lab
instance with the HyRiver stack pre-installed will be launched in your web browser
and you can start coding!

Please note that since this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/cheginit/pygeohydro/issues>`__.

Installation
------------

You can install PyGeoHydro using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``). Moreover, PyGeoHydro has an optional
dependency for using persistent caching, ``requests-cache``. We highly recommend to install
this package as it can significantly speedup send/receive queries. You don't have to change
anything in your code, since PyGeoHydro under-the-hood looks for ``requests-cache`` and
if available, it will automatically use persistent caching:

.. code-block:: console

    $ pip install pygeohydro

Alternatively, PyGeoHydro can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pygeohydro

Quick start
-----------

We can explore the available NWIS stations within a bounding box using ``interactive_map``
function. It returns an interactive map and by clicking on an station some of the most
important properties of stations are shown.

.. code-block:: python

    import pygeohydro as gh

    bbox = (-69.5, 45, -69, 45.5)
    gh.interactive_map(bbox)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/interactive_map.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nwis.ipynb
    :width: 400
    :alt: Interactive Map

We can select all the stations within this boundary box that have daily mean streamflow data from
2000-01-01 to 2010-12-31:

.. code-block:: python

    from pygeohydro import NWIS

    nwis = NWIS()
    query = {
        **nwis.query_bybox(bbox),
        "hasDataTypeCd": "dv",
        "outputDataTypeCd": "dv",
    }
    info_box = nwis.get_info(query)
    dates = ("2000-01-01", "2010-12-31")
    stations = info_box[
        (info_box.begin_date <= dates[0]) & (info_box.end_date >= dates[1])
    ].site_no.tolist()

Then, we can get the streamflow data in mm/day (by default the data are in cms) and plot them:

.. code-block:: python

    from pygeohydro import plot

    qobs = nwis.get_streamflow(stations, dates, mmd=True)
    plot.signatures(qobs)

Moreover, we can get land use/land cove data using ``nlcd`` function, percentages of
land cover types using ``cover_statistics``, and actual ET with ``ssebopeta_bygeom``:

.. code-block:: python

    from pynhd import NLDI

    geometry = NLDI().get_basins("01031500").geometry[0]
    lulc = gh.nlcd(geometry, 100, years={"cover": [2016, 2019]})
    stats = gh.cover_statistics(lulc.cover_2016)
    eta = gh.ssebopeta_bygeom(geometry, dates=("2005-10-01", "2005-10-05"))

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/lulc.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nlcd.ipynb
    :width: 200
    :alt: Land Use/Land Cover

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/eta.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/ssebop.ipynb
    :width: 200
    :alt: Actual ET

Additionally, we can pull all the US dams data using ``NID``. Let's get dams that are within this
bounding box and have a maximum storage larger than 200 acre-feet.

.. code-block:: python

    nid = NID()
    dams = nid.bygeom(bbox, "epsg:4326", sql_clause="MAX_STORAGE > 200")

We can get all the dams within CONUS using ``NID`` and plot them:
.. code-block:: python

    import geopandas as gpd

    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    conus = world[world.name == "United States of America"].geometry.iloc[0][0]
    conus_dams = nid.bygeom(conus, "epsg:4326")


.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/dams.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nid.ipynb
    :width: 400
    :alt: Dams
