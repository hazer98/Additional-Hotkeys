from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout

import cvars


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.setFixedHeight(cvars.WINDOW_HEIGHT)
        self.setFixedWidth(cvars.WINDOW_WIDTH)
        self.setObjectName('window')

        self.central_widget = QWidget()
        self.central_widget_layout = QGridLayout(self.central_widget)

        self.main_layout = QVBoxLayout()

        self.central_widget_layout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.button = QPushButton('Test')
        self.main_layout.addWidget(self.button)

        self.setCentralWidget(self.central_widget)

        self.load_stylesheet()

    def load_stylesheet(self):
        with open('ui/window.qss') as f:
            self.setStyleSheet(f.read())

