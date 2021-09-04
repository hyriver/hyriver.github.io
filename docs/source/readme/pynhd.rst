PyNHD: Navigate and subset NHDPlus database
-------------------------------------------

.. image:: https://img.shields.io/pypi/v/pynhd.svg
    :target: https://pypi.python.org/pypi/pynhd
    :alt: PyPi

.. image:: https://img.shields.io/conda/vn/conda-forge/pynhd.svg
    :target: https://anaconda.org/conda-forge/pynhd
    :alt: Conda Version

.. image:: https://codecov.io/gh/cheginit/pynhd/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/cheginit/pynhd
    :alt: CodeCov

.. image:: https://img.shields.io/pypi/pyversions/pynhd.svg
    :target: https://pypi.python.org/pypi/pynhd
    :alt: Python Versions

.. image:: https://pepy.tech/badge/pynhd
    :target: https://pepy.tech/project/pynhd
    :alt: Downloads

|

.. image:: https://www.codefactor.io/repository/github/cheginit/pynhd/badge
   :target: https://www.codefactor.io/repository/github/cheginit/pynhd
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

PyNHD is a part of `HyRiver <https://github.com/cheginit/HyRiver>`__ software stack that
is designed to aid in watershed analysis through web services.

This package provides access to
`WaterData <https://labs.waterdata.usgs.gov/geoserver/web/wicket/bookmarkable/org.geoserver.web.demo.MapPreviewPage?1>`__,
the National Map's `NHDPlus HR <https://hydro.nationalmap.gov/arcgis/rest/services/NHDPlus_HR/MapServer>`__,
`NLDI <https://labs.waterdata.usgs.gov/about-nldi/>`__,
and `PyGeoAPI <https://labs.waterdata.usgs.gov/api/nldi/pygeoapi>`__ web services. These web services
can be used to navigate and extract vector data from NHDPlus V2 (both medium- and
hight-resolution) database such as catchments, HUC8, HUC12, GagesII, flowlines, and water bodies.
Moreover, PyNHD gives access to an item on `ScienceBase <https://sciencebase.usgs.gov>`_ called
`Select Attributes for NHDPlus Version 2.1 Reach Catchments and Modified Network Routed Upstream Watersheds for the Conterminous United States <https://www.sciencebase.gov/catalog/item/5669a79ee4b08895842a1d47>`_.
This item provides over 30 attributes at catchment-scale based on NHDPlus ComIDs.
These attributes are available in three categories:

1. Local (`local`): For individual reach catchments,
2. Total (`upstream_acc`): For network-accumulated values using total cumulative drainage area,
3. Divergence (`div_routing`): For network-accumulated values using divergence-routed.

Moreover, the PyGeoAPI service provides four functionalities:

1. ``flow_trace``: Trace flow from a starting point to up/downstream direction.
2. ``split_catchment``: Split the local catchment of a point of interest at the point's location.
3. ``elevation_profile``: Extract elevation profile along a flow path between two points.
4. ``cross_section``: Extract cross-section at a point of interest along a flow line.

A list of these attributes for each characteristic type can be accessed using ``nhdplus_attrs``
function.

Similarly, PyNHD uses `this <https://www.hydroshare.org/resource/6092c8a62fac45be97a09bfd0b0bf726/>`__
item on Hydroshare to get ComID-linked NHDPlus Value Added Attributes. This dataset includes
slope and roughness, among other attributes, for all the flowlines. You can use ``nhdplus_vaa``
function to get this dataset.

Additionally, PyNHD offers some extra utilities for processing the flowlines:

- ``prepare_nhdplus``: For cleaning up the dataframe by, for example, removing tiny networks,
  adding a ``to_comid`` column, and finding a terminal flowlines if it doesn't exist.
- ``topoogical_sort``: For sorting the river network topologically which is useful for routing
  and flow accumulation.
- ``vector_accumulation``: For computing flow accumulation in a river network. This function
  is generic and any routing method can be plugged in.

These utilities are developed based on an ``R`` package called
`nhdplusTools <https://github.com/USGS-R/nhdplusTools>`__.

You can find some example notebooks `here <https://github.com/cheginit/HyRiver-examples>`__.

Please note that since this project is in early development stages, while the provided
functionalities should be stable, changes in APIs are possible in new releases. But we
appreciate it if you give this project a try and provide feedback. Contributions are most welcome.

Moreover, requests for additional functionalities can be submitted via
`issue tracker <https://github.com/cheginit/pynhd/issues>`__.

Installation
------------

You can install PyNHD using ``pip`` after installing ``libgdal`` on your system
(for example, in Ubuntu run ``sudo apt install libgdal-dev``). Moreover, PyNHD has an optional
dependency for using persistent caching, ``requests-cache``. We highly recommend to install
this package as it can significantly speedup send/receive queries. You don't have to change
anything in your code, since PyNHD under-the-hood looks for ``requests-cache`` and if available,
it will automatically use persistent caching:

.. code-block:: console

    $ pip install pynhd

Alternatively, PyNHD can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge pynhd

Quick start
-----------

Let's explore the capabilities of ``NLDI``. We need to instantiate the class first:

.. code:: python

    from pynhd import NLDI, WaterData, NHDPlusHR
    import pynhd as nhd

First, let’s get the watershed geometry of the contributing basin of a
USGS station using ``NLDI``:

.. code:: python

    nldi = NLDI()
    station_id = "01031500"

    basin = nldi.get_basins(station_id)

The ``navigate_byid`` class method can be used to navigate NHDPlus in
both upstream and downstream of any point in the database. Let’s get ComIDs and flowlines
of the tributaries and the main river channel in the upstream of the station.

.. code:: python

    flw_main = nldi.navigate_byid(
        fsource="nwissite",
        fid=f"USGS-{station_id}",
        navigation="upstreamMain",
        source="flowlines",
        distance=1000,
    )

    flw_trib = nldi.navigate_byid(
        fsource="nwissite",
        fid=f"USGS-{station_id}",
        navigation="upstreamTributaries",
        source="flowlines",
        distance=1000,
    )

We can get other USGS stations upstream (or downstream) of the station
and even set a distance limit (in km):

.. code:: python

    st_all = nldi.navigate_byid(
        fsource="nwissite",
        fid=f"USGS-{station_id}",
        navigation="upstreamTributaries",
        source="nwissite",
        distance=1000,
    )

    st_d20 = nldi.navigate_byid(
        fsource="nwissite",
        fid=f"USGS-{station_id}",
        navigation="upstreamTributaries",
        source="nwissite",
        distance=20,
    )

Now, let’s get the
`HUC12 pour points <https://www.sciencebase.gov/catalog/item/5762b664e4b07657d19a71ea>`__:

.. code:: python

    pp = nldi.navigate_byid(
        fsource="nwissite",
        fid=f"USGS-{station_id}",
        navigation="upstreamTributaries",
        source="huc12pp",
        distance=1000,
    )

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/nhdplus_navigation.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nhdplus.ipynb
    :align: center

Also, we can get the slope data for each river segment from NHDPlus VAA database:

.. code:: python

    vaa = nhd.nhdplus_vaa("input_data/nhdplus_vaa.parquet")

    flw_trib["comid"] = pd.to_numeric(flw_trib.nhdplus_comid)
    slope = gpd.GeoDataFrame(
        pd.merge(flw_trib, vaa[["comid", "slope"]], left_on="comid", right_on="comid"),
        crs=flw_trib.crs,
    )
    slope[slope.slope < 0] = np.nan

Now, let's explore the PyGeoAPI capabilities:

.. code:: python

    pygeoapi = PyGeoAPI()

    trace = pygeoapi.flow_trace(
        (1774209.63, 856381.68), crs="ESRI:102003", raindrop=False, direction="none"
    )

    split = pygeoapi.split_catchment((-73.82705, 43.29139), crs="epsg:4326", upstream=False)

    profile = pygeoapi.elevation_profile(
        [(-103.801086, 40.26772), (-103.80097, 40.270568)], numpts=101, dem_res=1, crs="epsg:4326"
    )

    section = pygeoapi.cross_section((-103.80119, 40.2684), width=1000.0, numpts=101, crs="epsg:4326")

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/split_catchment.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/pygeoapi.ipynb
    :align: center

Next, we retrieve the medium- and high-resolution flowlines within the bounding box of our
watershed and compare them. Moreover, Since several web services offer access to NHDPlus database,
``NHDPlusHR`` has an argument for selecting a service and also an argument for automatically
switching between services.

.. code:: python

    mr = WaterData("nhdflowline_network")
    nhdp_mr = mr.bybox(basin.geometry[0].bounds)

    hr = NHDPlusHR("networknhdflowline", service="hydro", auto_switch=True)
    nhdp_hr = hr.bygeom(basin.geometry[0].bounds)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/hr_mr.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nhdplus.ipynb
    :align: center

Moreover, ``WaterData`` can find features within a given radius (in meters) of a point:

.. code:: python

    eck4 = "+proj=eck4 +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
    coords = (-5727797.427596455, 5584066.49330473)
    rad = 5e3
    flw_rad = mr.bydistance(coords, rad, loc_crs=eck4)
    flw_rad = flw_rad.to_crs(eck4)

Instead of getting all features within a radius of the coordinate, we can snap to the closest
flowline using NLDI:

.. code:: python

    comid_closest = nldi.comid_byloc((x, y), eck4)
    flw_closest = nhdp_mr.byid("comid", comid_closest.comid.values[0])


.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/nhdplus_radius.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nhdplus.ipynb
    :align: center

Since NHDPlus HR is still at the pre-release stage let's use the MR flowlines to
demonstrate the vector-based accumulation.
Based on a topological sorted river network
``pynhd.vector_accumulation`` computes flow accumulation in the network.
It returns a dataframe which is sorted from upstream to downstream that
shows the accumulated flow in each node.

PyNHD has a utility called ``prepare_nhdplus`` that identifies such
relationship among other things such as fixing some common issues with
NHDPlus flowlines. But first we need to get all the NHDPlus attributes
for each ComID since ``NLDI`` only provides the flowlines’ geometries
and ComIDs which is useful for navigating the vector river network data.
For getting the NHDPlus database we use ``WaterData``. Let’s use the
``nhdflowline_network`` layer to get required info.

.. code:: python

    wd = WaterData("nhdflowline_network")

    comids = flw_trib.nhdplus_comid.to_list()
    nhdp_trib = wd.byid("comid", comids)
    flw = nhd.prepare_nhdplus(nhdp_trib, 0, 0, purge_non_dendritic=False)

To demonstrate the use of routing, let's use ``nhdplus_attrs`` function to get list of available
NHDPlus attributes

.. code:: python

    char = "CAT_RECHG"
    area = "areasqkm"

    local = nldi.getcharacteristic_byid(comids, "local", char_ids=char)
    flw = flw.merge(local[char], left_on="comid", right_index=True)


    def runoff_acc(qin, q, a):
        return qin + q * a


    flw_r = flw[["comid", "tocomid", char, area]]
    runoff = nhd.vector_accumulation(flw_r, runoff_acc, char, [char, area])


    def area_acc(ain, a):
        return ain + a


    flw_a = flw[["comid", "tocomid", area]]
    areasqkm = nhd.vector_accumulation(flw_a, area_acc, area, [area])

    runoff /= areasqkm

Since these are catchment-scale characteristic, let’s get the catchments
then add the accumulated characteristic as a new column and plot the
results.

.. code:: python

    wd = WaterData("catchmentsp")
    catchments = wd.byid("featureid", comids)

    c_local = catchments.merge(local, left_on="featureid", right_index=True)
    c_acc = catchments.merge(runoff, left_on="featureid", right_index=True)

.. image:: https://raw.githubusercontent.com/cheginit/HyRiver-examples/main/notebooks/_static/flow_accumulation.png
    :target: https://github.com/cheginit/HyRiver-examples/blob/main/notebooks/nhdplus.ipynb
    :align: center

More examples can be found `here <https://pygeohydro.readthedocs.io/en/latest/examples.html>`__.
