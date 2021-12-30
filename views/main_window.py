from functools import partial

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QVBoxLayout, QKeySequenceEdit, QHBoxLayout, \
    QLineEdit, QSpacerItem, QSizePolicy, QApplication, QMenu, QSystemTrayIcon, QStyle

import cvars
from views.hotkey import Hotkey


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Windows Hotkeys')
        self.resize(cvars.WINDOW_WIDTH, cvars.WINDOW_HEIGHT)
        self.setMaximumHeight(600)
        self.setWindowIcon(QIcon(cvars.ICON_PATH))
        self.setObjectName('window')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.hotkeys_layout = QVBoxLayout()

        self.main_layout.addLayout(self.hotkeys_layout)

        self.add_hotkey_button = QPushButton('Add new hotkey')
        self.add_hotkey_button.setMaximumSize(105, 50)
        self.main_layout.addWidget(self.add_hotkey_button)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer)

        self.setup_tray()

        self.load_stylesheet()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def setup_tray(self):
        icon = QIcon(cvars.ICON_PATH)

        tray = QSystemTrayIcon(self)
        tray.setIcon(icon)
        tray.setToolTip('Windows Hotkeys')
        tray.setVisible(True)
        tray.activated.connect(self.show)

        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(QApplication.instance().quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        tray.setContextMenu(tray_menu)

    def load_stylesheet(self):
        with open('views/window.qss') as f:
            self.setStyleSheet(f.read())
