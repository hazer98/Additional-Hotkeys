from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout, QKeySequenceEdit, QHBoxLayout, \
    QLineEdit, QSpacerItem, QSizePolicy

import cvars
from ui.hotkey import Hotkey


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.resize(cvars.WINDOW_WIDTH, cvars.WINDOW_HEIGHT)
        self.setMaximumHeight(600)
        self.setObjectName('window')

        self.central_widget = QWidget()

        self.main_layout = QVBoxLayout(self.central_widget)

        self.hotkeys_layout = QVBoxLayout()

        self.main_layout.addLayout(self.hotkeys_layout)

        self.button = QPushButton('Add new')
        self.button.setMaximumSize(100, 50)
        self.main_layout.addWidget(self.button)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer)

        self.setCentralWidget(self.central_widget)

        self.load_stylesheet()

    def add_hotkey(self) -> Hotkey:
        hotkey = Hotkey()
        self.hotkeys_layout.insertWidget(0, hotkey)
        return hotkey

    def load_stylesheet(self):
        with open('ui/window.qss') as f:
            self.setStyleSheet(f.read())

