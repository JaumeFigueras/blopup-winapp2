#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

from PyQt5 import uic  # noqa
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QDialog

from typing import Union
from typing import List

class DlgAbout(QDialog):
    """
    Class to model the QDialog with the information of the application. Such as: the version number the different
    authorship's, etc.
    """

    lbl_windows_application: QLabel
    lbl_version: QLabel
    lbl_icon_attributions: QLabel
    lbl_icon_1: QLabel
    lbl_icon_2: QLabel
    lbl_icon_3: QLabel
    lbl_icon_4: QLabel
    lbl_icon_5: QLabel
    lbl_icon_6: QLabel
    lbl_icon_7: QLabel

    def __init__(self, parent: Union[QWidget, None] = None):
        """
        Class Constructor

        :param parent: Widget that the dialog will be bound with
        :type parent: QWidget
        """
        super().__init__(parent)
        current_location = pathlib.Path(__file__).parent.resolve()
        uic.loadUi(str(current_location) + '/about.ui', self)

    @property
    def lbl_icons(self) -> List[QLabel]:
        return [
            self.lbl_icon_1,
            self.lbl_icon_2,
            self.lbl_icon_3,
            self.lbl_icon_4,
            self.lbl_icon_5,
            self.lbl_icon_6,
            self.lbl_icon_7,
        ]
