from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout, QKeySequenceEdit, QHBoxLayout, \
    QLineEdit

import cvars
from ui.hotkey import Hotkey


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.resize(cvars.WINDOW_WIDTH, cvars.WINDOW_HEIGHT)
        self.setObjectName('window')

        self.central_widget = QWidget()
        self.central_widget_layout = QGridLayout(self.central_widget)

        self.main_layout = QVBoxLayout()

        self.central_widget_layout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.button = QPushButton('Test')
        self.main_layout.addWidget(self.button)

        self.setCentralWidget(self.central_widget)

        self.load_stylesheet()

    def add_hotkey(self):
        hotkey = Hotkey()
        self.main_layout.addWidget(hotkey)

    def load_stylesheet(self):
        with open('ui/window.qss') as f:
            self.setStyleSheet(f.read())

