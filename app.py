import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, QCoreApplication

from listener import Listener
from ui.window import Window

combinations = {
    'ctrl+alt+t': 'wt.exe',
}


class App(QObject):
    def __init__(self, window_thread):
        super().__init__()
        self.window = window_thread
        self.app = QCoreApplication.instance()
        self.app.aboutToQuit.connect(self.exit_handler)

        self.listener = Listener(combinations)

        self.window.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.window.add_hotkey()

    def exit_handler(self):
        self.listener.cancel()

    def start_listener_thread(self):
        self.listener.run()


if __name__ == '__main__':

    app_proc = QApplication(sys.argv)
    window = Window()
    window.show()

    app = App(window)

    sys.exit(app_proc.exec())
