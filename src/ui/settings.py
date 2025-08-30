#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

from PyQt5 import uic  # noqa: Bug in pycharm
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtCore import QLocale

from typing import Union


class DlgSettings(QDialog):

    # Server settings
    group_box_server: QGroupBox
    label_server_name: QLabel
    line_edit_server_name: QLineEdit
    # Language settings
    group_box_locale: QGroupBox
    label_language_selection: QLabel
    combo_box_language: QComboBox
    # Buttons
    buttonbox: QDialogButtonBox

    def __init__(self, parent: QWidget = None) -> None:
        """
        Class constructor

        :param parent: Widget that this dialog belongs to
        :type parent: QWidget
        """
        super().__init__(parent)
        current_dir = pathlib.Path(__file__).parent.resolve()
        uic.loadUi(str(current_dir) + '/settings.ui', self)
        # Language Settings
        self.combo_box_language.setItemData(0, QLocale.system().name())
        self.combo_box_language.setItemData(1, 'ca_ES')
        self.combo_box_language.setItemData(2, 'en_US')
        self.combo_box_language.setItemData(3, 'es_ES')

    @property
    def language(self) -> str:
        """
        Property getter of the language combo box

        :return: The language code selected in the combo box
        """
        idx: int = self.combo_box_language.currentIndex()
        return self.combo_box_language.itemData(idx)

    @language.setter
    def language(self, value: str) -> None:
        """
        Property setter of the language combo box. If the language code does not exist in the combo box the first
        element is selected (this element correspond to the default language)

        :param value: The ISO language code to be selected in the combo box
        :type value: str
        :return: None
        """
        self.combo_box_language.blockSignals(True)
        index: int = self.combo_box_language.findData(value)
        if index != -1:
            self.combo_box_language.setCurrentIndex(index)
        else:
            self.combo_box_language.setCurrentIndex(0)
        self.combo_box_language.blockSignals(False)

    @property
    def server_name(self) -> Union[str, None]:
        """
        Property getter of the server name line edit

        :return: The server name or None if no name is set.
        :rtype: Union[str, None]
        """
        txt = self.line_edit_server_name.text()
        return None if txt == '' else txt

    @server_name.setter
    def server_name(self, value: str) -> None:
        """
        Property setter for the servername line edit

        :param value: New server name
        :type value: str
        :return: None
        """
        self.line_edit_server_name.blockSignals(True)
        self.line_edit_server_name.setText(value)
        self.line_edit_server_name.blockSignals(False)

