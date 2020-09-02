import sphinx
import sphinx_tabs
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'EB FIRST'
copyright = '2020, EB FIRST Inc.'
author = 'Varun Mehrotra'
version = '2020'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_tabs.tabs',
    'sphinx.ext.imgmath',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.ghcontributors',
    'sphinxcontrib.remoteliteralinclude',
    'notfound.extension'
]

# TODO Directives omit a warning
todo_emit_warnings = False

# TODO Directives are not shown in output
todo_include_todos = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# Specify the master doc file, AKA our homepage
master_doc = "index"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
	'collapse_navigation': True,
	'sticky_navigation': False,
	'titles_only': True
}

user_options = [
        ('warning-is-error', True),
]


# -- Options for latex generation --------------------------------------------

latex_engine = 'xelatex'



latex_elements = {
    'fontpkg': r'''
	\setmainfont{DejaVu Serif}
	\setsansfont{DejaVu Sans}
	\setmonofont{DejaVu Sans Mono}''',
    'preamble': r'''
	\usepackage[titles]{tocloft}
	\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
	\setlength{\cftchapnumwidth}{0.75cm}
	\setlength{\cftsecindent}{\cftchapnumwidth}
	\setlength{\cftsecnumwidth}{1.25cm}
	''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}

suppress_warnings = ['epub.unknown_project_files']

sphinx_tabs_valid_builders = ['epub', 'linkcheck']
