#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the About dialog (DlgAbout) of the application.

This module contains UI tests for verifying that the About dialog is shown
correctly, displays all expected widgets, and presents translated texts
depending on the application locale.

The tests use ``pytest-qt`` to drive the UI and ``QTimer`` to simulate
user interaction with the dialog.
"""

import pytest

from pytestqt.qtbot import QtBot
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtCore import Qt as Qt

from src.main import MainWindow
from src.ui.about import DlgAbout

@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_shown_00(qtbot: QtBot, isolated_settings: QSettings, app: MainWindow):
    """
    Test that the About dialog is displayed correctly.

    This test verifies that when the About action is triggered, the
    About dialog (``DlgAbout``) is shown, contains all expected labels,
    and can be closed via the OK button.

    Parameters
    ----------
    qtbot : pytestqt.qtbot.QtBot
        The pytest-qt bot used to interact with Qt widgets.
    isolated_settings : QSettings
        An isolated settings instance to prevent modification of
        persistent user settings.
    app : MainWindow
        The main application window fixture, parameterized with
        different locales.

    Notes
    -----
    - The test checks visibility of the dialog and its labels.
    - A ``QTimer`` is used to simulate interaction with the dialog
      after it appears.
    """
    def on_timer():
        dlg: DlgAbout = app.dlg
        qtbot.add_widget(dlg)
        assert dlg.isVisible()
        assert dlg.lbl_windows_application.isVisible()
        assert dlg.lbl_version.isVisible()
        assert dlg.lbl_icon_attributions.isVisible()
        assert len(dlg.lbl_icons) == 7
        for label in dlg.lbl_icons:
            assert label.isVisible()
        qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
        assert not dlg.isVisible()

    QTimer.singleShot(500, on_timer)
    app.toolbar_actions['about'].trigger()


@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_text_translations_00(qtbot: QtBot, isolated_settings: QSettings, app: MainWindow):
    """
    Test that the About dialog texts are translated correctly.

    This test verifies that the About dialog displays the correct
    translations for the window title and labels depending on the
    selected locale. It also checks that the dialog can be closed
    using the OK button.

    Parameters
    ----------
    qtbot : pytestqt.qtbot.QtBot
        The pytest-qt bot used to interact with Qt widgets.
    isolated_settings : QSettings
        An isolated settings instance to prevent modification of
        persistent user settings.
    app : MainWindow
        The main application window fixture, parameterized with
        different locales.

    Notes
    -----
    - The expected translations for each label are defined in a
      dictionary mapping locale codes to strings.
    - A ``QTimer`` is used to wait for the dialog to appear before
      performing assertions.
    """
    items = {
        'dialog': {
            'en_US': 'About',
            'ca_ES': 'Quant a BLOPUP',
            'es_ES': 'Acerca de BLOPUP',},
        'lbl_windows_application': {
            'en_US': 'BLOPUP Windows Application',
            'ca_ES': 'Aplicació de Windows de BLOPUP',
            'es_ES': 'Aplicación de Windows de BLOPUP',},
        'lbl_version': {
            'en_US': 'Version 0.9.0',
            'ca_ES': 'Versió 0.9.0',
            'es_ES': 'Versión 0.9.0',},
        'lbl_icon_attributions': {
            'en_US': 'Icon Attributions:',
            'ca_ES': 'Atribució de les icones:',
            'es_ES': 'Atribución de los iconos:',},
        'lbl_icon_1': {
            'en_US': '- Key by Alice Design from <a href="https://thenounproject.com/browse/icons/term/key/" target="_blank" title="Key Icons">Noun Project</a>',
            'ca_ES': '- Key per Alice Design de <a href="https://thenounproject.com/browse/icons/term/key/" target="_blank" title="Key Icons">Noun Project</a>',
            'es_ES': '- Key por Alice Design de <a href="https://thenounproject.com/browse/icons/term/key/" target="_blank" title="Key Icons">Noun Project</a>',},
        'lbl_icon_2': {
            'en_US': '- Lock by Aleksandr Vector from <a href="https://thenounproject.com/browse/icons/term/lock/" target="_blank" title="Lock Icons">Noun Project</a>',
            'ca_ES': '- Lock per Aleksandr Vector de <a href="https://thenounproject.com/browse/icons/term/lock/" target="_blank" title="Lock Icons">Noun Project</a>',
            'es_ES': '- Lock por Aleksandr Vector de <a href="https://thenounproject.com/browse/icons/term/lock/" target="_blank" title="Lock Icons">Noun Project</a>', },
        'lbl_icon_3': {
            'en_US': '- Search User by Wilson Joseph from <a href="https://thenounproject.com/browse/icons/term/search-user/" target="_blank" title="Search User Icons">Noun Project</a>',
            'ca_ES': '- Search User per Wilson Joseph de <a href="https://thenounproject.com/browse/icons/term/search-user/" target="_blank" title="Search User Icons">Noun Project</a>',
            'es_ES': '- Search User por Wilson Joseph de <a href="https://thenounproject.com/browse/icons/term/search-user/" target="_blank" title="Search User Icons">Noun Project</a>', },
        'lbl_icon_4': {
            'en_US': '- Add User by Wilson Joseph from <a href="https://thenounproject.com/browse/icons/term/add-user/" target="_blank" title="Add User Icons">Noun Project</a>',
            'ca_ES': '- Add User per Wilson Joseph de <a href="https://thenounproject.com/browse/icons/term/add-user/" target="_blank" title="Add User Icons">Noun Project</a>',
            'es_ES': '- Add User por Wilson Joseph de <a href="https://thenounproject.com/browse/icons/term/add-user/" target="_blank" title="Add User Icons">Noun Project</a>', },
        'lbl_icon_5': {
            'en_US': '- Medical appointment by Minh Do from <a href="https://thenounproject.com/browse/icons/term/medical-appointment/" target="_blank" title="medical appointment Icons">Noun Project</a>',
            'ca_ES': '- Medical appointment per Minh Do de <a href="https://thenounproject.com/browse/icons/term/medical-appointment/" target="_blank" title="medical appointment Icons">Noun Project</a>',
            'es_ES': '- Medical appointment por Minh Do de <a href="https://thenounproject.com/browse/icons/term/medical-appointment/" target="_blank" title="medical appointment Icons">Noun Project</a>', },
        'lbl_icon_6': {
            'en_US': '- About by Adrian Adam from <a href="https://thenounproject.com/browse/icons/term/about/" target="_blank" title="about Icons">Noun Project</a>',
            'ca_ES': '- About per Adrian Adam de <a href="https://thenounproject.com/browse/icons/term/about/" target="_blank" title="about Icons">Noun Project</a>',
            'es_ES': '- About por Adrian Adam de <a href="https://thenounproject.com/browse/icons/term/about/" target="_blank" title="about Icons">Noun Project</a>', },
        'lbl_icon_7': {
            'en_US': '- Settings by i cons from <a href="https://thenounproject.com/browse/icons/term/settings/" target="_blank" title="Settings Icons">Noun Project</a>',
            'ca_ES': '- Settings per i cons de <a href="https://thenounproject.com/browse/icons/term/settings/" target="_blank" title="Settings Icons">Noun Project</a>',
            'es_ES': '- Settings por i cons de <a href="https://thenounproject.com/browse/icons/term/settings/" target="_blank" title="Settings Icons">Noun Project</a>', },
    }

    def on_timer():
        dlg: DlgAbout = app.dlg
        qtbot.add_widget(dlg)
        assert dlg.windowTitle() == items['dialog'][app.current_language]
        assert getattr(dlg, 'lbl_windows_application').text() == items['lbl_windows_application'][app.current_language]
        assert getattr(dlg, 'lbl_version').text() == items['lbl_version'][app.current_language]
        assert getattr(dlg, 'lbl_icon_attributions').text() == items['lbl_icon_attributions'][app.current_language]
        for i in range(1, 8):
            assert getattr(dlg, f'lbl_icon_{i}').text() == items[f'lbl_icon_{i}'][app.current_language]
        qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
        assert not dlg.isVisible()

    QTimer.singleShot(500, on_timer)
    app.toolbar_actions['about'].trigger()
