# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join('..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join('..', 'test')))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BLOPUP-WinApp'
copyright = '2025, BLOPUP'
author = 'BLOPUP'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

highlight_language = 'default'    # or 'python', doesn't affect SQL blocks
pygments_style = 'sphinx'         # or another theme like 'monokai'
pygments_dark_style = "native"    # good for Furo's dark mode
autodoc_member_order = 'bysource' # Keep attrs and functions order when generating the docs

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

from sqlalchemy.ext.hybrid import hybrid_property
from sphinx.ext.autodoc import PropertyDocumenter


class HybridPropertyDocumenter(PropertyDocumenter):
    """
    Custom documenter to treat SQLAlchemy hybrid_property like a normal @property.
    """
    objtype = "hybrid_property"
    directivetype = "attribute"

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, hybrid_property)


def setup(app):
    # Register our custom documenter
    app.add_autodocumenter(HybridPropertyDocumenter)
