#!python3

"""
Configuration for project documentation using Sphinx.
"""

# standard
import sys
from datetime import datetime
from os import environ, path

sys.path.insert(0, path.abspath(".."))  # move into project package

# Package
from profile_manager import __about__

# -- Project information -----------------------------------------------------
author = __about__.__author__
copyright = __about__.__copyright__
description = __about__.__summary__
project = __about__.__title__
version = release = __about__.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Sphinx included
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    # 3rd party
    "myst_parser",
    "sphinx_copybutton",
]


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
autosectionlabel_prefix_document = True
# The master toctree document.
master_doc = "index"


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "_build",
    ".venv",
    "Thumbs.db",
    ".DS_Store",
    "_output",
    "ext_libs",
    "tests",
    "demo",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# -- Theme

html_favicon = str(__about__.__icon_path__)
html_logo = str(__about__.__icon_path__)
# uncomment next line if you store some statics which are not directly linked into the markdown/RST files
# html_static_path = ["static/include_additional"]
html_theme = "furo"

# -- EXTENSIONS --------------------------------------------------------

# Sphinx API doc
autodoc_mock_imports = [
    "qgis.core",
    "qgis.gui",
    "qgis.PyQt",
    "qgis.PyQt.QtCore",
    "qgis.PyQt.QtGui",
    "qgis.PyQt.QtNetwork",
    "qgis.PyQt.QtWidgets",
    "qgis.utils",
]

# Configuration for intersphinx (refer to others docs).
intersphinx_mapping = {
    "PyQt5": ("https://www.riverbankcomputing.com/static/Docs/PyQt5", None),
    "python": ("https://docs.python.org/3/", None),
    "qgis": ("https://qgis.org/pyqgis/master/", None),
}

# MyST Parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]

myst_substitutions = {
    "author": author,
    "date_update": datetime.now().strftime("%d %B %Y"),
    "description": description,
    "qgis_version_max": __about__.__plugin_md__.get("general").get(
        "qgismaximumversion"
    ),
    "qgis_version_min": __about__.__plugin_md__.get("general").get(
        "qgisminimumversion"
    ),
    "repo_url": __about__.__uri__,
    "title": project,
    "version": version,
}

myst_url_schemes = ("http", "https", "mailto")


# -- API Doc --------------------------------------------------------
# run api doc
def run_apidoc(_):
    from sphinx.ext.apidoc import main

    cur_dir = path.normpath(path.dirname(__file__))
    output_path = path.join(cur_dir, "_apidoc")
    modules = path.normpath(path.join(cur_dir, "../profile_manager"))
    exclusions = ["../.venv", "../tests"]
    main(["-e", "-f", "-M", "-o", output_path, modules] + exclusions)


# launch setup
def setup(app):
    app.connect("builder-inited", run_apidoc)
