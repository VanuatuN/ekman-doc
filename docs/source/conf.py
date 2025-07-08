project = 'Ekman Cluster Documentation'
author = 'Natalia Tilinina and Alexander Gavrikov'
release = '1.0'

extensions = []

templates_path = ['_templates/sidebar']


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
}

html_static_path = ['_static']

exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

exclude_patterns = []


html_logo = '_static/lab_logo.jpg'

html_sidebars = {
    '**': [
        'sidebar/navigation.html',     # глобальное оглавление (как “Contents”)
        'relations.html',     # кнопки "next" и "previous"
        'searchbox.html',     # строка поиска
    ]
}

html_theme_options = {
    'logo': 'lab_logo.jpg',
    'description': 'Ekman Cluster: Specs & Usage',
    'github_user': 'VanuatuN',
    'github_repo': 'ekman-doc',
    'fixed_sidebar': True,
    'sidebar_includehidden': True,
    'extra_nav_links': {
        'Institute of Oceanology RAS': 'https://ocean.ru',
        'Sea-Air Interaction and Climate Laboratory': 'https://sail.ocean.ru',
    },
}