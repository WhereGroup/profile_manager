from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox, QLineEdit, QVBoxLayout


class NameProfileDialog(QDialog):
    """A dialog to define a profile name."""

    def __init__(self, title=None, *args, **kwargs):
        """Sets up dialog with input field

        Args:
            title (str): Title of the dialog, defaults to profile *creation*
        """
        super().__init__(*args, **kwargs)

        if title is None:
            self.setWindowTitle(self.tr("Create Profile!"))
        else:
            self.setWindowTitle(title)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Name")
        self.button_box = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_input, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button_box, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

        self.text_input.textChanged.connect(self.adjust_ok_button_state)

        self.adjust_ok_button_state()

    def adjust_ok_button_state(self):
        """Disable OK button if no profile name has been entered (yet)"""
        ok_button = self.button_box.button(QDialogButtonBox.Ok)
        if self.text_input.text() == "":
            ok_button.setEnabled(False)
        else:
            ok_button.setEnabled(True)