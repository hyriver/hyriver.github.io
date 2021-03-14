# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "HyRiver"
author = "Taher Chegini"
copyright = f"2019-{datetime.datetime.now().year}, {author}"

# The full version, including alpha/beta/rc tags
from github import Github

g = Github()
repo = g.get_repo("cheginit/pygeohydro")
tags = repo.get_tags()
version = f"{'.'.join(tags[0].name[1:].split('.')[:2])}.x"
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",
    "sphinx_gallery.load_style",
    "sphinx.ext.mathjax",
    "recommonmark",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
    "geopandas": ("https://geopandas.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "folium": ("https://python-visualization.github.io/folium/", None),
}

autoapi_dirs = [
    "../../pygeoogc",
    "../../pygeoutils",
    "../../pynhd",
    "../../pygeohydro",
    "../../py3dep",
    "../../pydaymet",
]
autoapi_ignore = ["**ipynb_checkpoints**", "**tests**", "**setup**", "**generate_pip**", "**conf**"]
autoapi_options = [
    "members",
    "inherited-members",
    "undoc-members",
    # 'private-members',
    "show-inheritance",
    # 'show-module-summary',
    # 'special-members',
    # 'imported-members',
]
autodoc_typehints = "description"
modindex_common_prefix = [
    "pygeoogc.",
    "pygeoutils.",
    "pynhd.",
    "pygeohydro.",
    "py3dep.",
    "pydaymet.",
]

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
        :raw-html:`<a href="https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?filepath=notebooks/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/cheginit/HyRiver-examples/tree/main/notebooks/{{ docname }}
"""

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
today_fmt = "%Y-%m-%d"
pygments_style = "sphinx"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "tests", ".ipynb_checkpoints"]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'pydata_sphinx_theme'
import sphinx_material

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {"logo_only": True}
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": project,
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://hyriver.readthedocs.io/",
    # Set the color and the accent color
    "color_primary": "indigo",
    "color_accent": "deep-purple",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/cheginit/HyRiver",
    "repo_name": project,
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 3,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": False,
    "html_minify": True,
    "css_minify": True,
}

html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_title = "HyRiver"
html_last_updated_fmt = today_fmt
html_logo = "_static/hyriver_logo.svg"
html_favicon = "_static/favicon.ico"
htmlhelp_basename = "HyRiverdoc"

ipython_savefig_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_build", "html", "_static"
)
if not os.path.exists(ipython_savefig_dir):
    os.makedirs(ipython_savefig_dir)

import recommonmark
from recommonmark.transform import AutoStructify

github_doc_root = "https://github.com/rtfd/recommonmark/tree/master/doc/"


def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {
            "url_resolver": lambda url: github_doc_root + url,
            "auto_toc_tree_section": "Contents",
        },
        True,
    )
    app.add_transform(AutoStructify)
