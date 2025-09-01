#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from pytestqt.qtbot import QtBot
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtCore import Qt as Qt

from src.main import MainWindow
from src.ui.settings import DlgSettings

@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_shown_00(qtbot: QtBot, isolated_settings: QSettings, app: MainWindow):
    def on_timer():
        dlg: DlgSettings = app.dlg
        qtbot.add_widget(dlg)
        assert dlg.isVisible()
        assert dlg.group_box_server.isVisible()
        assert dlg.label_server_name.isVisible()
        assert dlg.line_edit_server_name.isVisible()
        assert dlg.group_box_locale.isVisible()
        assert dlg.label_language_selection.isVisible()
        assert dlg.combo_box_language.isVisible()
        assert dlg.combo_box_language.count() == 4
        qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
        assert not dlg.isVisible()

    QTimer.singleShot(500, on_timer)
    app.toolbar_actions['setup'].trigger()


@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_text_translations_00(qtbot: QtBot, isolated_settings: QSettings, app: MainWindow):
    items = {
        'dialog': {
            'en_US': 'Settings',
            'ca_ES': 'Configuració',
            'es_ES': 'Configuración',},
        'group_box_server': {
            'en_US': 'Server',
            'ca_ES': 'Servidor',
            'es_ES': 'Servidor',},
        'label_server_name': {
            'en_US': 'Server Name:',
            'ca_ES': 'Nom del servidor:',
            'es_ES': 'Nombre del servidor:',},
        'group_box_locale': {
            'en_US': 'Locale Information',
            'ca_ES': 'Informació de la configuració regional',
            'es_ES': 'Información de la configuración regional',},
        'label_language_selection': {
            'en_US': 'Language Selection:',
            'ca_ES': "Selecció d'idioma:",
            'es_ES': 'Selección de idioma:',},
        'combo_box_language': {
            'en_US': 'System Default',
            'ca_ES': 'Català',
            'es_ES': 'Español', },
    }
    def on_timer():
        dlg: DlgSettings = app.dlg
        qtbot.add_widget(dlg)
        assert dlg.windowTitle() == items['dialog'][app.current_language]
        assert dlg.group_box_server.title() == items['group_box_server'][app.current_language]
        assert getattr(dlg, 'label_server_name').text() == items['label_server_name'][app.current_language]
        assert dlg.group_box_locale.title() == items['group_box_locale'][app.current_language]
        assert getattr(dlg, 'label_language_selection').text() == items['label_language_selection'][app.current_language]
        idx: int = dlg.combo_box_language.currentIndex()
        assert dlg.combo_box_language.itemText(idx) == items['combo_box_language'][app.current_language]
        qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
        assert not dlg.isVisible()

    QTimer.singleShot(500, on_timer)
    app.toolbar_actions['setup'].trigger()

@pytest.mark.parametrize('dlg_settings', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_properties_01(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog without any initialization is correctly shown

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    assert dlg_settings.combo_box_language.count() == 4
    assert dlg_settings.language == QLocale.system().name()
    assert dlg_settings.server_name is None
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)


@pytest.mark.parametrize('dlg_settings', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_properties_02(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog Changing the language values

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    qtbot.keyClicks(dlg_settings.combo_box_language, 'es_ES')
    assert dlg_settings.language == 'es_ES'
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)


@pytest.mark.parametrize('dlg_settings', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_properties_03(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog Changing the server value

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    qtbot.keyClicks(dlg_settings.line_edit_server_name, 'server.com')
    assert dlg_settings.server_name == 'server.com'
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)


@pytest.mark.parametrize('dlg_settings', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_properties_04(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog initializing the language values

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    dlg_settings.language = 'es_ES'
    assert dlg_settings.language == 'es_ES'
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)


@pytest.mark.parametrize('dlg_settings', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_properties_05(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog initializing the server value

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    dlg_settings.server_name = 'server.com'
    assert dlg_settings.server_name == 'server.com'
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)


def test_properties_06(qtbot: QtBot, dlg_settings: DlgSettings):
    """
    Test the settings dialog failing in selecting the language. For example in a computer that we do not have a
    language translation

    :param qtbot: QT Fixture
    :type qtbot: QtBot
    :param dlg_settings: Patient Dialog
    :type dlg_settings: DlgSettings
    :return: None
    """

    dlg_settings.language = 'it_IT'
    assert dlg_settings.language == QLocale.system().name()
    qtbot.mouseClick(dlg_settings.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)