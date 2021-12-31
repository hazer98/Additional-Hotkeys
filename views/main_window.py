from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication, \
    QMenu, QSystemTrayIcon, QHBoxLayout, QLineEdit

import cvars


class MainWindow(QMainWindow):
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

        self.new_hotkey_layout = QHBoxLayout()

        self.add_hotkey_button = QPushButton('New Hotkey')
        self.new_hotkey_layout.addWidget(self.add_hotkey_button)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.new_hotkey_layout.addItem(spacer)

        self.main_layout.addLayout(self.new_hotkey_layout)

        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_layout.addItem(spacer)

        self.setup_tray()

        self.load_stylesheet()

    def mousePressEvent(self, event):
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()

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
        with open('styles/main_window.qss') as f:
            self.setStyleSheet(f.read())
