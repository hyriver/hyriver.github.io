# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: sphinx
#       format_version: '1.1'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

"""
# NLCD
"""

import pygeohydro as gh
from pynhd import NLDI

""
import warnings

warnings.filterwarnings("ignore")

###############################################################################
# Land cover, imperviousness, and canopy data can be retrieved from the [NLCD](https://www.mrlc.gov/data) database. First, we use [PyNHD](https://github.com/cheginit/pynhd) to get the contributing watershed geometry of a NWIS station with the ID of `USGS-01031500`:

geometry = NLDI().get_basins("01031500").geometry[0]

###############################################################################
# We can now use the ``nlcd`` function to get the data. This function has one positional argumnet for passing the geometry which could be a Polygon or a boundig box. If CRS of the geometry is not EPSG:4326, it should be passed via ``geo_crs`` argument. The second argumnet is the target resolution of the data in meters. The NLCD database is multi-resolution and based on the target resolution, the source data are resampled on the server side.
#
# You should be mindful of the resolution since higher resolutions require more memory so if your requests requires more memory than the avialable memory on your system the code is likely to crash. You can either increase the resolution or divide your region of interest into smaller regions.
#
# Moreover, the [MRLC](https://www.mrlc.gov/geoserver/web/) GeoServer has a limit of about 8 million pixels per request but PyGeoHydro takes care of the domain decomposition under-the-hood and divides the request to smaller requests then merges them. So the only bottleneck for requests is the amount of available memory on your system.
#
# The ``nlcd`` function can request for three layers from the MRLC web service; imperviousness, land use/land cover, and tree canopy. Since NLCD is released every couple of years, you can specify the target year via the ``years`` argument. By default it is 2016. You can set any of the years to ``None`` to turn off that layer.
#
# Let's get the cover data at a 100 m resolution.

lulc = gh.nlcd(geometry, 100, years={"impervious": None, "cover": 2016, "canopy": None})

###############################################################################
# Additionaly, PyGeoHydro provides a function for getting the official legends of the cover data. Let's plot the data using this legends.

cmap, norm, levels = gh.plot.cover_legends()
ax = lulc.cover.plot(
    size=5, cmap=cmap, levels=levels, cbar_kwargs={"ticks": levels[:-1]}
)
ax.figure.savefig("_static/lulc.png", bbox_inches="tight", dpi=100)

###############################################################################
# Moreover, we can get the statistics of the cover data for each class or category as well:

stats = gh.cover_statistics(lulc.cover)
stats
