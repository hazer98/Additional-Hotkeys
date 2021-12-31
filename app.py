import sys
import threading

from PyQt6.QtCore import QObject, QCoreApplication
from PyQt6.QtWidgets import QApplication

from utils import data_parser
from controllers.main_window_controller import MainWindowController
from listener import Listener
from utils.data_parser import HotkeyData, get_listener_data


class App(QObject):
    def __init__(self):
        super().__init__()

        self.listener: Listener = Listener(get_listener_data())
        self.listener_thread = threading.Thread(target=self.listener.run)
        self.listener_thread.daemon = True

        self.window: MainWindowController = MainWindowController()
        self.window.on_data_updated.connect(self.update)

        self.load_hotkeys()

        self.start_listener_thread()

    def update(self):
        self.listener.update(get_listener_data())

    def load_hotkeys(self):
        hotkeys: list[HotkeyData] = data_parser.get_hotkeys_data()
        for hotkey in hotkeys:
            self.window.add_hotkey(hotkey)

    def start_listener_thread(self):
        self.listener_thread.start()


if __name__ == '__main__':
    app_proc: QApplication = QApplication(sys.argv)

    app: App = App()

    sys.exit(app_proc.exec())
