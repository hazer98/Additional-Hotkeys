from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication, \
    QMenu, QSystemTrayIcon, QHBoxLayout, QLineEdit, QLabel

import cvars
from utils.utils import resource_path
from views.section_container import SectionContainer
from views.section_item import SectionItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(cvars.WINDOW_TITLE + ' ' + cvars.VERSION)
        self.resize(cvars.WINDOW_WIDTH, cvars.WINDOW_HEIGHT)
        self.setMaximumHeight(600)

        self.setWindowIcon(QIcon(resource_path(cvars.ICON_PATH)))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.section_container = SectionContainer('Hotkeys')
        self.main_layout.addWidget(self.section_container)

        self.new_hotkey_layout = QHBoxLayout()
        self.add_hotkey_button = QPushButton('New Hotkey')
        self.new_hotkey_layout.addWidget(self.add_hotkey_button)
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.new_hotkey_layout.addItem(spacer)

        self.main_layout.addLayout(self.new_hotkey_layout)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer)

        self.setup_tray()

    def mousePressEvent(self, event):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def setup_tray(self):
        tray = QSystemTrayIcon(self)
        tray.setIcon(QIcon(resource_path(cvars.ICON_PATH)))
        tray.setToolTip('Additional Hotkeys')
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
