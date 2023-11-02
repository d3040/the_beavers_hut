# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "The Beaver's Hut"
copyright = '2023, Daniel Clavijo'
author = 'Daniel Clavijo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['sphinxcontrib.icon']
templates_path = ['_templates/']
exclude_patterns = ['book/*']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'press'
html_title = 'd3040'
html_favicon = '☕︎'

html_static_path = ['_static']
html_css_files = ['css/custom.css']
#html_js_files = ['js/custom.js']
#html_theme_options = {"external_links": [("Github", "https://github.com/d3040/the_beavers_hut"),("d3040", "https://d3040.com")]}

