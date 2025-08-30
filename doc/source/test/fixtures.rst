Fixtures
========

Fixtures are a powerful feature of ``pytest`` that provide a way to set up and
tear down resources needed by tests. Instead of duplicating setup code in every
test, fixtures allow you to declare reusable components that can be shared
across multiple test functions or modules.

In practice, a fixture is simply a Python function decorated with
``@pytest.fixture``. When a test function requests a fixture by name (as a
function argument), pytest automatically calls the fixture, provides its return
value to the test, and manages any cleanup afterwards.

Example
-------
A simple fixture that provides a temporary dictionary:

.. code-block:: python

   import pytest

   @pytest.fixture
   def empty_dict():
       return {}

   def test_insert(empty_dict):
       empty_dict["key"] = "value"
       assert empty_dict["key"] == "value"

Here, the test ``test_insert`` receives an empty dictionary from the fixture
``empty_dict``. Each time the test runs, pytest creates a fresh dictionary.

Scopes
------
Fixtures can have different scopes that control how often they are created:

- ``function``: (default) A new fixture instance is created for each test.
- ``class``: The fixture is created once per test class.
- ``module``: The fixture is created once per test module.
- ``session``: The fixture is created once for the entire test session.

Autouse fixtures
----------------
Fixtures can also be declared with ``autouse=True``. In this case, pytest will
automatically use the fixture in all relevant tests without the need to request
it explicitly.

Usage in this project
---------------------
In this project, fixtures are used extensively to:

- Provide isolated ``QSettings`` objects so tests do not pollute real user
  settings.
- Create and manage the ``MainWindow`` instance for UI tests, using ``pytest-qt``.
- Share common setup code (such as database state, API sessions, or application
  configuration) across multiple test files.

This makes tests more concise, easier to read, and less error-prone, while
ensuring proper setup and cleanup of resources.
