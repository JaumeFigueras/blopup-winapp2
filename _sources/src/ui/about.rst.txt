About Dialog
============

The *About* dialog displays information about the application, such as
the version number and icon attributions. It is defined in the
:mod:`src.ui.about` module.

This module defines the :class:`DlgAbout`, a Qt dialog that displays
information about the application, such as the version number and
attributions for icons used in the UI. The dialog is based on a
Qt Designer ``.ui`` file.

DlgAbout Class
--------------

.. autoclass:: src.ui.about.DlgAbout
   :members: __init__
   :undoc-members:
   :show-inheritance:
   :exclude-members: lbl_windows_application, lbl_version, lbl_icon_attributions, lbl_icon_1, lbl_icon_2, lbl_icon_3,
                     lbl_icon_4, lbl_icon_5, lbl_icon_6, lbl_icon_7

   .. autoproperty:: src.ui.about.DlgAbout.lbl_icons