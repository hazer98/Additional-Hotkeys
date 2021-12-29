import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject

from listener import Listener
from ui.window import Window

combinations = {
    'ctrl+alt+t': 'wt.exe',
}


class App(QObject):
    def __init__(self, window_thread):
        super().__init__()
        self.window = window_thread

    def start(self):
        ...


if __name__ == '__main__':
    # listener = Listener(combinations)
    # listener.run()
    app_proc = QApplication(sys.argv)
    window = Window()
    window.show()

    app = App(window)

    sys.exit(app_proc.exec())
