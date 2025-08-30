#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test fixtures for isolated application settings and main window.

This module provides pytest fixtures for testing a PyQt5 application
without interfering with the user's real `QSettings` or environment.
It ensures that tests are isolated, reproducible, and safe to run
without polluting persistent configuration.

Fixtures
--------
isolated_settings : pytest fixture
    Provides a temporary and isolated QSettings instance by
    monkeypatching the default QSettings constructor.
app : pytest fixture
    Provides a running instance of the application's MainWindow,
    initialized with a specific locale and managed by pytest-qt.
"""

import pytest
import tempfile
import os

from PyQt5.QtCore import QSettings
from pytestqt.qtbot import QtBot

from src.main import MainWindow

from typing import Generator
from typing import TypeVar

T = TypeVar("T")
YieldFixture = Generator[T, None, None]

@pytest.fixture(scope='function')
def isolated_settings(monkeypatch: pytest.MonkeyPatch) -> YieldFixture[QSettings]:
    """
    Fixture providing an isolated QSettings instance for testing.

    This fixture creates a temporary INI file and monkeypatches the
    ``QSettings`` constructor so that all new ``QSettings()`` calls
    within the test session will use the temporary instance.
    This prevents tests from affecting or reading the real
    application or system settings.

    The temporary settings file is automatically deleted after the
    test completes.

    Parameters
    ----------
    monkeypatch : pytest.MonkeyPatch
        Built-in pytest fixture that allows safe modification of
        attributes, environment variables, and modules during tests.

    Yields
    ------
    QSettings
        An isolated QSettings instance backed by a temporary INI file.

    Notes
    -----
    The fixture clears the settings and removes the temporary file
    during teardown.
    """
    # create a temporary file path
    fd, path = tempfile.mkstemp(suffix=".ini")
    os.close(fd)  # close the low-level file descriptor, QSettings will manage the file

    test_settings = QSettings(path, QSettings.IniFormat)

    # Monkeypatch so that QSettings() gives our test_settings
    monkeypatch.setattr("PyQt5.QtCore.QSettings", lambda *a, **kw: test_settings)

    yield test_settings

    # cleanup after test
    test_settings.clear()
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture(scope='function')
def app(request: pytest.FixtureRequest, qtbot: QtBot) -> YieldFixture[MainWindow]:
    """
    Fixture providing a running instance of the application's MainWindow.

    This fixture initializes the ``MainWindow`` with a given locale,
    temporarily overriding the application's language and server
    settings. It uses pytest-qt's ``qtbot`` to manage the Qt event loop
    and ensure proper cleanup of the window.

    Parameters
    ----------
    request : pytest.FixtureRequest
        Pytest fixture that allows parametrization of the fixture.
        If parametrized, the ``param`` attribute may contain a
        ``dict`` with a ``'locale'`` key to specify the desired locale.
        Defaults to ``'en_US'`` if not provided.
    qtbot : pytestqt.qtbot.QtBot
        Pytest-qt fixture for driving Qt widgets and applications
        during tests.

    Yields
    ------
    MainWindow
        A running instance of the application's main window, registered
        with pytest-qt for proper lifecycle management.

    Notes
    -----
    - The fixture saves the original ``language`` and ``server_name``
      settings and restores them after the test.
    - The main window is automatically closed during teardown.
    """
    if hasattr(request, 'param'):
        locale = request.param['locale'] if 'locale' in request.param else 'en_US'
    else:
        locale = 'en_US'
    settings: QSettings = QSettings("UPC", "BLOPUP_WINDOWS_APPLICATION")
    current_server_name: str = settings.value("server_name", '', str)
    current_language: str = settings.value("language", '', str)
    settings.setValue("language", locale)
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    yield window

    settings.setValue("language", current_language)
    settings.setValue("server_name", current_server_name)
    window.close()


