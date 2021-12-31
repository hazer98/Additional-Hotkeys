from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QHBoxLayout, QKeySequenceEdit, QLineEdit, QWidget, QPushButton

from utils.data_parser import HotkeyData


class HotkeyWidget(QWidget):
    def __init__(self, data: HotkeyData):
        super().__init__()

        self.data = data

        self.layout = QHBoxLayout()

        self.key_sequence_edit = QKeySequenceEdit()
        self.layout.addWidget(self.key_sequence_edit)

        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText('Executable path')
        self.layout.addWidget(self.path_edit)

        self.delete_button = QPushButton('Delete')
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

        self.set_key_sequence(data['key_sequence'])
        self.set_path(data['path'])

    def update_data(self):
        data: HotkeyData = {
            "id": self.get_id(),
            "key_sequence": self.get_key_sequence(),
            "path": self.get_path()
        }
        self.set_data(data)

    def get_data(self) -> HotkeyData:
        return self.data

    def set_data(self, data: HotkeyData):
        self.data = data

    def get_id(self) -> int:
        return self.data['id']

    def set_key_sequence(self, key_sequence: str):
        self.key_sequence_edit.setKeySequence(QKeySequence.fromString(key_sequence))

    def get_key_sequence(self) -> str:
        return self.key_sequence_edit.keySequence().toString()

    def set_path(self, path: str):
        self.path_edit.setText(path)

    def get_path(self) -> str:
        return self.path_edit.text()
