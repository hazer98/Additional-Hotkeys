import sys
import threading

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication

from controllers.main_window_controller import MainWindowController
from data_store import DataStore
from listener import Listener
from utils.utils import resource_path


class App(QObject):
    def __init__(self):
        super().__init__()

        self.data_store = DataStore()

        self.listener: Listener = Listener(self.data_store)
        self.listener_thread = threading.Thread(target=self.listener.run)
        self.listener_thread.daemon = True

        self.window: MainWindowController = MainWindowController(self.data_store)

        self.start_listener_thread()

    def start_listener_thread(self):
        self.listener_thread.start()


if __name__ == '__main__':
    app_proc: QApplication = QApplication(sys.argv)

    with open(resource_path('styles/style.qss')) as f:
        app_proc.setStyleSheet(f.read())

    app: App = App()

    sys.exit(app_proc.exec())
