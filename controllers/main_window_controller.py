from functools import partial

from PyQt6.QtCore import pyqtSignal

from utils.data_parser import HotkeyData, remove_hotkey_data, update_hotkey_data, get_new_hotkey_data, add_hotkey_data
from widgets.hotkey_widget import HotkeyWidget
from views.main_window import MainWindow


class MainWindowController(MainWindow):
    on_data_updated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.show()

        self.hotkeys: list[HotkeyWidget] = []

        self.add_hotkey_button.clicked.connect(self.add_hotkey)

    def on_update(self):
        self.on_data_updated.emit()

    def on_hotkey_changed(self, hotkey: HotkeyWidget):
        hotkey.update_data()
        update_hotkey_data(hotkey.get_data())
        self.on_update()

    def add_hotkey(self, hotkey_data: HotkeyData = None):
        data = hotkey_data if hotkey_data else get_new_hotkey_data()
        hotkey = HotkeyWidget(data)
        update_hotkey_data(data)

        hotkey.delete_button.clicked.connect(partial(self.delete_hotkey, hotkey))
        hotkey.key_sequence_edit.editingFinished.connect(partial(self.on_hotkey_changed, hotkey))
        hotkey.path_edit.textChanged.connect(partial(self.on_hotkey_changed, hotkey))

        self.hotkeys_layout.addWidget(hotkey)
        self.on_update()

    def delete_hotkey(self, hotkey: HotkeyWidget):
        remove_hotkey_data(hotkey.get_id())
        self.hotkeys_layout.removeWidget(hotkey)
        hotkey.deleteLater()
        self.on_update()
