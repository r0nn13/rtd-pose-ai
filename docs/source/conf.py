# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PoseAI'
copyright = '2022, PoseAI'
author = 'PoseAI developers'

release = '1.0'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PoseAI'
copyright = '2022, PoseAI'
author = 'PoseAI developers'

release = '1.0'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme_options = {
    'base_url': 'http://bashtage.github.io/sphinx-material/',
    'repo_url': 'https://github.com/bashtage/sphinx-material/',
    'repo_name': 'Material for Sphinx',
    'google_analytics_account': 'UA-XXXXX',
    'html_minify': True,
    'css_minify': True,
    'nav_title': 'Material Sphinx Demo',
    'logo_icon': '&#xe869',
    'globaltoc_depth': 2
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
# -- Options for EPUB output
epub_show_urls = 'footnote'
