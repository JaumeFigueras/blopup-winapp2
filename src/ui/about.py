#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
About dialog for the application.

This module defines the :class:`DlgAbout`, a Qt dialog that displays
information about the application, such as the version number and
attributions for icons used in the UI. The dialog is based on a
Qt Designer ``.ui`` file.
"""

import pathlib

from PyQt5 import uic  # noqa
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QDialog

from typing import Optional
from typing import List

class DlgAbout(QDialog):
    """
    Dialog for displaying application information.

    The *About* dialog provides details about the application,
    including version information, authorship, and icon attributions.
    The dialog is loaded from a ``.ui`` file created with Qt Designer.

    Attributes
    ----------
    lbl_windows_application : QLabel
        Label showing the application title.
    lbl_version : QLabel
        Label displaying the current version of the application.
    lbl_icon_attributions : QLabel
        Label introducing the list of icon attributions.
    lbl_icon_1 : QLabel
        Label with attribution for the first icon (login).
    lbl_icon_2 : QLabel
        Label with attribution for the second icon (logout).
    lbl_icon_3 : QLabel
        Label with attribution for the third icon (search patient).
    lbl_icon_4 : QLabel
        Label with attribution for the fourth icon (add patient).
    lbl_icon_5 : QLabel
        Label with attribution for the fifth icon (add visit).
    lbl_icon_6 : QLabel
        Label with attribution for the sixth icon (settings).
    lbl_icon_7 : QLabel
        Label with attribution for the seventh icon (about).
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

    def __init__(self, parent: Optional[QWidget] = None):
        """
        Initialize the About dialog.

        Parameters
        ----------
        parent : QWidget or None, optional
            The parent widget for the dialog. If ``None``, the dialog
            has no parent.
        """
        super().__init__(parent)
        current_location = pathlib.Path(__file__).parent.resolve()
        uic.loadUi(str(current_location) + '/about.ui', self)

    @property
    def lbl_icons(self) -> List[QLabel]:
        """
        List of all icon attribution labels.

        Returns
        -------
        List[QLabel]
            A list containing the labels for the seven icon attributions
            displayed in the dialog.
        """
        return [
            self.lbl_icon_1,
            self.lbl_icon_2,
            self.lbl_icon_3,
            self.lbl_icon_4,
            self.lbl_icon_5,
            self.lbl_icon_6,
            self.lbl_icon_7,
        ]
