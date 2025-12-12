# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Examples'
copyright = "2022-2025, The kALDo Developers"
author = 'Giuseppe Barbalinardo, Zekun Chen, Nicholas W. Lundgren, Dylan Folkner, Bohan Li, Davide Donadio'

version = ''
release = ''

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx_immaterial',
    'myst_parser',
    'nbsphinx',
    'sphinx.ext.mathjax',
]

autosummary_generate = True
autoclass_content = 'class'
autodoc_member_order = 'bysource'

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

# MyST parser configuration
myst_enable_extensions = [
    "html_image",
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

needs_sphinx = '8.0'
master_doc = 'index'
language = 'en'

exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store',
                    '**.ipynb_checkpoints']

pygments_style = 'default'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_immaterial'

html_title = 'Examples'

html_logo = 'docsource/_resources/logo.png'

html_theme_options = {
    "font": False,

    "analytics": {
        "provider": "google",
        "property": "G-HQHR3LWX3F"
    },

    'site_url': 'https://github.com/nanotheorygroup/kaldo-examples',

    "palette": {
        "scheme": "default",
        "primary": "red",
        "accent": "orange",
    },

    'repo_url': 'https://github.com/nanotheorygroup/kaldo-examples',
    'repo_name': 'kALDo Examples',

    'globaltoc_collapse': True,
    'globaltoc_maxdepth': 1,
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_static_path = ['_static']

html_js_files = [
    ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js', {'priority': 100}),
]

html_favicon = 'docsource/_resources/logo.ico'

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'kaldoexamplesdoc'

nbsphinx_execute = 'never'
nbsphinx_prompt_width = '0'

latex_engine = 'pdflatex'

default_role = 'math'
