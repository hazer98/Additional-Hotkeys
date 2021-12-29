from PyQt6.QtWidgets import QHBoxLayout, QKeySequenceEdit, QLineEdit, QWidget, QPushButton


class Hotkey(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.key_sequence_edit = QKeySequenceEdit()
        self.layout.addWidget(self.key_sequence_edit)

        self.path_edit = QLineEdit()
        self.layout.addWidget(self.path_edit)

        self.delete_button = QPushButton('Delete')
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)
