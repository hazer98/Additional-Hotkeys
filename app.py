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
        self.app: QCoreApplication = QCoreApplication.instance()
        self.app.aboutToQuit.connect(self.exit_handler)

        self.listener: Listener = Listener(get_listener_data())
        self.listener_thread = threading.Thread(target=self.listener.run)
        self.listener_thread.daemon = True

        self.main_window: MainWindowController = MainWindowController()

        self.load_hotkeys()

        self.start_listener_thread()

    def exit_handler(self):
        self.stop_listener_thread()

    def load_hotkeys(self):
        hotkeys: list[HotkeyData] = data_parser.get_hotkeys_data()
        for hotkey in hotkeys:
            self.main_window.add_hotkey(hotkey)

    def start_listener_thread(self):
        self.listener_thread.start()

    def stop_listener_thread(self):
        self.listener_thread.join()


if __name__ == '__main__':
    app_proc: QApplication = QApplication(sys.argv)

    app: App = App()

    sys.exit(app_proc.exec())
