from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QHBoxLayout, QKeySequenceEdit, QLineEdit, QWidget, QPushButton


class Hotkey(QWidget):
    def __init__(self, key_sequence: str = None, path: str = None):
        super().__init__()

        self.layout = QHBoxLayout()

        self.key_sequence_edit = QKeySequenceEdit()
        self.layout.addWidget(self.key_sequence_edit)

        self.path_edit = QLineEdit()
        self.layout.addWidget(self.path_edit)

        self.delete_button = QPushButton('Delete')
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

        if key_sequence:
            self.set_key_sequence(key_sequence)

        if path:
            self.set_path(path)

    def set_key_sequence(self, key_sequence: str):
        self.key_sequence_edit.setKeySequence(QKeySequence.fromString(key_sequence))

    def get_key_sequence(self) -> str:
        return self.key_sequence_edit.keySequence().toString()

    def set_path(self, path: str):
        self.path_edit.setText(path)

    def get_path(self) -> str:
        return self.path_edit.text()
