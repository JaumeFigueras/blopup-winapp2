Setup
=====

.. contents::
   :local:
   :depth: 1

Overview
--------

The **BLOPUP** project integrates several tools and components that must be configured before use.
This setup guide provides an overview of each requirement and links to detailed instructions.

Requirements
------------

1. **Python Virtual Environment**
   BLOPUP runs on a dedicated Python virtual environment that is required to ensure
   that all librearies are isolated and do not cause conflicts with other existing
   software. This virtual environment is needed to both users and developers.
   See :doc:`setup/python_virtual_environment` for setup steps.

2. **Sphinx Documentation System**
   `Sphinx <https://www.sphinx-doc.org/en/master/>`_ is required to build the project
   documentation. If you develop on this project the Sphinx environment is needed.
   See :doc:`setup/sphinx_documentation` for setup steps.

3. **Deploying Sphinx Documentation to GitHub**
   Enables automated generation and publishing of the documentation to GitHub Pages.
   This should have been set up on `BLOPUP/winapp2 <https://github.com/BLOPUP-UPC/blopup-winapp2>`_
   github repo, but still documented just in case.
   See :doc:`setup/deploy_sphinx_to_github` for setup steps.

Setup Pages
-----------

.. toctree::
   :maxdepth: 1

   setup/python_virtual_environment
   setup/sphinx_documentation
   setup/deploy_sphinx_to_github