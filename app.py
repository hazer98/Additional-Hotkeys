import sys
import threading

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication

from controllers.main_window_controller import MainWindowController
from data_store import DataStore
from listener import Listener


class App(QObject):
    def __init__(self):
        super().__init__()

        self.data_store = DataStore()

        self.listener: Listener = Listener(self.data_store)
        self.listener_thread = threading.Thread(target=self.listener.run)
        self.listener_thread.daemon = True

        self.window: MainWindowController = MainWindowController(self.data_store)

        self.load_hotkeys()

        self.start_listener_thread()

    def load_hotkeys(self):
        hotkeys = self.data_store.get_hotkeys()
        for hotkey in hotkeys:
            self.window.add_hotkey(hotkey)

    def start_listener_thread(self):
        self.listener_thread.start()


if __name__ == '__main__':
    app_proc: QApplication = QApplication(sys.argv)

    app: App = App()

    sys.exit(app_proc.exec())
