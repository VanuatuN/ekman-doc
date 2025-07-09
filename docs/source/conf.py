project = 'Ekman Cluster Documentation'

#release = '1.0'

copyright = u'2025, Alexander Gavrikov, Natalia Tilinina'
author = u'Alexander Gavrikov, Natalia Tilinina'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


extensions = []

templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'    
html_theme = 'sphinx_rtd_theme'    #'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'collapse_navigation': False,
  'navigation_depth': 4,
  'titles_only': False,
}

html_static_path = ['_static']

exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

exclude_patterns = []


html_context = {
    "display_github": True,
    "github_user": "VanuatuN",
    "github_repo": "ekman-doc",
    "github_version": "main",
}

html_logo = '_static/institute_logo.png'
html_favicon = '_static/favicon_ekman.ico'


# html_theme_options = {
#     'logo': 'lab_logo.jpg',
#     'description': 'Ekman Cluster: Specs & Usage',
#     'github_user': 'VanuatuN',
#     'github_repo': 'ekman-doc',
#     'fixed_sidebar': True,
#     'sidebar_includehidden': True,
#     'extra_nav_links': {
#         'Institute of Oceanology RAS': 'https://ocean.ru',
#         'Sea-Air Interaction and Climate Laboratory': 'https://sail.ocean.ru',
#     },
# }