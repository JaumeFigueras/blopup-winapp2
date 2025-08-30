#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import requests
import requests_mock
from pytestqt.qtbot import QtBot

from PyQt5.QtCore import QTimer, QSettings
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt as Qt

from src.main import MainWindow
# from src.ui.settings import DlgSettings
# from src.ui.login import DlgLogin
# from src.remote_api.open_mrs_api import LOCATION_LIST
# from src.remote_api.open_mrs_api import LOGIN
# from src.remote_api.open_mrs_api import PATIENT_IDENTIFIER_TYPE_LIST
# from src.remote_api.open_mrs_api import LOGOUT
# from src.data_models.user import User
# from src.data_models.location import Location
# from src.data_models.patient_identifier_type import PatientIdentifierType

@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_shown_00(isolated_settings: QSettings, app: MainWindow):
    """
    Test that the main window displays toolbar and menu actions correctly.

    This test verifies that, for different locales, the application's
    main window is created with the expected number of toolbar and
    menu actions, and that all actions have valid icons. It also checks
    that the window is visible after being shown.

    Parameters
    ----------
    isolated_settings : QSettings
        Isolated settings fixture ensuring tests do not pollute
        the real application settings.
    app : MainWindow
        Main application window fixture initialized with different
        locales via pytest parametrization.

    Notes
    -----
    - The number of toolbar actions is exactly 7.
    - Each toolbar action is a ``QAction`` with a valid ``QIcon``.
    - The number of menu actions is exactly 7.
    - Each menu action is a ``QAction`` with a valid ``QIcon``.
    - The main window is visible.
    """
    assert len(app.toolbar_actions) == 7
    for (key, action) in app.toolbar_actions.items():
        assert isinstance(app.toolbar_actions[key], QAction)
        assert isinstance(app.toolbar_actions[key].icon(), QIcon)
    assert len(app.menu_actions) == 7
    for (key, action) in app.menu_actions.items():
        assert isinstance(app.menu_actions[key], QAction)
        assert isinstance(app.menu_actions[key].icon(), QIcon)
    assert app.isVisible()

@pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
def test_text_translations_00(isolated_settings: QSettings, app: MainWindow):
    """
    Test that toolbar and menu action texts are correctly translated.

    This test validates that, for different locales, the text of each
    action in the toolbar and menu matches the expected translation.
    It also verifies that the application window title is correctly
    set.

    Parameters
    ----------
    isolated_settings : QSettings
        Isolated settings fixture ensuring tests do not affect
        persistent application settings.
    app : MainWindow
        Main application window fixture initialized with different
        locales via pytest parametrization.

    Notes
    -----
    - The text of each toolbar and menu action matches the expected
      translation for the current locale.
    - The main window title is ``'BLOPUP'``.
    """
    items = {
        'login': {'en_US': 'Login', 'ca_ES': 'Iniciar sessió','es_ES': 'Iniciar sessión',},
        'logout': {'en_US': 'Logout', 'ca_ES': 'Tancar sessió','es_ES': 'Cerrar sessión',},
        'search_patient': {'en_US': 'Search Patient', 'ca_ES': 'Cerca un pacient','es_ES': 'Busca un paciente',},
        'add_patient': {'en_US': 'Add Patient', 'ca_ES': 'Afegeix un pacient','es_ES': 'Añade un paciente',},
        'visit_patient': {'en_US': 'Visit Patient', 'ca_ES': 'Visita un pacient','es_ES': 'Visita un paciente',},
        'setup': {'en_US': 'Setup', 'ca_ES': 'Configuració','es_ES': 'Ajustes',},
        'about': {'en_US': 'About', 'ca_ES': 'Quant a BLOPUP','es_ES': 'Acerca de BLOPUP',},
    }
    for key, texts in items.items():
        assert app.toolbar_actions[key].text() == texts[app.current_language]
        assert app.menu_actions[key].text() == texts[app.current_language]
    assert app.windowTitle() == 'BLOPUP'


# def test_retranslate_01(qtbot: QtBot, app: MainWindow):
#     """
#     Tests the change of the language through the setup dialog
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer():
#         dlg: DlgSettings = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.keyClicks(dlg.combo_box_language, 'ca_ES')
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#
#     QTimer.singleShot(500, on_timer)
#     app.toolbar_actions['setup'].trigger()
#     qtbot.waitUntil(lambda: app.current_language == 'ca_ES')
#     test_translation_01(qtbot, app)
#
#
# def test_retranslate_02(qtbot: QtBot, app: MainWindow):
#     """
#     Tests the change of the language through the setup dialog
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer():
#         dlg: DlgSettings = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.keyClicks(dlg.combo_box_language, 'es_ES')
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#
#     QTimer.singleShot(500, on_timer)
#     app.toolbar_actions['setup'].trigger()
#     qtbot.waitUntil(lambda: app.current_language == 'es_ES')
#     test_translation_01(qtbot, app)
#
#
# @pytest.mark.parametrize('app', [{'locale': 'en_US'}, {'locale': 'ca_ES'}, {'locale': 'es_ES'}, {'locale': ''}], indirect=True)
# def test_translation_01(qtbot: QtBot, app: MainWindow):
#     """
#     Tests the translation
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     locale: str = QLocale().name()
#     if locale == 'ca_ES':
#         assert app.windowTitle() == "BLOPUP"
#         assert app.toolbar_action_setup.text() == "Configuració"
#         assert app.menu_action_setup.text() == app.toolbar_action_setup.text()
#         assert app.toolbar_action_login.text() == "Iniciar sessió"
#         assert app.menu_action_login.text() == app.toolbar_action_login.text()
#         assert app.toolbar_action_logout.text() == "Tancar sessió"
#         assert app.menu_action_logout.text() == app.toolbar_action_logout.text()
#         assert app.toolbar_action_about.text() == "Quant a BLOPUP"
#         assert app.menu_action_about.text() == app.toolbar_action_about.text()
#         assert app.toolbar_action_search_patient.text() == "Cerca un pacient"
#         assert app.menu_action_search_patient.text() == app.toolbar_action_search_patient.text()
#         assert app.toolbar_action_add_patient.text() == "Afegeix un pacient"
#         assert app.menu_action_add_patient.text() == app.toolbar_action_add_patient.text()
#         assert app.toolbar_action_visit.text() == "Visita un pacient"
#         assert app.menu_action_visit.text() == app.toolbar_action_visit.text()
#         assert app.label_status_user.text().startswith("Usuari:")
#     elif locale == 'es_ES':
#         assert app.windowTitle() == "BLOPUP"
#         assert app.toolbar_action_setup.text() == "Ajustes"
#         assert app.menu_action_setup.text() == app.toolbar_action_setup.text()
#         assert app.toolbar_action_login.text() == "Iniciar sessión"
#         assert app.menu_action_login.text() == app.toolbar_action_login.text()
#         assert app.toolbar_action_logout.text() == "Cerrar sessión"
#         assert app.menu_action_logout.text() == app.toolbar_action_logout.text()
#         assert app.toolbar_action_about.text() == "Acerca de BLOPUP"
#         assert app.menu_action_about.text() == app.toolbar_action_about.text()
#         assert app.toolbar_action_search_patient.text() == "Busca un paciente"
#         assert app.menu_action_search_patient.text() == app.toolbar_action_search_patient.text()
#         assert app.toolbar_action_add_patient.text() == "Añade un paciente"
#         assert app.menu_action_add_patient.text() == app.toolbar_action_add_patient.text()
#         assert app.toolbar_action_visit.text() == "Visita un paciente"
#         assert app.menu_action_visit.text() == app.toolbar_action_visit.text()
#         assert app.label_status_user.text().startswith("Usuario:")
#     else:
#         assert app.windowTitle() == "BLOPUP"
#         assert app.toolbar_action_setup.text() == "Setup"
#         assert app.menu_action_setup.text() == app.toolbar_action_setup.text()
#         assert app.toolbar_action_login.text() == "Login"
#         assert app.menu_action_login.text() == app.toolbar_action_login.text()
#         assert app.toolbar_action_logout.text() == "Logout"
#         assert app.menu_action_logout.text() == app.toolbar_action_logout.text()
#         assert app.toolbar_action_about.text() == "About"
#         assert app.menu_action_about.text() == app.toolbar_action_about.text()
#         assert app.toolbar_action_search_patient.text() == "Search Patient"
#         assert app.menu_action_search_patient.text() == app.toolbar_action_search_patient.text()
#         assert app.toolbar_action_add_patient.text() == "Add Patient"
#         assert app.menu_action_add_patient.text() == app.toolbar_action_add_patient.text()
#         assert app.toolbar_action_visit.text() == "Visit Patient"
#         assert app.menu_action_visit.text() == app.toolbar_action_visit.text()
#         assert app.label_status_user.text().startswith("User:")
#
#
# def test_setup_01(qtbot: QtBot, app: MainWindow) -> None:
#     """
#     Tests that the server is None
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer():
#         dlg: DlgSettings = app.dlg
#         qtbot.add_widget(dlg)
#         dlg.line_edit_server_name.clear()
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#
#     QTimer.singleShot(500, on_timer)
#     app.toolbar_actions['setup'].trigger()
#     qtbot.waitUntil(lambda: app.current_server_name is None)
#     for (key, action) in app.toolbar_actions.items():
#         if key == 'setup' or key == 'about':
#             assert action.isEnabled()
#         else:
#             assert not action.isEnabled()
#     qtbot.waitUntil(lambda: app.dlg is None)
#
#
# def test_setup_02(qtbot: QtBot, app: MainWindow) -> None:
#     """
#     Tests that the server has changed
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer() -> None:
#         dlg: DlgSettings = app.dlg
#         qtbot.add_widget(dlg)
#         dlg.line_edit_server_name.clear()
#         qtbot.keyClicks(dlg.line_edit_server_name, 'new_server.com')
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#
#     QTimer.singleShot(500, on_timer)
#     app.toolbar_actions['setup'].trigger()
#     qtbot.waitUntil(lambda: app.current_server_name == 'new_server.com')
#     for (key, action) in app.toolbar_actions.items():
#         if key == 'setup' or key == 'about' or key == 'login':
#             assert action.isEnabled()
#         else:
#             assert not action.isEnabled()
#     qtbot.waitUntil(lambda: app.dlg is None)
#
#
# def test_login_01(qtbot: QtBot, app: MainWindow) -> None:
#     """
#     Tests that the locations can't be retrieved and an error message box is displayed
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer() -> None:
#         msg: QMessageBox = app.msg
#         qtbot.add_widget(msg)
#         assert msg.isVisible()
#         qtbot.mouseClick(msg.button(QMessageBox.StandardButton.Ok), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_server_name = 'blopup-test.upc.edu'
#         url = LOCATION_LIST.format('blopup-test.upc.edu')
#         rm.get(url, exc=requests.exceptions.HTTPError)
#         QTimer.singleShot(500, on_timer)
#         app.toolbar_actions['login'].trigger()
#         qtbot.waitUntil(lambda: app.msg is None)
#         qtbot.waitUntil(lambda: app.dlg is None)
#
#
# def test_login_02(qtbot: QtBot, app: MainWindow, person_location_list_string: str) -> None:
#     """
#     Tests that the dialog is cancelled and nothing changes
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer() -> None:
#         dlg: DlgLogin = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Cancel), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_server_name = 'blopup-test.upc.edu'
#         user = User(open_mrs_uuid="1234", username="User12")
#         app.current_user = user
#         location = Location(open_mrs_uuid="5678", name="loc")
#         app.current_location = location
#         url = LOCATION_LIST.format('blopup-test.upc.edu')
#         rm.get(url, text=person_location_list_string)
#         QTimer.singleShot(500, on_timer)
#         app.toolbar_actions['login'].trigger()
#         qtbot.waitUntil(lambda: app.dlg is None)
#         assert user == app.current_user
#         assert location == app.current_location
#
#
# def test_login_03(qtbot: QtBot, app: MainWindow, person_location_list_string: str, login_error_string: str) -> None:
#     """
#     Tests that the user provide wrong credentials
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer_01() -> None:
#         dlg: DlgLogin = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.keyClicks(dlg.line_edit_username, 'user')
#         qtbot.keyClicks(dlg.line_edit_password, 'pass')
#         qtbot.keyClicks(dlg.combo_box_location, 'Laboratory')
#         QTimer.singleShot(500, on_timer_02)
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#         qtbot.waitUntil(lambda: app.msg is None)
#
#     def on_timer_02() -> None:
#         msg: QMessageBox = app.msg
#         qtbot.add_widget(msg)
#         assert msg.isVisible()
#         qtbot.mouseClick(msg.button(QMessageBox.StandardButton.Ok), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_server_name = 'blopup-test.upc.edu'
#         user = User(open_mrs_uuid="1234", username="User12")
#         app.current_user = user
#         location = Location(open_mrs_uuid="5678", name="loc")
#         app.current_location = location
#         url = LOCATION_LIST.format('blopup-test.upc.edu')
#         rm.get(url, text=person_location_list_string)
#         url = LOGIN.format('blopup-test.upc.edu')
#         rm.get(url, text=login_error_string)
#         QTimer.singleShot(500, on_timer_01)
#         app.toolbar_actions['login'].trigger()
#         qtbot.waitUntil(lambda: app.dlg is None)
#         assert user == app.current_user
#         assert location == app.current_location
#
#
# def test_login_04(qtbot: QtBot, app: MainWindow, person_location_list_string: str, login_string: str) -> None:
#     """
#     Tests that the user provide correct credentials but no identifier types are correctly get
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :param person_location_list_string: Fixture with the response to a location query in OpenMRS
#     :type person_location_list_string: str
#     :param login_string: Fixture with the response to a successful session login
#     :type login_string: str
#     :return: None
#     """
#
#     def on_timer_01() -> None:
#         dlg: DlgLogin = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.keyClicks(dlg.line_edit_username, 'user')
#         qtbot.keyClicks(dlg.line_edit_password, 'pass')
#         qtbot.keyClicks(dlg.combo_box_location, 'Laboratory')
#         QTimer.singleShot(500, on_timer_02)
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#         qtbot.waitUntil(lambda: app.msg is None)
#
#     def on_timer_02() -> None:
#         msg: QMessageBox = app.msg
#         qtbot.add_widget(msg)
#         assert msg.isVisible()
#         qtbot.mouseClick(msg.button(QMessageBox.StandardButton.Ok), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_server_name = 'blopup-test.upc.edu'
#         user = User(open_mrs_uuid="1234", username="User12")
#         app.current_user = user
#         location = Location(open_mrs_uuid="5678", name="loc")
#         app.current_location = location
#         url = LOCATION_LIST.format('blopup-test.upc.edu')
#         rm.get(url, text=person_location_list_string)
#         url = LOGIN.format('blopup-test.upc.edu')
#         rm.get(url, text=login_string)
#         url = PATIENT_IDENTIFIER_TYPE_LIST.format('blopup-test.upc.edu')
#         rm.get(url, exc=requests.exceptions.HTTPError)
#         QTimer.singleShot(500, on_timer_01)
#         app.toolbar_actions['login'].trigger()
#         qtbot.waitUntil(lambda: app.dlg is None)
#         assert User(username='user', password='pass') == app.current_user
#         assert Location(open_mrs_uuid='7fdfa2cb-bc95-405a-88c6-32b7673c0453', name='Laboratory') == app.current_location
#
#
# def test_login_05(qtbot: QtBot, app: MainWindow, person_location_list_string: str, login_string: str,
#                   patient_identifier_type_list_string: str) -> None:
#     """
#     Tests that the user provide correct credentials
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :param person_location_list_string: Fixture with the response to a location query in OpenMRS
#     :type person_location_list_string: str
#     :param login_string: Fixture with the response to a successful session login
#     :type login_string: str
#     :param person_location_list_string: Fixture with the response to a patient identifier type query in OpenMRS
#     :type person_location_list_string: str
#     :return: None
#     """
#
#     def on_timer_01() -> None:
#         dlg: DlgLogin = app.dlg
#         qtbot.add_widget(dlg)
#         qtbot.keyClicks(dlg.line_edit_username, 'user')
#         qtbot.keyClicks(dlg.line_edit_password, 'pass')
#         qtbot.keyClicks(dlg.combo_box_location, 'Laboratory')
#         qtbot.mouseClick(dlg.buttonbox.button(QDialogButtonBox.Ok), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_server_name = 'blopup-test.upc.edu'
#         user = User(open_mrs_uuid="1234", username="User12")
#         app.current_user = user
#         location = Location(open_mrs_uuid="5678", name="loc")
#         app.current_location = location
#         url = LOCATION_LIST.format('blopup-test.upc.edu')
#         rm.get(url, text=person_location_list_string)
#         url = LOGIN.format('blopup-test.upc.edu')
#         rm.get(url, text=login_string)
#         url = PATIENT_IDENTIFIER_TYPE_LIST.format('blopup-test.upc.edu')
#         rm.get(url, text=patient_identifier_type_list_string)
#         QTimer.singleShot(500, on_timer_01)
#         app.toolbar_actions['login'].trigger()
#         qtbot.waitUntil(lambda: app.dlg is None)
#         assert User(username='user', password='pass') == app.current_user
#         assert Location(open_mrs_uuid='7fdfa2cb-bc95-405a-88c6-32b7673c0453', name='Laboratory') == app.current_location
#         assert len(app.current_patient_identifier_types) == 7
#         for (k, v) in app.current_patient_identifier_types.items():
#             assert isinstance(v, PatientIdentifierType)
#         assert not app.menu_action_login.isEnabled()
#         assert app.menu_action_logout.isEnabled()
#         assert app.menu_action_search_patient.isEnabled()
#         assert app.menu_action_add_patient.isEnabled()
#         assert app.menu_action_visit.isEnabled()
#         assert not app.toolbar_action_login.isEnabled()
#         assert app.toolbar_action_logout.isEnabled()
#         assert app.toolbar_action_search_patient.isEnabled()
#         assert app.toolbar_action_add_patient.isEnabled()
#         assert app.toolbar_action_visit.isEnabled()
#
#
# def test_logout_01(qtbot: QtBot, app: MainWindow) -> None:
#     """
#     Tests the logout function
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     def on_timer_01() -> None:
#         msg: QMessageBox = app.msg
#         qtbot.add_widget(msg)
#         assert msg.isVisible()
#         qtbot.mouseClick(msg.button(QMessageBox.StandardButton.Ok), Qt.LeftButton)
#
#     with requests_mock.Mocker() as rm:
#         app.current_user = User(username='user', password='pass')
#         app.current_server_name = 'blopup-test.upc.edu'
#         app.menu_action_login.setEnabled(False)
#         app.menu_action_logout.setEnabled(True)
#         app.menu_action_search_patient.setEnabled(True)
#         app.menu_action_add_patient.setEnabled(True)
#         app.menu_action_visit.setEnabled(True)
#         app.toolbar_action_login.setEnabled(False)
#         app.toolbar_action_logout.setEnabled(True)
#         app.toolbar_action_search_patient.setEnabled(True)
#         app.toolbar_action_add_patient.setEnabled(True)
#         app.toolbar_action_visit.setEnabled(True)
#         url = LOGOUT.format('blopup-test.upc.edu')
#         rm.delete(url, exc=requests.exceptions.HTTPError)
#         QTimer.singleShot(500, on_timer_01)
#         app.toolbar_actions['logout'].trigger()
#         qtbot.waitUntil(lambda: app.current_user is None)
#         qtbot.waitUntil(lambda: app.current_location is None)
#         qtbot.waitUntil(lambda: app.current_patient_identifier_types is None)
#         assert app.menu_action_login.isEnabled()
#         assert not app.menu_action_logout.isEnabled()
#         assert not app.menu_action_search_patient.isEnabled()
#         assert not app.menu_action_add_patient.isEnabled()
#         assert not app.menu_action_visit.isEnabled()
#         assert app.toolbar_action_login.isEnabled()
#         assert not app.toolbar_action_logout.isEnabled()
#         assert not app.toolbar_action_search_patient.isEnabled()
#         assert not app.toolbar_action_add_patient.isEnabled()
#         assert not app.toolbar_action_visit.isEnabled()
#
#
# def test_logout_02(qtbot: QtBot, app: MainWindow) -> None:
#     """
#     Tests the logout function
#
#     :param qtbot: QT Fixture
#     :type qtbot: QtBot
#     :param app: Application Main Window
#     :type app: MainWindow
#     :return: None
#     """
#
#     with requests_mock.Mocker() as rm:
#         app.current_user = User(username='user', password='pass')
#         app.current_server_name = 'blopup-test.upc.edu'
#         app.menu_action_login.setEnabled(False)
#         app.menu_action_logout.setEnabled(True)
#         app.menu_action_search_patient.setEnabled(True)
#         app.menu_action_add_patient.setEnabled(True)
#         app.menu_action_visit.setEnabled(True)
#         app.toolbar_action_login.setEnabled(False)
#         app.toolbar_action_logout.setEnabled(True)
#         app.toolbar_action_search_patient.setEnabled(True)
#         app.toolbar_action_add_patient.setEnabled(True)
#         app.toolbar_action_visit.setEnabled(True)
#         url = LOGOUT.format('blopup-test.upc.edu')
#         rm.delete(url, status_code=204)
#         app.toolbar_actions['logout'].trigger()
#         qtbot.waitUntil(lambda: app.current_user is None)
#         qtbot.waitUntil(lambda: app.current_location is None)
#         qtbot.waitUntil(lambda: app.current_patient_identifier_types is None)
#         assert app.menu_action_login.isEnabled()
#         assert not app.menu_action_logout.isEnabled()
#         assert not app.menu_action_search_patient.isEnabled()
#         assert not app.menu_action_add_patient.isEnabled()
#         assert not app.menu_action_visit.isEnabled()
#         assert app.toolbar_action_login.isEnabled()
#         assert not app.toolbar_action_logout.isEnabled()
#         assert not app.toolbar_action_search_patient.isEnabled()
#         assert not app.toolbar_action_add_patient.isEnabled()
#         assert not app.toolbar_action_visit.isEnabled()
#
