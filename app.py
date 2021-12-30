import sys
from functools import partial

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, QCoreApplication

from listener import Listener
from views.hotkey import Hotkey
from views.window import Window

import utils


class App(QObject):
    def __init__(self, window_thread: Window = None):
        super().__init__()
        self.window = window_thread
        self.app = QCoreApplication.instance()
        self.app.aboutToQuit.connect(self.exit_handler)

        self.listener = Listener({})

        self.window.add_hotkey_button.clicked.connect(self.add_hotkey)

        self.load_hotkeys()

    def exit_handler(self):
        self.listener.cancel()

    def load_hotkeys(self):
        data = utils.get_json_data()
        for sequence, path in data.items():
            self.add_hotkey(sequence, path)

    def add_hotkey(self, sequence=None, path=None):
        hotkey = Hotkey(key_sequence=sequence, path=path)
        hotkey.delete_button.clicked.connect(partial(self.delete_hotkey, hotkey))
        self.window.hotkeys_layout.addWidget(hotkey)

    def delete_hotkey(self, hotkey: Hotkey):
        self.window.hotkeys_layout.removeWidget(hotkey)
        hotkey.deleteLater()

    def start_listener_thread(self):
        self.listener.run()


if __name__ == '__main__':
    app_proc = QApplication(sys.argv)

    window = Window()
    window.show()

    app = App(window_thread=window)

    sys.exit(app_proc.exec())
