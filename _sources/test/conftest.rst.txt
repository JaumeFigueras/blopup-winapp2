conftest.py
===========

The ``conftest.py`` file is a special configuration file used by pytest.
It allows you to define shared fixtures, hooks, and plugins that are
automatically discovered and made available to all tests within the
directory tree.

In this project, ``conftest.py`` is located in the root ``test/`` folder
and configures the test environment as follows:

- Defines the root paths for the test folder and the main project folder.
- Declares a list of ``pytest_plugins`` that extend the available fixtures.
  These plugins are organized by domain (e.g. data model, UI, remote API),
  but many are currently commented out to keep the active test environment
  minimal.
- Provides access to commonly used fixtures (such as the UI application
  fixture defined in ``test/fixtures/ui/application.py``) without the need
  to import them explicitly in each test file.

Notes
-----
- Pytest will automatically load this file when running tests.
- Any fixtures or hooks defined here are globally available within the
  project’s tests.
- Commenting or uncommenting entries in ``pytest_plugins`` controls which
  fixture sets are active.

``conftest.py`` is therefore the central place to organize and activate
fixtures that should be shared across multiple test modules.
