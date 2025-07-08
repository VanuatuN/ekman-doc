# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Guide to Ekman'
copyright = '2025, Natalia Tilinina and Alexander Gavrikov'
author = 'Natalia Tilinina and Alexander Gavrikov'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'

html_theme = "furo"
html_static_path = ['_static']

html_logo = "_static/lab_logo.jpg"  # логотип в шапке
html_favicon = "_static/logotip_03-2.png"  # можно заменить

html_theme_options = {
    "light_logo": "lab_logo.jpg",
    "dark_logo": "lab_logo.jpg",
    "sidebar_hide_name": False,
}


