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
# Spatiotemporal Distribution of Dams
"""

import os
import pickle
import shutil

import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import pygeohydro as gh
from matplotlib.font_manager import fontManager
from tqdm.auto import tqdm

"""
Get the data from the [National Inventory of Dams](https://nid.sec.usace.army.mil) using [PyGeoHydro](https://github.com/cheginit/pygeohydro) package.
"""

try:
    with open("input_data/nid.pkl", "rb") as f:
        nid = pickle.load(f)
except FileNotFoundError:
    nid = gh.get_nid()

###############################################################################
# Since we're going to use dam coordinates and completion year to filter the data, let's check number of missing data to find the total available dams that include these two data.

missing = (
    nid[nid.geometry.x > -60].shape[0]
    + nid[nid.geometry.y < 10].shape[0]
    + nid.geometry.isna().sum()
    + nid.YEAR_COMPLETED.isna().sum()
)
nid.shape[0] - missing

###############################################################################
# Let's plot the number of missing data by state.

ax = (
    nid[
        (nid.geometry.x > -60)
        | (nid.geometry.y < 10)
        | nid.geometry.isna()
        | nid.YEAR_COMPLETED.isna()
    ]
    .groupby("STATE")
    .size()
    .plot.bar(figsize=(20, 5))
)
ax.set_title("Number of dams with missing coordinate or completion year data")
for p in ax.patches:
    ax.annotate(
        p.get_height(),
        (p.get_x() + p.get_width() / 2, p.get_height() + 70),
        ha="center",
        va="center",
    )
ax.figure.set_dpi(300)

###############################################################################
# Filter the data to only include dams that are within Contiguous US.

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
conus = world[world.name == "United States of America"].geometry.iloc[0][0]
conus = gpd.GeoDataFrame({"FID": [0], "geometry": conus}, crs=world.crs)
nid_conus = nid[nid.within(conus.to_crs(nid.crs).geometry[0])]

###############################################################################
# Plot the frames.

column = "DAM_HEIGHT"
cmap = "viridis"
min_q, max_q = 0.1, 0.9

label = f"{column.replace('_', ' ').title()} ({nid.attrs[column].split(',', 1)[0][1:].lower()})"
label = "\n".join([label, f"{min_q} - {max_q} Quantile"])
norm = plt.Normalize(
    vmin=nid_conus[column].quantile(min_q), vmax=nid_conus[column].quantile(max_q)
)

dpi = 250.0
figsize = (1920.0 / dpi, 1080.0 / dpi)
font = "Lato"
indent = "\n        "
if font in {f.name for f in fontManager.ttflist}:
    matplotlib.rcParams["font.sans-serif"] = font
    matplotlib.rcParams["font.family"] = "sans-serif"
plt.ioff()

os.makedirs("tmp", exist_ok=True)


def get_ax():
    ax = conus.plot(figsize=figsize, facecolor="none", edgecolor="k")
    ax.axis(False)
    fig = ax.figure
    fig.set_dpi(dpi)
    cax = fig.add_axes(
        [
            ax.get_position().x1 + 0.01,
            ax.get_position().y0,
            0.02,
            ax.get_position().height,
        ]
    )
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    fig.colorbar(sm, cax=cax, label=label)
    return ax


years = range(nid_conus.YEAR_COMPLETED.min() + 1, nid_conus.YEAR_COMPLETED.max() + 1)
with tqdm(total=len(years), desc="Plotting") as pbar:
    for year in years:
        pbar.set_postfix_str(f"Year: {year}")
        dams = nid_conus[nid_conus.YEAR_COMPLETED <= year]
        ax = get_ax()
        dams.plot(
            ax=ax,
            column=column,
            cmap=cmap,
            norm=norm,
            alpha=0.3,
            markersize=3,
        )
        ax.set_title(f"Dams Completed Up to {year}\nTotal = {len(dams):,}")
        h_max = dams[column].max()
        name_max = dams.iloc[dams[column].argmax()].DAM_NAME.title()
        ax.annotate(
            f"Largest Dam:{indent}Height: {h_max:.1f} ft{indent}Name: {name_max}",
            xy=(0, 0),
            xycoords=ax.transAxes,
        )
        ax.figure.savefig(
            f"tmp/{year}.png", bbox_inches="tight", dpi=dpi, facecolor="w"
        )
        plt.close("all")
        pbar.update(1)

###############################################################################
# Repeat the last frame 100 times.

for i in range(1, 100):
    shutil.copy(f"tmp/{years[-1]}.png", f"tmp/{years[-1] + i}.png")

###############################################################################
# Convert the frames to a video file.

# !ffmpeg -hide_banner -loglevel panic -start_number 1641 -i tmp/%04d.png -pix_fmt yuv420p -vf scale=1920:-2 -y input_data/NID_2019.mp4
