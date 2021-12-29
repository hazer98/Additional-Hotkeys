from PyQt6.QtWidgets import QMainWindow

import cvars


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.setFixedHeight(cvars.WINDOW_HEIGHT)
        self.setFixedWidth(cvars.WINDOW_WIDTH)