import datetime
import os
import urllib.request
import json
import tomllib as tomli
from pathlib import Path
from textwrap import dedent, indent

import yaml
from PIL import Image
from sphinx.application import Sphinx
from sphinx.util import logging


LOGGER = logging.getLogger("conf")

# -- Project information -----------------------------------------------------
project = "HyRiver"
author = "Taher Chegini"
copyright = f"2019-{datetime.datetime.now().year}, {author}"

with urllib.request.urlopen('https://pypi.python.org/pypi/pygeohydro/json') as r:
    version = json.loads(r.read().decode('utf-8'))["info"]["version"]
    version = f"v{'.'.join(version.split('.')[:2])}"

packages = {
    "async-retriever": "AsyncRetriever",
    "pygeoogc": "PyGeoOGC",
    "pygeoutils": "PyGeoUtils",
    "pynhd": "PyNHD",
    "py3dep": "Py3DEP",
    "pygeohydro": "PyGeoHydro",
    "pydaymet": "PyDaymet",
    "pygridmet": "PyGridMET",
    "pynldas2": "PyNLDAS2",
    "hydrosignatures": "HydroSignatures",
}
# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
# -- General configuration ---------------------------------------------------

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_favicon",
]

bibtex_bibfiles = ['refs.bib']

# intersphinx configurations
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
    "geopandas": ("https://geopandas.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "rasterio": ("https://rasterio.readthedocs.io/en/latest", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "folium": ("https://python-visualization.github.io/folium/latest", None),
}

# autoapi configurations
autoapi_dirs = [
    "../../pynhd",
    "../../pygeohydro",
    "../../py3dep",
    "../../pydaymet",
    "../../pygridmet",
    "../../pynldas2",
    "../../hydrosignatures",
    "../../async-retriever",
    "../../pygeoogc",
    "../../pygeoutils",
]
autoapi_ignore = [
    "**ipynb_checkpoints**",
    "**tests**",
    "**setup.py",
    "**conf.py",
    "**conftest.py",
    "**noxfile.py",
    "**exceptions.py",
    "**print_versions.py",
    "**cli.py",
]
autoapi_options = ["members"]
autoapi_member_order = "groupwise"
autoapi_keep_files = False
autoapi_add_toctree_entry = False
modindex_common_prefix = [
    "pynhd.",
    "pygeohydro.",
    "py3dep.",
    "pydaymet.",
    "pygridmet.",
    "pynldas2.",
    "hydrosignatures.",
    "async-retriever.",
    "pygeoogc.",
    "pygeoutils.",
]

# typehints configurations
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# nbsphinx configurations
nbsphinx_timeout = 600
nbsphinx_execute = "never"
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None).rsplit("/", 1)[-1] %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{ docname }}`__.
        Interactive online version:
        :raw-html:`<a href="https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/notebooks/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/hyriver/HyRiver-examples/tree/main/notebooks/{{ docname }}
"""

# sphinx-copybutton configurations
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Napoleon configurations
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    # general terms
    "sequence": ":term:`sequence`",
    "iterable": ":term:`iterable`",
    "callable": ":py:func:`callable`",
    "dict_like": ":term:`dict-like <mapping>`",
    "dict-like": ":term:`dict-like <mapping>`",
    "path-like": ":term:`path-like <path-like object>`",
    "mapping": ":term:`mapping`",
    "file-like": ":term:`file-like <file-like object>`",
    # stdlib type aliases
    "MutableMapping": "~collections.abc.MutableMapping",
    "sys.stdout": ":obj:`sys.stdout`",
    "timedelta": "~datetime.timedelta",
    "string": ":class:`string <str>`",
    # numpy terms
    "array_like": ":term:`array_like`",
    "array-like": ":term:`array-like <array_like>`",
    "scalar": ":term:`scalar`",
    # objects without namespace
    "DataArray": "~xarray.DataArray",
    "Dataset": "~xarray.Dataset",
    "Variable": "~xarray.Variable",
    "ndarray": "~numpy.ndarray",
}

extlinks = {
    "issue": ("https://github.com/hyriver/hyriver.github.io/issues/%s", "GH %s"),
    "issue_async": ("https://github.com/hyriver/async-retriever/issues/%s", "GH %s"),
    "issue_ogc": ("https://github.com/hyriver/pygeoogc/issues/%s", "GH %s"),
    "issue_utils": ("https://github.com/hyriver/pygeoutils/issues/%s", "GH %s"),
    "issue_hydro": ("https://github.com/hyriver/pygeohydro/issues/%s", "GH %s"),
    "issue_nhd": ("https://github.com/hyriver/pynhd/issues/%s", "GH %s"),
    "issue_3dep": ("https://github.com/hyriver/py3dep/issues/%s", "GH %s"),
    "issue_day": ("https://github.com/hyriver/pydaymet/issues/%s", "GH %s"),
    "issue_grid": ("https://github.com/hyriver/pygridmet/issues/%s", "GH %s"),
    "issue_nldas": ("https://github.com/hyriver/pynldas2/issues/%s", "GH %s"),
    "issue_sig": ("https://github.com/hyriver/hydrosinatures/issues/%s", "GH %s"),
    "pull": ("https://github.com/hyriver/hyriver.github.io/pull/%s", "PR %s"),
    "pull_async": ("https://github.com/hyriver/async-retriever/pull/%s", "PR %s"),
    "pull_ogc": ("https://github.com/hyriver/pygeoogc/pull/%s", "PR %s"),
    "pull_utils": ("https://github.com/hyriver/pygeoutils/pull/%s", "PR %s"),
    "pull_hydro": ("https://github.com/hyriver/pygeohydro/pull/%s", "PR %s"),
    "pull_nhd": ("https://github.com/hyriver/pynhd/pull/%s", "PR %s"),
    "pull_3dep": ("https://github.com/hyriver/py3dep/pull/%s", "PR %s"),
    "pull_day": ("https://github.com/hyriver/pydaymet/pull/%s", "PR %s"),
    "pull_grid": ("https://github.com/hyriver/pygridmet/pull/%s", "PR %s"),
    "pull_ndlas": ("https://github.com/hyriver/pynldas2/pull/%s", "PR %s"),
    "pull_sig": ("https://github.com/hyriver/hydrosinatures/pull/%s", "PR %s"),
}

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
today_fmt = "%Y-%m-%d"
pygments_style = "sphinx"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "tests", ".ipynb_checkpoints", "**.github", "**examples/README.md"]

# sphinx_book_theme configurations
html_theme = "pydata_sphinx_theme"
html_title = ""

# logo
html_last_updated_fmt = today_fmt
html_logo = "_static/hyriver_logo_text.svg"
html_favicon = "_static/favicon.ico"

html_context = {
    "github_user": "cheginit",
    "github_repo": "hyriver.github.io",
    "github_version": "main",
    "doc_path": "docs",
}
html_baseurl = "https://docs.hyriver.io"

html_theme_options = {
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/ContactHyRiver",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/hyriver/hyriver.github.io",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "text": "",
        "image_dark": "_static/hyriver_logo_text.svg",
    },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",
    "navbar_center": ["version-switcher", "navbar-nav"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        "examples/no-sidebar": [],
    },
    "switcher": {
        "json_url": "https://docs.hyriver.io/_static/switcher.json",
        "version_match": version,
    },
    "navigation_with_keys": False,
}

html_sidebars = {
    "contributing": [],
    "authors": [],
    "license": [],
    "readme/*": [],
}

htmlhelp_basename = "HyRiverdoc"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta

# -- favicon options ---------------------------------------------------------

# see https://sphinx-favicon.readthedocs.io for more information about the
# sphinx-favicon extension
favicons = [
    # generic icons compatible with most browsers
    # "favicon-32x32.png",
    # "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # # chrome specific
    # "android-chrome-192x192.png",
    # # apple icons
    # {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    # {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    # # msapplications
    # {"name": "msapplication-TileColor", "content": "#459db9"},
    # {"name": "theme-color", "content": "#ffffff"},
    # {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]

# configuration for opengraph
description = " ".join(
    [
        "HyRiver is a suite of Python packages that provides a",
        "unified API for retrieving geospatial/temporal data from various web services."
    ]
)
ogp_site_url = "https://docs.hyriver.io"
ogp_image = "https://raw.githubusercontent.com/hyriver/hyriver.github.io/main/docs/source/_static/hydriver_logo.png"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary" />',
    '<meta name="twitter:site" content="@_taher_" />',
    '<meta name="twitter:creator" content="@_taher_" />',
    f'<meta name="twitter:description" content="{description}" />',
    f'<meta name="twitter:image" content="{ogp_image}" />',
    f'<meta name="twitter:image:alt" content="{description}" />',
]


# add visitor tracking
html_js_files = [
    ('https://app.rybbit.io/api/script.js', {
        'data-site-id': '303',
        'defer': None
    })
]

# -- Generating Gallery -------------------------------------------------------
def update_gallery(app: Sphinx)-> None:
    """Update the gallery page.

    Taken from https://github.com/pydata/xarray/blob/main/doc/conf.py
    """

    LOGGER.info("Updating gallery page ...")

    gallery = yaml.safe_load(Path(app.srcdir, "gallery.yml").read_bytes())
    for item in gallery:
        thumb = Path(item['thumbnail'])
        thumb.parent.mkdir(parents=True, exist_ok=True)
        thumb.write_bytes(Path(app.srcdir, "examples", "notebooks", "_static", thumb.name).read_bytes())

    items = [
        f"""
         .. grid-item-card::
            :text-align: center
            :link: {item['path']}

            .. image:: {item['thumbnail']}
                :alt: {item['title']}
            +++
            {item['title']}
        """
        for item in gallery
    ]

    items_md = indent(dedent("\n".join(items)), prefix="    ")
    markdown = f"""
.. grid:: 1 2 2 2
    :gutter: 2

    {items_md}
"""
    Path(app.srcdir, "examples-gallery.txt").write_text(markdown)
    LOGGER.info("Gallery page updated.")


def update_videos(app: Sphinx)-> None:
    """Update the videos page.

    Taken from https://github.com/pydata/xarray/blob/main/doc/conf.py
    """

    LOGGER.info("Updating videos page ...")

    videos = yaml.safe_load(Path(app.srcdir, "videos.yml").read_bytes())

    items = []
    for video in videos:

        authors = " | ".join(video["authors"])
        item = f"""
.. grid-item-card:: {" ".join(video["title"].split())}
    :text-align: center

    .. raw:: html

        {video['src']}
    +++
    {authors}
        """
        items.append(item)

    items_md = indent(dedent("\n".join(items)), prefix="    ")
    markdown = f"""
.. grid:: 1 2 2 2
    :gutter: 2

    {items_md}
    """
    Path(app.srcdir, "videos-gallery.txt").write_text(markdown)
    LOGGER.info("Videos page updated.")


def update_versions(app: Sphinx)-> None:
    """Update the versions page."""

    LOGGER.info("Updating versions page ...")
    LOGGER.info(f"Version match: {version}")

    versions = []
    for p, n in packages.items():
        with urllib.request.urlopen(f'https://pypi.python.org/pypi/{p}/json') as r:
            versions.append(
                {
                    "package": n,
                    "path": f"autoapi/{p.replace('-', '_')}/index.html",
                    "version": json.loads(r.read().decode('utf-8'))["info"]["version"],
                }
            )

    items = [
        f"""
         .. grid-item-card:: {item['package']}
            :text-align: center

            .. button-link:: {item['path']}
                :click-parent:
                :ref-type: ref
                :align: center

                v{item['version']}
        """
        for item in versions
    ]

    items_md = indent(dedent("\n".join(items)), prefix="    ")
    markdown = f"""
.. grid::
    :gutter: 3

    {items_md}
"""
    Path(app.srcdir, "versions.txt").write_text(markdown)
    LOGGER.info("Package versions page updated.")


def update_deps(app: Sphinx) -> None:
    """Get the dependencies of the package."""

    LOGGER.info("Updating dependencies page ...")

    deps = {}
    for p, n in packages.items():
        with Path(app.srcdir, "..", "..", p, "pyproject.toml").open("rb") as f:
            deps[n] = "\n".join(f"        - ``{d}``" for d in tomli.load(f)["project"]["dependencies"])

    items = [
        f"""
   .. tab-item:: {name}

{dep_list}
        """
        for name, dep_list in deps.items()
    ]

    items_md = indent(dedent("\n".join(items)), prefix="    ")
    markdown = f"""
.. tab-set::

   {items_md}
"""
    Path(app.srcdir, "dependencies.txt").write_text(markdown)
    LOGGER.info("Package dependencies updated.")


def resize_thumbnails(app: Sphinx)-> None:
    """Resize thumbnails to the same width and height as the second item's thumbnail."""
    LOGGER.info("Resizing gallery thumbnails ...")
    thumb_dir = Path("source/_static/thumbnails")
    src = Path("source/examples/notebooks/_static")
    thumb_dir.mkdir(exist_ok=True, parents=True)
    try:
        with Path('source/gallery.yml').open() as file:
            docs = yaml.safe_load(file)


        second_thumbnail_path = Path(docs[1]['thumbnail'])
        with Image.open(Path(src, second_thumbnail_path.name)) as img:
            target_size = img.size

        for doc in docs:
            thumbnail_path = Path(doc['thumbnail'])
            with Image.open(Path(src, thumbnail_path.name)) as img:
                # Calculate the new size, maintaining aspect ratio
                ratio = min(target_size[0] / img.width, target_size[1] / img.height)
                new_size = (int(img.width * ratio), int(img.height * ratio))

                # Resize the image with the new size
                img = img.resize(new_size, Image.Resampling.LANCZOS)

                # Create a new image with a white background
                new_img = Image.new('RGB', target_size, (255, 255, 255))
                # Calculate the position to paste the resized image on the canvas
                position = ((target_size[0] - new_size[0]) // 2, (target_size[1] - new_size[1]) // 2)
                # Paste the resized image onto the canvas
                new_img.paste(img, position)
                # Save the final thumbnail
                new_img.save(Path(thumb_dir,  thumbnail_path.name))
    except Exception as e:
        LOGGER.exception(f"An error occurred: {e}")
    LOGGER.info("Gallery thumbnails resized.")


def html_page_context(app, pagename, templatename, context, doctree):
    # Disable edit button for docstring generated pages
    if "generated" in pagename:
        context["theme_use_edit_page_button"] = False


def setup(app: Sphinx):
    app.connect("html-page-context", html_page_context)
    app.connect("builder-inited", update_gallery)
    app.connect("builder-inited", resize_thumbnails)
    app.connect("builder-inited", update_videos)
    app.connect("builder-inited", update_versions)
    app.connect("builder-inited", update_deps)
