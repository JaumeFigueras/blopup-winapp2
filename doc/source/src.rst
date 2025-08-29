Source Files
============

.. contents::
   :local:
   :depth: 1

All the code is under the ``src`` folder. It contains the main window, the QT resources file (for the
graphical user interface and the internationalization (i18n) configuration files

main.py
-------

This is the main file to run the application. The application is designed with modules, not to run like a
regular script. To run it type:

    .. code-block:: bash

      python3 -m src.main

resources.qrc
-------------

The resources definition file is the configuration file for the different images, icons and other display
elements required to run the main application. The resources have to be compiled with the PyQt5 resource
compiler. To run it type:

    .. code-block:: bash

      pyrcc5 src/resources.qrc -o src/resources.py

This will generate the ``resources.py`` file that is the necessary file for python to load the resources in
the main application

i18n - blopup.pro
-----------------

The transaltion project file ``blopup.pro`` is the file that contains the locations of the translation strings,
the python files that contain literal strings to translate and the graphical user interface files with literal
strings to translate.

The translations are done with the `QTLinguist <https://doc.qt.io/archives/qt-5.15/qtlinguist-index.html>`_
application. Be careful because the project still uses Qt5, not Qt6.

The normal workflow to translate qith **QTLinguist** is:

    1. Create the code and the ``.ui`` user interface files

    2. Add them to the ``blopup.pro`` file

    3. Generate or update the translation strings for the desired locales (that are defined in the ``blopup.pro`` file

    .. code-block:: bash

      pylupdate5 -noobsolete src/blopup.pro

    4. Use **QTLinguist** to edit and generate the strings

All the ``.ts`` and ``.qm`` files are stored in the ``i18n`` folder

Data Model
----------

The data model folder ``data_model`` is where all the classes that model the **OpenMRS** elements and types are
modelled. Although not necessary, the SQLAlchemy ORM is used to be prepared to store locally any possible replicas
of the data stored in the Open MRS servers.

The objects currently modelled are:

.. toctree::
   :maxdepth: 2

   src/data_model

JSON Decoders
-------------

To decode the **OpenMRS** REST API calls, that are serialized with JSON, it is possible to have receive some
``null`` or ``None`` values, that can break the specific decoder for each API call. This module provides a
JSON decoder that skip null objects (not null values). To use it as this example:

    .. code-block:: python

      json.loads(json_str, cls=NoNoneInList, object_hook=Patient.object_hook_search_custom)

.. toctree::
   :maxdepth: 2

   src/json_encoders

User Interface
--------------

.. todo::

   Descripció

.. toctree::
   :maxdepth: 2

   src/ui

OpenMRS Remote API
------------------

.. todo::

   Descripció

.. toctree::
   :maxdepth: 2

   src/remote_api


