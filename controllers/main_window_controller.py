from functools import partial

from utils import data_parser
from views.hotkey import Hotkey
from views.main_window import MainWindow


class MainWindowController(MainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.hotkeys: list[Hotkey] = []

        self.add_hotkey_button.clicked.connect(self.add_hotkey)

    def on_hotkey_changed(self, hotkey: Hotkey):
        data: dict[str, str] = data_parser.get_json_data()
        data[hotkey.get_key_sequence()] = hotkey.get_path()
        print(data)
        data_parser.save_json_data(data)

    def add_hotkey(self, sequence: str = None, path: str = None):
        hotkey = Hotkey(key_sequence=sequence, path=path)

        hotkey.delete_button.clicked.connect(partial(self.delete_hotkey, hotkey))
        hotkey.key_sequence_edit.editingFinished.connect(partial(self.on_hotkey_changed, hotkey))
        hotkey.path_edit.textChanged.connect(partial(self.on_hotkey_changed, hotkey))

        self.hotkeys_layout.addWidget(hotkey)

    def delete_hotkey(self, hotkey: Hotkey):
        data: dict[str, str] = data_parser.get_json_data()
        data.pop(hotkey.get_key_sequence())
        data_parser.save_json_data(data)
        self.hotkeys_layout.removeWidget(hotkey)
        hotkey.deleteLater()
