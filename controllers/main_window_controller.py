from functools import partial

from data_store import HotkeyData
from views.main_window import MainWindow
from widgets.hotkey_widget import HotkeyWidget


class MainWindowController(MainWindow):
    def __init__(self, data_store):
        super().__init__()
        self.show()

        self.data_store = data_store

        self.hotkeys: list[HotkeyWidget] = []

        self.add_hotkey_button.clicked.connect(self.add_hotkey)

    def on_hotkey_update(self, hotkey: HotkeyWidget):
        hotkey.update()
        self.data_store.update_hotkey(hotkey.get_data())

    def add_hotkey(self, hotkey_data: HotkeyData = None):
        data = hotkey_data if hotkey_data else self.data_store.get_new_hotkey_data()
        hotkey = HotkeyWidget(data)

        hotkey.delete_button.clicked.connect(partial(self.delete_hotkey, hotkey))
        hotkey.key_sequence_edit.editingFinished.connect(partial(self.on_hotkey_update, hotkey))
        hotkey.path_edit.editingFinished.connect(partial(self.on_hotkey_update, hotkey))

        self.hotkeys_layout.addWidget(hotkey)

    def delete_hotkey(self, hotkey: HotkeyWidget):
        self.data_store.remove_hotkey(hotkey.get_id())
        self.hotkeys_layout.removeWidget(hotkey)
        hotkey.deleteLater()
