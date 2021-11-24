import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------
project = "HyRiver"
author = "Taher Chegini"
copyright = f"2019-{datetime.datetime.now().year}, {author}"

from github import Github

repo = Github().get_repo("cheginit/pygeohydro")
tags = repo.get_tags()
version = f"{'.'.join(tags[0].name[1:].split('.')[:2])}.x"
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.linkcode",
    "sphinx.ext.mathjax",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "nbsphinx",
    "nbsphinx_link",
    "sphinx_gallery.load_style",
    "recommonmark",
    "sphinx_panels",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.bibtex",
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
        :raw-html:`<a href="https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/cheginit/HyRiver-examples/tree/main/{{ docname }}
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
    "Path": "~~pathlib.Path",
    # objects with abbreviated namespace (from pandas)
    "pd.Index": "~pandas.Index",
    "pd.NaT": "~pandas.NaT",
}


extlinks = {
    "issue": ("https://github.com/cheginit/HyRiver/issues/%s", "GH"),
    "issue_async": ("https://github.com/cheginit/async_retriever/issues/%s", "GH"),
    "issue_ogc": ("https://github.com/cheginit/pygeoogc/issues/%s", "GH"),
    "issue_utils": ("https://github.com/cheginit/pygeoutils/issues/%s", "GH"),
    "issue_hydro": ("https://github.com/cheginit/pygeohydro/issues/%s", "GH"),
    "issue_nhd": ("https://github.com/cheginit/pynhd/issues/%s", "GH"),
    "issue_3dep": ("https://github.com/cheginit/py3dep/issues/%s", "GH"),
    "issue_day": ("https://github.com/cheginit/pydaymet/issues/%s", "GH"),
    "pull": ("https://github.com/cheginit/HyRiver/pull/%s", "PR"),
    "pull_async": ("https://github.com/cheginit/async_retriever/pull/%s", "PR"),
    "pull_ogc": ("https://github.com/cheginit/pygeoogc/pull/%s", "PR"),
    "pull_utils": ("https://github.com/cheginit/pygeoutils/pull/%s", "PR"),
    "pull_hydro": ("https://github.com/cheginit/pygeohydro/pull/%s", "PR"),
    "pull_nhd": ("https://github.com/cheginit/pynhd/pull/%s", "PR"),
    "pull_3dep": ("https://github.com/cheginit/py3dep/pull/%s", "PR"),
    "pull_day": ("https://github.com/cheginit/pydaymet/pull/%s", "PR"),
}

# -- Options for HTML output -------------------------------------------------

templates_path = ["_templates"]
html_css_files = ["style.css"]
today_fmt = "%Y-%m-%d"
pygments_style = "sphinx"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "tests", ".ipynb_checkpoints"]

# sphinx_book_theme configurations
html_theme = "sphinx_book_theme"
html_title = ""

html_context = {
    "github_user": "cheginit",
    "github_repo": "HyRiver",
    "github_version": "main",
    "doc_path": "docs",
}

html_theme_options = {
    "repository_url": "https://github.com/cheginit/HyRiver",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org/v2/gh/cheginit/HyRiver-examples/main?urlpath=lab/tree/notebooks",
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

html_static_path = ["_static"]

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
ogp_image = "https://raw.githubusercontent.com/cheginit/HyRiver/main/docs/source/_static/hydriver_logo.png"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary" />',
    '<meta name="twitter:site" content="@_taher_" />',
    '<meta name="twitter:creator" content="@_taher_" />',
    f'<meta name="twitter:description" content="{description}" />',
    f'<meta name="twitter:image" content="{ogp_image}" />',
    f'<meta name="twitter:image:alt" content="{description}" />',
]

# fix an issue with ipython where it doesn't create the missing dirs
ipython_savefig_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_build", "html", "_static"
)
if not os.path.exists(ipython_savefig_dir):
    os.makedirs(ipython_savefig_dir)

# -- markdown configurations -------------------------------------------------
import inspect
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

# -- link to source ----------------------------------------------------------

# based on numpy doc/source/conf.py
def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != "py":
        return None

    p_name = info["module"].split(".")[0]
    p_obj = sys.modules.get(p_name)

    modname = info["module"]
    fullname = info["fullname"]

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split("."):
        try:
            obj = getattr(obj, part)
        except AttributeError:
            return None

    try:
        fn = inspect.getsourcefile(inspect.unwrap(obj))
    except TypeError:
        fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except OSError:
        lineno = None

    if lineno:
        linespec = f"#L{lineno}-L{lineno + len(source) - 1}"
    else:
        linespec = ""

    fn = os.path.relpath(fn, start=os.path.dirname(p_obj.__file__))

    if "+" in p_obj.__version__:
        return f"https://github.com/cheginit/{p_name}/blob/main/{p_name}/{fn}{linespec}"
    else:
        return (
            f"https://github.com/cheginit/{p_name}/blob/"
            f"v{p_obj.__version__}/{p_name}/{fn}{linespec}"
        )

def html_page_context(app, pagename, templatename, context, doctree):
    # Disable edit button for docstring generated pages
    if "generated" in pagename:
        context["theme_use_edit_page_button"] = False


def setup(app):
    app.connect("html-page-context", html_page_context)