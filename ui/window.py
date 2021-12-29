from PyQt6.QtWidgets import QMainWindow

import cvars


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.setFixedHeight(cvars.WINDOW_HEIGHT)
        self.setFixedWidth(cvars.WINDOW_WIDTH)
        self.setObjectName('window')

        self.setupUi()
        self.load_stylesheet()

    def load_stylesheet(self):
        with open('ui/window.qss') as f:
            self.setStyleSheet(f.read())

    def setupUi(self):
        ...
