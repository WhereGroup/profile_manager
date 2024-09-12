"""
/***************************************************************************
 ProfileManagerDialog
                                 A QGIS plugin
 Makes creating profiles easy by giving you an UI to easly import settings from other profiles
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-03-17
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Dominik Szill / WhereGroup GmbH
        email                : dominik.szill@wheregroup.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from pathlib import Path
from typing import Optional

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QMessageBox
from .userInterface.mdl_profiles import ProfileListModel
from .qdt_export.profile_export import export_profile_for_qdt, get_qdt_profile_infos_from_file, QDTProfileInfos

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "profile_manager_dialog_base.ui")
)


class ProfileManagerDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super().__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.profile_mdl = ProfileListModel(self)
        self.qdt_export_profile_cbx.setModel(self.profile_mdl)
        self.export_qdt_button.clicked.connect(self.export_qdt_handler)
        self.export_qdt_button.setEnabled(False)
        self.qdt_file_widget.fileChanged.connect(self._qdt_export_dir_changed)

        self.comboBoxNamesSource.setModel(self.profile_mdl)
        self.comboBoxNamesTarget.setModel(self.profile_mdl)
        self.list_profiles.setModel(self.profile_mdl)

    def get_list_selection_profile_name(self) -> Optional[str]:
        """Get selected profile name from list

        Returns:
            Optional[str]: selected profile name, None if no profile selected
        """
        index = self.list_profiles.selectionModel().currentIndex()
        if index.isValid():
            return self.list_profiles.model().data(index, ProfileListModel.NAME_COL)
        return None
    
    def _qdt_export_dir_changed(self) -> None:
        """Update UI when QDT export dir is changed:
        - enabled/disable button
        - define QDTProfileInformations if profile.json file is available
        """
        export_dir = self.qdt_file_widget.filePath()
        if export_dir:
            self.export_qdt_button.setEnabled(True)
            profile_json = Path(export_dir) / "profile.json"
            if profile_json.exists():
                self._set_qdt_profile_infos(get_qdt_profile_infos_from_file(profile_json))
        else:
            self.export_qdt_button.setEnabled(False)


    def _get_qdt_profile_infos(self) -> QDTProfileInfos:
        """Get QDTProfileInfos from UI

        Returns:
            QDTProfileInfos: QDT Profile Information
        """
        return QDTProfileInfos(
                description=self.qdt_description_edit.toPlainText(),
                email=self.qdt_email_edit.text(),
                version=self.qdt_version_edit.text(),
                qgis_min_version=self.qdt_qgis_min_version_edit.text(),
                qgis_max_version=self.qdt_qgis_max_version_edit.text(),
            )   

    def _set_qdt_profile_infos(self, qdt_profile_infos : QDTProfileInfos) -> None:
        """Set QDTProfileInfos in UI

        Args:
            qdt_profile_infos (QDTProfileInfos): QDT Profile Information
        """
        self.qdt_description_edit.setPlainText(qdt_profile_infos.description)
        self.qdt_email_edit.setText(qdt_profile_infos.email)
        self.qdt_version_edit.setText(qdt_profile_infos.version)
        self.qdt_qgis_min_version_edit.setText(qdt_profile_infos.qgis_min_version)
        self.qdt_qgis_max_version_edit.setText(qdt_profile_infos.qgis_max_version)

    def export_qdt_handler(self) -> None:
        """Export selected profile as QDT profile"""
        profile_path = self.qdt_file_widget.filePath()
        if profile_path:
            source_profile_name = self.qdt_export_profile_cbx.currentText()
            export_profile_for_qdt(
                profile_name=source_profile_name,
                export_path=Path(profile_path),
                qdt_profile_infos=self._get_qdt_profile_infos(),
                clear_export_path=self.qdt_clear_export_folder_checkbox.isChecked(),
                export_inactive_plugin=self.qdt_inactive_plugin_export_checkbox.isChecked(),
            )
            QMessageBox.information(
                self,
                self.tr("QDT profile export"),
                self.tr(
                    "QDT profile have been successfully exported."
                ),
            )


