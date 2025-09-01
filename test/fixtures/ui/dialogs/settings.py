#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dlg_about fixture for testing the About dialog.

This module defines a pytest fixture that creates and manages the lifecycle
of the :class:`~src.ui.about.DlgAbout` dialog for use in unit and UI tests.
It ensures that the dialog is shown with the correct locale, integrated
with the Qt testing environment provided by ``pytest-qt``, and cleaned up
after the test finishes.
"""

import pytest

from src.main import MainWindow
from src.ui.settings import DlgSettings

from PyQt5.QtCore import QLocale
from PyQt5.QtCore import QSettings
from pytestqt.qtbot import QtBot

from typing import Generator
from typing import TypeVar

T = TypeVar("T")
YieldFixture = Generator[T, None, None]

@pytest.fixture
def dlg_settings(request: pytest.FixtureRequest, qtbot: QtBot, isolated_settings: QSettings, app: MainWindow) -> YieldFixture[DlgSettings]:
    """
    Fixture that provides an initialized :class:`~src.ui.about.DlgSettings` dialog.

    This fixture creates and displays the *Settings* dialog, ensuring that it is
    initialized with the appropriate locale and properly integrated into the
    test environment. The dialog is automatically closed when the test ends.

    Parameters
    ----------
    request : pytest.FixtureRequest
        The pytest request object, which can carry parameters to the fixture.
        If ``request.param`` contains a ``'locale'`` key, that locale will be
        used; otherwise, the default ``'en_US'`` locale is applied.
    qtbot : pytestqt.qtbot.QtBot
        The Qt test bot fixture used to simulate user interactions and
        manage Qt widgets in tests.
    app : MainWindow
        The main application window that serves as the parent for the dialog.

    Yields
    ------
    DlgSettings
        An instance of the *Settings* dialog, shown and registered with the
        Qt testing environment.

    Notes
    -----
    - The fixture ensures the dialog is closed after the test to prevent
      resource leaks.
    - Useful for UI tests that need to verify labels, translations, or
      visibility of elements in the *About* dialog.
    """
    if hasattr(request, 'param'):
        locale = request.param['locale'] if 'locale' in request.param else 'en_US'
    else:
        locale = 'en_US'
    QLocale().setDefault(QLocale(locale))
    dlg: DlgSettings = DlgSettings(app)
    dlg.show()
    qtbot.add_widget(dlg)

    yield dlg

    dlg.close()
