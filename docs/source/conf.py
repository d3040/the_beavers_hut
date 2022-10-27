# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "The Beaver's Hut"
copyright = '2022, Daniel Clavijo'
author = 'Daniel Clavijo'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates/']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = 'd3040'
html_theme_options = {
    'use_download_button': False,
    'use_fullscreen_button': False,
    'repository_url': 'https://github.com/d3040/the_beavers_hut',
    'use_repository_button': True,
    'show_navbar_depth': 2,
    'announcement': ""
}
