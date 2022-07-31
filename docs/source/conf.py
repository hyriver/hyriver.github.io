import datetime
from pathlib import Path
from textwrap import dedent, indent

import yaml
from sphinx.application import Sphinx
from sphinx.util import logging
from github import Github


LOGGER = logging.getLogger("conf")

# -- Project information -----------------------------------------------------
project = "HyRiver"
author = "Taher Chegini"
copyright = f"2019-{datetime.datetime.now().year}, {author}"

repo = Github().get_repo("hyriver/pygeohydro")
tags = repo.get_tags()
version = f"{'.'.join(tags[0].name[1:].split('.')[:2])}.x"
release = version

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
    "recommonmark",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
    "sphinx_design",
]

bibtex_bibfiles = ['refs.bib']

# intersphinx configurations
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
    "dask": ("https://docs.dask.org/en/latest/", None),
    "geopandas": ("https://geopandas.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "rasterio": ("https://rasterio.readthedocs.io/en/latest", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "folium": ("https://python-visualization.github.io/folium/", None),
}

# autoapi configurations
autoapi_dirs = [
    "../../pynhd",
    "../../pygeohydro",
    "../../py3dep",
    "../../pydaymet",
    "../../async_retriever",
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
autoapi_keep_files = True
autoapi_add_toctree_entry = False
modindex_common_prefix = [
    "pynhd.",
    "pygeohydro.",
    "py3dep.",
    "pydaymet.",
    "async_retriever.",
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
{% set docname = env.doc2path(env.docname, base=None).replace("nblink","ipynb") %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{ docname }}`__.
        Interactive online version:
        :raw-html:`<a href="https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/hyriver/HyRiver-examples/tree/main/{{ docname }}
"""

# sphinx-copybutton configurations
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

autodoc_typehints = "none"

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
    "array": ":term:`array`",
    "hashable": ":term:`hashable <name>`",
    # matplotlib terms
    "color-like": ":py:func:`color-like <matplotlib.colors.is_color_like>`",
    "matplotlib colormap name": ":doc:matplotlib colormap name <Colormap reference>",
    "matplotlib axes object": ":py:class:`matplotlib axes object <matplotlib.axes.Axes>`",
    "colormap": ":py:class:`colormap <matplotlib.colors.Colormap>`",
    # objects without namespace
    "DataArray": "~xarray.DataArray",
    "Dataset": "~xarray.Dataset",
    "Variable": "~xarray.Variable",
    "ndarray": "~numpy.ndarray",
    "MaskedArray": "~numpy.ma.MaskedArray",
    "dtype": "~numpy.dtype",
    "ComplexWarning": "~numpy.ComplexWarning",
    "Index": "~pandas.Index",
    "MultiIndex": "~pandas.MultiIndex",
    "CategoricalIndex": "~pandas.CategoricalIndex",
    "TimedeltaIndex": "~pandas.TimedeltaIndex",
    "DatetimeIndex": "~pandas.DatetimeIndex",
    "Series": "~pandas.Series",
    "DataFrame": "~pandas.DataFrame",
    "Categorical": "~pandas.Categorical",
    "Path": "~~Path",
    # objects with abbreviated namespace (from pandas)
    "pd.Index": "~pandas.Index",
    "pd.NaT": "~pandas.NaT",
}

extlinks = {
    "issue": ("https://github.com/hyriver/hyriver.github.io/issues/%s", "GH"),
    "issue_async": ("https://github.com/hyriver/async_retriever/issues/%s", "GH"),
    "issue_ogc": ("https://github.com/hyriver/pygeoogc/issues/%s", "GH"),
    "issue_utils": ("https://github.com/hyriver/pygeoutils/issues/%s", "GH"),
    "issue_hydro": ("https://github.com/hyriver/pygeohydro/issues/%s", "GH"),
    "issue_nhd": ("https://github.com/hyriver/pynhd/issues/%s", "GH"),
    "issue_3dep": ("https://github.com/hyriver/py3dep/issues/%s", "GH"),
    "issue_day": ("https://github.com/hyriver/pydaymet/issues/%s", "GH"),
    "pull": ("https://github.com/hyriver/hyriver.github.io/pull/%s", "PR"),
    "pull_async": ("https://github.com/hyriver/async_retriever/pull/%s", "PR"),
    "pull_ogc": ("https://github.com/hyriver/pygeoogc/pull/%s", "PR"),
    "pull_utils": ("https://github.com/hyriver/pygeoutils/pull/%s", "PR"),
    "pull_hydro": ("https://github.com/hyriver/pygeohydro/pull/%s", "PR"),
    "pull_nhd": ("https://github.com/hyriver/pynhd/pull/%s", "PR"),
    "pull_3dep": ("https://github.com/hyriver/py3dep/pull/%s", "PR"),
    "pull_day": ("https://github.com/hyriver/pydaymet/pull/%s", "PR"),
}

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
html_css_files = ["style.css"]
today_fmt = "%Y-%m-%d"
pygments_style = "sphinx"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "tests", ".ipynb_checkpoints", "**.github", "**examples/README.md"]

# sphinx_book_theme configurations
html_theme = "sphinx_book_theme"
html_title = ""

html_context = {
    "github_user": "cheginit",
    "github_repo": "hyriver.github.io",
    "github_version": "main",
    "doc_path": "docs",
}
html_baseurl = "https://docs.hyriver.io"
html_theme_options = {
    "repository_url": "https://github.com/hyriver/hyriver.github.io",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org/v2/gh/hyriver/HyRiver-examples/main?urlpath=lab/tree/notebooks",
        "notebook_interface": "jupyterlab",
    },
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_download_button": False,
    "use_issues_button": True,
    "home_page_in_toc": True,
    "extra_navbar": "",
    "navbar_footer_text": "",
}

# logo
html_last_updated_fmt = today_fmt
html_logo = "_static/hyriver_logo_text.svg"
html_favicon = "_static/favicon.ico"
htmlhelp_basename = "HyRiverdoc"

# configuration for opengraph
description = " ".join(
    [
        "HyRiver is a suite of Python packages that provides a",
        "unified API for retrieving geospatial/temporal data from various web services."
    ]
)
ogp_site_url = "https://hyriver.readthedocs.io/en/latest"
ogp_image = "https://raw.githubusercontent.com/hyriver/hyriver.github.io/main/docs/source/_static/hydriver_logo.png"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary" />',
    '<meta name="twitter:site" content="@_taher_" />',
    '<meta name="twitter:creator" content="@_taher_" />',
    f'<meta name="twitter:description" content="{description}" />',
    f'<meta name="twitter:image" content="{ogp_image}" />',
    f'<meta name="twitter:image:alt" content="{description}" />',
]

# -- Generating Gallery -------------------------------------------------------
def update_gallery(app: Sphinx):
    """Update the gallery page.

    Taken from https://github.com/pydata/xarray/blob/main/doc/conf.py
    """

    LOGGER.info("Updating gallery page...")

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
    Path(app.srcdir, "example-gallery.txt").write_text(markdown)
    LOGGER.info("Gallery page updated.")


def update_videos(app: Sphinx):
    """Update the videos page."""

    LOGGER.info("Updating videos page...")

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


def html_page_context(app, pagename, templatename, context, doctree):
    # Disable edit button for docstring generated pages
    if "generated" in pagename:
        context["theme_use_edit_page_button"] = False


def setup(app: Sphinx):
    app.connect("html-page-context", html_page_context)
    app.connect("builder-inited", update_gallery)
    app.connect("builder-inited", update_videos)