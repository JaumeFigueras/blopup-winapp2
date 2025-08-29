.. BLOPUP-WinApp documentation master file, created by
   sphinx-quickstart on Fri Aug 29 22:24:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

BLOPUP-WinApp documentation
===========================

.. todo::

   Millorar descripció

This repository contains all the code and manuals for the **BLOPUP** Project windows application.

The project is organized as follows:

    1. The ``doc`` folder is the root directory for all the documentation system build with
       `Sphinx <https://www.sphinx-doc.org/>`_.

    2. The ``src`` folder is the sources root.

    3. The ``test`` folder is the unit testing and ui testing sources folder.

    4. There is also the ``LICENSE``. ``README`` files and the ``requirements.txt`` file to create the python
       virtual enviroment that is explained in the :doc:`setup/python_virtual_environment` Setup doc.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   setup
   src
   test
