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
# NWIS and Plotting
"""

import pydaymet as daymet
import pygeohydro as gh
from pygeohydro import NWIS, plot
from pynhd import NLDI

###############################################################################
# We can explore the available NWIS stations within a bounding box using ``interactive_map`` function. It returns an interactive map and by clicking on an station some of the most important properties of stations are shown so you can decide which station(s) to choose from.

bbox = (-69.5, 45, -69, 45.5)
gh.interactive_map(bbox)

###############################################################################
# We can more information about the station using the ``get_info`` function from ``NWIS`` class.

nwis = NWIS()
info_box = nwis.get_info(nwis.query_bybox(bbox))

###############################################################################
# Now, let's select all the stations that their daily mean streamflow data are available between 2000-01-01 and 2010-12-31.

dates = ("2000-01-01", "2010-12-31")
stations = info_box[
    (info_box.begin_date <= dates[0]) & (info_box.end_date >= dates[1])
].site_no.tolist()

###############################################################################
# One of the useful information in the database in Hydro-Climatic Data Network - 2009 (HCDN-2009) flag. This flag shows whether the station is natural (True) or affected by human activities (False). If an station is not available in the HCDN dataset `None` is returned.

info = nwis.get_info(nwis.query_byid(stations), expanded=True)
info.set_index("site_no").hcdn_2009

###############################################################################
# We can get the daily mean streamflow for these stations using the ``get_streamflow`` function. This function has a flag to return the data mm/day rather than the default `cms` which is useful for hydrolgy models and plotting hydrologic signatures.

qobs = nwis.get_streamflow(stations, dates, mmd=True)

###############################################################################
# Then we can use the ``signatures`` function to plot hydrologic signatures of the streamflow. Note that the input time series should be in mm/day. This function has argument, `output`, for saving the plot as a `png` file.

plot.signatures(qobs, output="_static/example_plots_signatures.png")

###############################################################################
# This function also can show precipitation data as a bar plot. Let's use [PyDaymet](https://github.com/cheginit/pydaymet) to get the precipitation at the NWIS stations location.

sid = "01031500"
coords = tuple(info[info.site_no == sid][["dec_long_va", "dec_lat_va"]].to_numpy()[0])
prcp = daymet.get_byloc(coords, dates, variables="prcp")

""
plot.signatures(
    qobs[f"USGS-{sid}"], prcp, title=f"Streamflow Observations for USGS-{sid}"
)
