Unit and UI Test Files
======================

This section introduces the basics of testing within the project and explains
how the test files are structured.

What is testing?
----------------
*Testing* is the process of verifying that an application behaves as expected.
It helps detect errors early, ensures code quality, and guarantees that future
changes do not break existing functionality. Tests can be manual (executed by a
person) or automated (executed by the computer with the help of a testing
framework such as ``pytest``).

Unit tests
----------
*Unit tests* validate the behavior of small, isolated units of code, such as
functions or individual classes. The goal is to confirm that each component
fulfills its responsibility correctly and consistently. Unit tests are usually
fast to execute and very useful for detecting regressions.

UI tests
--------
*UI tests* (User Interface tests) verify the behavior of the visible parts of
the application: windows, buttons, menus, and other interactive elements.
For Qt-based applications, this includes checking that widgets are displayed
correctly, respond to user actions, and reflect the application’s state
properly. These tests ensure that the end-user experience is preserved.

conftest.py
-----------

The ``conftest.py`` file is a special configuration file used by pytest to
provide shared fixtures and plugins across multiple test modules. It allows
the project to centralize setup, teardown, and reusable test resources without
explicit imports in every test file.

Fixtures
--------

*Fixtures* are functions that prepare and provide resources for tests, such as
isolated ``QSettings`` objects or running instances of the main application
window. They help keep tests concise, consistent, and independent, while
ensuring proper setup and cleanup of resources.

.. toctree::
   :maxdepth: 2

   test/conftest
   test/fixtures

Tests
-----

.. toctree::
   :maxdepth: 1

   test/main

