import sys

from PyQt6.QtCore import QObject, QCoreApplication
from PyQt6.QtWidgets import QApplication

import utils
from controllers.main_window_controller import WindowController
from listener import Listener


class App(QObject):
    def __init__(self):
        super().__init__()
        self.app: QCoreApplication = QCoreApplication.instance()
        self.app.aboutToQuit.connect(self.exit_handler)

        self.listener: Listener = Listener(utils.get_json_data())

        self.window_controller: WindowController = WindowController()

        self.load_hotkeys()

    def exit_handler(self):
        self.stop_listener_thread()

    def load_hotkeys(self):
        data: dict[str, str] = utils.get_json_data()
        for sequence, path in data.items():
            self.window_controller.add_hotkey(sequence, path)

    def start_listener_thread(self):
        self.listener.run()

    def stop_listener_thread(self):
        self.listener.cancel()


if __name__ == '__main__':
    app_proc: QApplication = QApplication(sys.argv)

    app: App = App()

    sys.exit(app_proc.exec())
