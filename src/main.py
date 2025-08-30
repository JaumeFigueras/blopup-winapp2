#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import random
import pathlib
import sys
import src.resources  # noqa loads the QT compiled resources
import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QTranslator
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QShowEvent
from PyQt5.QtGui import QCloseEvent
from PyQt5 import uic  # noqa: There is a bug in pycharm with uic
from PyQt5.sip import voidptr
from PyQt5.QtCore import QByteArray

from typing import Union
from typing import Tuple
from typing import Dict
from typing import Any
from typing import Optional

# from src.ui.about import DlgAbout
# from src.ui.settings import DlgSettings
# from src.ui.patient import DlgPatient
# from src.ui.login import DlgLogin
# from src.ui.search_patient import DlgSearchPatient
# from src.data_models.patient import Patient
# from src.data_models.user import User
# from src.data_models.location import Location
# from src.data_models.patient_identifier_type import PatientIdentifierType
# from src.data_models.patient_identifier import PatientIdentifier
# from src.data_models.patient_identifier import IdentifierCategory
# from src.data_models import Base
# from src.data_models.person import Person
# from src.data_models.person_name import PersonName
# from src.data_models.person_attribute_type import PersonAttributeType
# from src.data_models.person_attribute import PersonAttribute
# from src.data_models.person_address import PersonAddress
# from src.data_models.categories.person_attributes_categories import GenderCategory
# from src.data_models.visit_type import VisitType
# from src.remote_api.open_mrs_api import login
# from src.remote_api.open_mrs_api import logout
# from src.remote_api.open_mrs_api import get_locations
# from src.remote_api.open_mrs_api import get_patient_identifier_type_list
# from src.remote_api.open_mrs_api import get_visit_type_list
# from src.remote_api.open_mrs_api import get_patient
# from src.remote_api.open_mrs_api import get_visit_list


if platform.system() == 'Windows':  # pragma: no cover
    import clr  # noqa due to .NET call
    import ctypes.wintypes  # noqa due to .NET call
    sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve() / 'lib'))
    clr.AddReference('System')  # noqa due to .NET call
    from System import IntPtr, Int32, Int64  # noqa due to .NET call
    clr.AddReference('System.Windows.Forms')  # noqa due to .NET call
    from System.Windows.Forms import Message  # noqa due to .NET call
    clr.AddReference("System.Collections")  # noqa due to .NET call
    from System.Collections.Generic import List  # noqa due to .NET call
    clr.AddReference('WatchBPHome')  # noqa due to .NET call
    import WatchBPHome  # noqa due to .NET call

VERSION = "0.9.0"

class MainWindow(QMainWindow):
    # Elements automatically created when uic loads the main window UI
    menu_main: QMenuBar
    tool_bar_main: QToolBar
    status_main: QStatusBar
    label_status_network: QLabel
    label_status_user: QLabel
    # Variable to hold Dialogs and Message boxes during its visible state
    # dlg: Union[DlgPatient, DlgSettings, DlgLogin, DlgSearchPatient, None] = None
    msg: Union[QMessageBox, None] = None
    # Current application user
    # current_user: Union[User, None] = None
    # current_location: Union[Location, None] = None
    # current_patient_identifier_types: Union[Dict[str, PatientIdentifierType], None] = None
    # current_visit_types: Union[Dict[str, VisitType], None] = None
    # locations: Union[Dict[str, Location], None] = None
    # patient_identifiers: Union[Dict[str, PatientIdentifier], None] = None
    # locations_by_uuid: Union[Dict[str, Location], None] = None

    def __init__(self) -> None:
        super().__init__()
        # Load the main window GUI
        current_dir = pathlib.Path(__file__).parent.resolve()
        uic.loadUi(str(current_dir) + '/ui/main_window.ui', self)
        # Widgets (menus and toolbar buttons) needed to manage the main GUI
        self.menu_action_login: Optional[QAction] = None
        self.toolbar_action_login: Optional[QAction] = None
        self.menu_action_logout: Optional[QAction] = None
        self.toolbar_action_logout: Optional[QAction] = None
        self.menu_action_search_patient: Optional[QAction] = None
        self.toolbar_action_search_patient: Optional[QAction] = None
        self.menu_action_add_patient: Optional[QAction] = None
        self.toolbar_action_add_patient: Optional[QAction] = None
        self.menu_action_visit: Optional[QAction] = None
        self.toolbar_action_visit: Optional[QAction] = None
        self.menu_action_setup: Optional[QAction] = None
        self.toolbar_action_setup: Optional[QAction] = None
        self.menu_action_about: Optional[QAction] = None
        self.toolbar_action_about: Optional[QAction] = None
        self.menu_actions: Dict[str, QAction] = dict()
        self.toolbar_actions: Dict[str, QAction] = dict()
        self.shown: bool = False
        # Initialization of the blood pressure reader only if the application is running under Windows
        if platform.system() == 'Windows':  # pragma: no cover
            self.HWND: Optional[voidptr] = None
            self.watchBPHomeHid = WatchBPHome.WatchBPHomeHid()
            self.watchBPHomeHid.InitWatchBPSDK("as2v1zrZti!pq0+y")
            self.watchBPHomeHid.SpecifiedDeviceRemoved += self.hid_removed
            self.watchBPHomeHid.SpecifiedDeviceArrived += self.hid_arrived
            self.status_hid = 0
        # Settings object to holds the application settings. Is a QT wrapper to be OS independent
        self.settings: QSettings = QSettings("UPC", "BLOPUP_WINDOWS_APPLICATION")
        self.current_server_name: str = self.settings.value("server_name", '', str)
        self.current_language: str = self.settings.value("language", '', str)
        # Translator and locale initialization
        self.translator: QTranslator = QTranslator()
        if self.current_language == '':
            dir_path = os.path.dirname(os.path.realpath(__file__))
            _ = self.translator.load(QLocale.system(), 'blopup', prefix='.', directory=dir_path + '/i18n', suffix='.qm')
            QCoreApplication.installTranslator(self.translator)
            QLocale().setDefault(QLocale.system())
            self.current_language = QLocale.system().name()
        else:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            _ = self.translator.load(QLocale(self.current_language), 'blopup', prefix='.', directory=dir_path + '/i18n', suffix='.qm')
            QCoreApplication.installTranslator(self.translator)
            QLocale().setDefault(QLocale(self.current_language))

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.settings.setValue('server_name', self.current_server_name)
        self.settings.setValue('language', self.current_language)

    def showEvent(self, a0: QShowEvent) -> None:
        QMainWindow.showEvent(self, a0)
        if not self.shown:
            self.shown = True
            if platform.system() == 'Windows':  # pragma: no cover
                # necessary for reading the USB blood pressure device
                self.HWND = self.effectiveWinId()
                # self.label_hwnd.setText("{0:08X}".format(int(self.HWND)))
                i = Int32(self.winId().__int__())
                p = IntPtr.op_Explicit(i)
                self.watchBPHomeHid.RegisterHandle(p)
            # Main window
            self.setWindowTitle("BLOPUP")
            # Toolbar
            self.toolbar_action_login = QAction(
                QIcon(':/blopup/login.png'),
                self.tr("Login"),
                parent=self
            )
            self.toolbar_action_login.triggered.connect(self.login)  # noqa - Bug in PyCharm
            self.toolbar_action_login.setEnabled(self.current_server_name != '')
            self.tool_bar_main.addAction(self.toolbar_action_login)
            self.toolbar_action_logout = QAction(
                QIcon(':/blopup/logout.png'),
                self.tr("Logout"),
                parent=self
            )
            self.toolbar_action_logout.triggered.connect(self.logout)  # noqa - Bug in PyCharm
            self.toolbar_action_logout.setEnabled(False)
            self.tool_bar_main.addAction(self.toolbar_action_logout)
            if random.randint(1, 2) == 1:
                self.toolbar_action_search_patient = QAction(
                    QIcon(':/blopup/search_patient_man.png'),
                    self.tr("Search Patient"),
                    parent=self
                )
            else:
                self.toolbar_action_search_patient = QAction(
                    QIcon(':/blopup/search_patient_woman.png'),
                    self.tr("Search Patient"),
                    parent=self
                )
            self.toolbar_action_search_patient.triggered.connect(self.search_patient)  # noqa - Bug in PyCharm
            self.toolbar_action_search_patient.setEnabled(False)
            self.tool_bar_main.addAction(self.toolbar_action_search_patient)
            if random.randint(1, 2) == 1:
                self.toolbar_action_add_patient = QAction(
                    QIcon(':/blopup/add_patient_man.png'),
                    self.tr("Add Patient"),
                    parent=self
                )
            else:
                self.toolbar_action_add_patient = QAction(
                    QIcon(':/blopup/add_patient_woman.png'),
                    self.tr("Add Patient"),
                    parent=self
                )
            self.toolbar_action_add_patient.triggered.connect(self.add_patient)  # noqa - Bug in PyCharm
            self.toolbar_action_add_patient.setEnabled(False)
            self.tool_bar_main.addAction(self.toolbar_action_add_patient)
            if random.randint(1, 2) == 1:
                self.toolbar_action_visit = QAction(
                    QIcon(':/blopup/visit_man.png'),
                    self.tr("Visit Patient"),
                    parent=self
                )
            else:
                self.toolbar_action_visit = QAction(
                    QIcon(':/blopup/visit_woman.png'),
                    self.tr("Visit Patient"),
                    parent=self
                )
            self.toolbar_action_visit.triggered.connect(self.visit)  # noqa - Bug in PyCharm
            self.toolbar_action_visit.setEnabled(False)
            self.tool_bar_main.addAction(self.toolbar_action_visit)
            self.toolbar_action_setup = QAction(
                QIcon(':/blopup/setup.png'),
                self.tr("Setup"),
                parent=self
            )
            self.toolbar_action_setup.triggered.connect(self.setup)  # noqa - Bug in PyCharm
            self.tool_bar_main.addAction(self.toolbar_action_setup)
            self.toolbar_action_about = QAction(
                QIcon(':/blopup/about.png'),
                self.tr("About"),
                parent=self
            )
            self.toolbar_action_about.triggered.connect(self.about)  # noqa - Bug in PyCharm
            self.tool_bar_main.addAction(self.toolbar_action_about)
            # Menu bar
            self.menu_action_login = QAction(self.tr("Login"), parent=self)
            self.menu_action_login.triggered.connect(self.login)  # noqa - Bug in PyCharm
            self.menu_action_login.setEnabled(self.current_server_name != '')
            self.menu_main.addAction(self.menu_action_login)
            self.menu_action_logout = QAction(self.tr("Logout"), parent=self)
            self.menu_action_logout.triggered.connect(self.logout)  # noqa - Bug in PyCharm
            self.menu_action_logout.setEnabled(False)
            self.menu_main.addAction(self.menu_action_logout)
            self.menu_action_search_patient = QAction(self.tr("Search Patient"), parent=self)
            self.menu_action_search_patient.triggered.connect(self.search_patient)  # noqa - Bug in PyCharm
            self.menu_action_search_patient.setEnabled(False)
            self.menu_main.addAction(self.menu_action_search_patient)
            self.menu_action_add_patient = QAction(self.tr("Add Patient"), parent=self)
            self.menu_action_add_patient.triggered.connect(self.add_patient)  # noqa - Bug in PyCharm
            self.menu_action_add_patient.setEnabled(False)
            self.menu_main.addAction(self.menu_action_add_patient)
            self.menu_action_visit = QAction(self.tr("Visit Patient"), parent=self)
            self.menu_action_visit.triggered.connect(self.visit)  # noqa - Bug in PyCharm
            self.menu_action_visit.setEnabled(False)
            self.menu_main.addAction(self.menu_action_visit)
            self.menu_action_setup = QAction(self.tr("Setup"), parent=self)
            self.menu_action_setup.triggered.connect(self.setup)  # noqa - Bug in PyCharm
            self.menu_main.addAction(self.menu_action_setup)
            self.menu_action_about = QAction(self.tr("About"), parent=self)
            self.menu_action_about.triggered.connect(self.about)  # noqa - Bug in PyCharm
            self.menu_main.addAction(self.menu_action_about)
            self.menu_actions['setup'] = self.menu_action_setup
            self.menu_actions['about'] = self.menu_action_about
            self.menu_actions['login'] = self.menu_action_login
            self.menu_actions['logout'] = self.menu_action_logout
            self.menu_actions['search_patient'] = self.menu_action_search_patient
            self.menu_actions['add_patient'] = self.menu_action_add_patient
            self.menu_actions['visit_patient'] = self.menu_action_visit
            self.toolbar_actions['setup'] = self.toolbar_action_setup
            self.toolbar_actions['about'] = self.toolbar_action_about
            self.toolbar_actions['login'] = self.toolbar_action_login
            self.toolbar_actions['logout'] = self.toolbar_action_logout
            self.toolbar_actions['search_patient'] = self.toolbar_action_search_patient
            self.toolbar_actions['add_patient'] = self.toolbar_action_add_patient
            self.toolbar_actions['visit_patient'] = self.toolbar_action_visit
            # StatusBar
            self.label_status_user = QLabel()
            self.label_status_user.setText(self.tr("User:") + " 🔴")
            self.status_main.addPermanentWidget(self.label_status_user)

    def _retranslate_ui(self) -> None:
        """
        When the language in the settings is changed, the different elements of the main UI have to be retranslated

        :return: None
        """
        # Menu
        self.menu_action_login.setText(self.tr('Login'))
        self.menu_action_logout.setText(self.tr('Logout'))
        self.menu_action_search_patient.setText(self.tr('Search Patient'))
        self.menu_action_add_patient.setText(self.tr('Add Patient'))
        self.menu_action_visit.setText(self.tr('Visit Patient'))
        self.menu_action_setup.setText(self.tr('Setup'))
        self.menu_action_about.setText(self.tr('About'))
        # Toolbar
        self.toolbar_action_login.setText(self.tr('Login'))
        self.toolbar_action_logout.setText(self.tr('Logout'))
        self.toolbar_action_search_patient.setText(self.tr('Search Patient'))
        self.toolbar_action_add_patient.setText(self.tr('Add Patient'))
        self.toolbar_action_visit.setText(self.tr('Visit Patient'))
        self.toolbar_action_setup.setText(self.tr('Setup'))
        self.toolbar_action_about.setText(self.tr('About'))
        # Status bar
        status_char = self.label_status_user.text()[-1]
        self.label_status_user.setText(self.tr("User:") + " " + status_char)

    # noinspection PyPep8Naming
    def nativeEvent(self, eventType: Union[QByteArray, bytes, bytearray], message: voidptr) -> Tuple[bool, int]:   # pragma: no cover
        # result = QMainWindow.nativeEvent(self, eventType, message)
        try:
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            i = Int32(msg.hWnd)
            p1 = IntPtr.op_Explicit(i)
            i = Int32(msg.wParam)
            p3 = IntPtr.op_Explicit(i)
            i = Int64(msg.lParam)
            p4 = IntPtr.op_Explicit(i)
            msg2 = Message.Create(p1, msg.message, p3, p4)
            # print("{0:08X}".format(int(msg.hWnd)), msg.message, msg.wParam, msg.lParam, eventType)
            msg_result = self.watchBPHomeHid.ParseMessages(msg2)
            return False, 0  # msg_result.Result
        except:  # noqa
            return False, 0

    def hid_removed(self, sender, e):  # pragma: no cover
        # self.label_status_hid.setText('Disconnected')
        self.status_hid = 2

    def hid_arrived(self, sender, e):  # pragma: no cover
        # self.label_status_hid.setText('Connected')
        self.status_hid = 1

    def on_test_can_communication(self):  # pragma: no cover
        if self.watchBPHomeHid.CanCommunication:
            self.label_test_can_communication.setText('True')
        else:
            self.label_test_can_communication.setText('False')

    def on_read_id(self):  # pragma: no cover
        data = self.watchBPHomeHid.WriteCmd(1)
        out_text = 'No ID defined'
        result, text = WatchBPHome.Decode.DeviceInfoParser.ParseDeviceID(data, out_text)
        self.label_read_id.setText(text)

    def on_read_date_time(self):  # pragma: no cover
        data = self.watchBPHomeHid.WriteCmd(5)
        out_text = ''
        result, text = WatchBPHome.Decode.DeviceInfoParser.ParseDeviceDateTime(data, out_text)
        self.label_read_date_time.setText(text)

    def on_read_version(self):  # pragma: no cover
        data = self.watchBPHomeHid.WriteCmd(2)
        out_text = ''
        result, text = WatchBPHome.Decode.DeviceInfoParser.ParseDeviceName(data, out_text)
        self.label_read_version.setText(text)

    def on_read_usual_data(self):  # pragma: no cover
        data = self.watchBPHomeHid.WriteCmd(3)
        out_usu_data = List[WatchBPHome.Decode.Data](range(10))
        result, data_list = WatchBPHome.Decode.DataParser.ParseUsuData(data, out_usu_data)
        text = "Length: {} - First: ID={}, DateTime={}, Sys={}, Dia={}, bpm={}".format(
            str(len(data_list)), data_list[0].ID, data_list[0].MeasureDateTime, data_list[0].Systole,
            data_list[0].Diastole, data_list[0].Pulse)
        self.label_read_usual_data.setText(text)

    def setup(self) -> None:
        self.dlg = DlgSettings(self)
        dlg: DlgSettings = self.dlg   # Not necessary but useful for type verification
        dlg.server_name = self.current_server_name
        dlg.language = QLocale().name()
        if dlg.exec() == QDialog.Accepted:
            if self.current_server_name != dlg.server_name:
                self.current_user = None
                for (key, action) in self.toolbar_actions.items():
                    if key != 'setup' and key != 'about':
                        action.setEnabled(False)
                    else:
                        action.setEnabled(True)
                for (key, action) in self.menu_actions.items():
                    if key != 'setup' and key != 'about':
                        action.setEnabled(False)
                    else:
                        action.setEnabled(True)
                if dlg.server_name is not None:
                    self.current_server_name = dlg.server_name
                    self.toolbar_action_login.setEnabled(True)
                    self.menu_action_login.setEnabled(True)
                else:
                    self.current_server_name = None
            if dlg.language != QLocale().name():
                QCoreApplication.removeTranslator(self.translator)
                QLocale().setDefault(QLocale(dlg.language))
                print(QLocale().name())
                dir_path = os.path.dirname(os.path.realpath(__file__))
                result = self.translator.load(QLocale(), 'blopup', prefix='.', directory=dir_path+'/i18n', suffix='.qm')
                QCoreApplication.installTranslator(self.translator)
                self._retranslate_ui()
                print(QLocale().name())
                self.current_language = dlg.language
                print(self.current_language)
        self.dlg = None

    def login(self) -> None:
        try:
            self.locations: List[Location] = get_locations(self.current_server_name)
            if self.locations is not None and len(self.locations) > 0:
                location: Location
                self.locations_by_uuid = {location.open_mrs_uuid: location for location in self.locations}
        except Exception as xcpt:  # noqa
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Error")
            self.msg.setInformativeText(self.tr("Can't retrieve Locations from server. Please check your internet "
                                                "connection or the server name in the Settings Dialog"))
            self.msg.setWindowTitle(self.tr("Error"))
            self.msg.exec_()
            self.label_status_user.setText(self.tr("User:") + " 🔴")
            self.msg = None
            self.dlg = None
            print(xcpt)
            return
        self.dlg = DlgLogin(self)
        dlg: DlgLogin = self.dlg  # Not necessary but useful for type verification
        dlg.locations = self.locations
        if dlg.exec() == QDialog.Accepted:
            try:
                _ = login(self.current_server_name, dlg.username, dlg.password)
                self.current_user = User(username=dlg.username, password=dlg.password)
                self.current_location = dlg.location
                self.label_status_user.setText(self.tr("User:") + " 🟢")
                # Get additional information that is needed from OpenMRS
                try:
                    patient_identifier_types: List[PatientIdentifierType] = get_patient_identifier_type_list(self.current_server_name, self.current_user.username, self.current_user.password)
                    patient_identifier_type: PatientIdentifierType
                    patient_identifier_types = [patient_identifier_type for patient_identifier_type in patient_identifier_types if isinstance(patient_identifier_type, PatientIdentifierType)]
                    self.current_patient_identifier_types = {patient_identifier_type.name: patient_identifier_type for patient_identifier_type in patient_identifier_types}
                    visit_types: List[VisitType] = get_visit_type_list(self.current_server_name, self.current_user.username, self.current_user.password)
                    visit_type: VisitType
                    visit_types = [visit_type for visit_type in visit_types if isinstance(visit_type, VisitType)]
                    self.current_visit_types = {visit_type.open_mrs_uuid: visit_type for visit_type in visit_types}
                    self.menu_action_login.setEnabled(False)
                    self.menu_action_logout.setEnabled(True)
                    self.menu_action_search_patient.setEnabled(True)
                    self.menu_action_add_patient.setEnabled(True)
                    self.menu_action_visit.setEnabled(True)
                    self.toolbar_action_login.setEnabled(False)
                    self.toolbar_action_logout.setEnabled(True)
                    self.toolbar_action_search_patient.setEnabled(True)
                    self.toolbar_action_add_patient.setEnabled(True)
                    self.toolbar_action_visit.setEnabled(True)
                except Exception as xcpt:  # noqa
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Warning)
                    self.msg.setText("Warning")
                    self.msg.setInformativeText(
                        "Can't retrieve Identifier types from server. Please check your internet connection or the "
                        "server name in the Settings Dialog")
                    self.msg.setWindowTitle("Warning")
                    self.msg.exec_()
                    self.msg = None
                    self.dlg = None
                    self.label_status_user.setText(self.tr("User:") + " 🔴")
                    print(xcpt)
                    return
            except Exception:  # noqa
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("Error")
                self.msg.setInformativeText('Incorrect Username or Password or server is not reachable')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
                self.msg = None
                self.dlg = None
                self.label_status_user.setText(self.tr("User:") + " 🔴")
                return
        self.dlg = None

    def logout(self) -> None:
        """
        TODO:
        :return:
        """
        self.menu_action_login.setEnabled(True)
        self.menu_action_logout.setEnabled(False)
        self.menu_action_search_patient.setEnabled(False)
        self.menu_action_add_patient.setEnabled(False)
        self.menu_action_visit.setEnabled(False)
        self.toolbar_action_login.setEnabled(True)
        self.toolbar_action_logout.setEnabled(False)
        self.toolbar_action_search_patient.setEnabled(False)
        self.toolbar_action_add_patient.setEnabled(False)
        self.toolbar_action_visit.setEnabled(False)
        self.label_status_user.setText(self.tr("User:") + " 🔴")
        try:
            _ = logout(self.current_server_name, self.current_user.username, self.current_user.password)
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Warning")
            self.msg.setInformativeText("There has been a problem with the server connection or during the logout")
            self.msg.setWindowTitle("Warning")
            self.msg.exec_()
            self.label_status_user.setText(self.tr("User:") + " 🔴")
            print(e)
        self.current_user = None

    def search_patient(self):
        """
        Opens a dialog box to select a patient using a search box. If a patient is selected, the dialog closes and
        a patient dialog with the patient information is opened
        """
        self.dlg = DlgSearchPatient(self, self.current_user, self.current_server_name, self.current_patient_identifier_types)
        dlg: DlgSearchPatient = self.dlg  # Not necessary but useful for type verification
        if dlg.exec() == QDialog.Accepted:
            patient: Patient = dlg.patient
            dlg.close()
            self.edit_patient(patient)

    # def edit_patient(self, patient: Optional[Patient] = None):
    #     if patient is not None:
    #         full_patient = get_patient(self.current_server_name, self.current_user.username, self.current_user.password, patient.open_mrs_uuid)
    #         if full_patient.identifiers is not None and len(full_patient.identifiers) > 0:
    #             for identifier in full_patient.identifiers:
    #                 print(str(identifier))
    #                 print(str(identifier.patient_identifier_type_uuid))
    #                 for key, value in self.current_patient_identifier_types.items():
    #                     print(key, str(value.open_mrs_uuid))
    #                     if value.open_mrs_uuid == identifier.patient_identifier_type_uuid:
    #                         identifier.patient_identifier_type = value
    #         visits = get_visit_list(self.current_server_name, self.current_user.username, self.current_user.password, patient.open_mrs_uuid)
    #         if visits is not None and len(visits) > 0:
    #             for visit in visits:
    #                 if visit.location_uuid in self.locations_by_uuid:
    #                     visit.location = self.locations_by_uuid[visit.location_uuid]
    #                 if visit.visit_type_uuid in self.current_visit_types:
    #                     visit.visit_type = self.current_visit_types[visit.visit_type_uuid]
    #         full_patient.visits = visits
    #
    #     else:
    #         # TODO: Missatge d'error
    #         return
    #     self.dlg = DlgPatient(self, self.current_server_name, self.current_user.username, self.current_user.password, full_patient)
    #     dlg: DlgPatient = self.dlg  # Not necessary but useful for type verification
    #     if dlg.exec() == QDialog.Accepted:
    #         pass

    def add_patient(self):
        self.edit_patient()

    def visit(self):
        pass

    def about(self):
        dlg: DlgAbout = DlgAbout(self)
        dlg.exec()

    def update(self, from_version: Union[str, None] = None, to_version: str = VERSION) -> bool:
        print("Version")
        return False


if __name__ == '__main__':
    app: QApplication = QApplication([])
    main_window: MainWindow = MainWindow()
    main_window.show()
    app.exec()
