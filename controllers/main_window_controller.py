from functools import partial

from views.hotkey import Hotkey
from views.main_window import MainWindow


class WindowController:
    def __init__(self):
        self.window = MainWindow()
        self.window.show()

        self.hotkeys: list[Hotkey] = []

        self.window.add_hotkey_button.clicked.connect(self.add_hotkey)

    def add_hotkey(self, sequence=None, path=None):
        hotkey = Hotkey(key_sequence=sequence, path=path)
        hotkey.delete_button.clicked.connect(partial(self.delete_hotkey, hotkey))
        self.window.hotkeys_layout.addWidget(hotkey)

    def delete_hotkey(self, hotkey: Hotkey):
        self.window.hotkeys_layout.removeWidget(hotkey)
        hotkey.deleteLater()
