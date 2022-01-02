import json
import os
from typing import TypedDict

import cvars
from listener import ListenerData


class HotkeyData(TypedDict):
    id: int
    key_sequence: str
    path: str


class Data(TypedDict):
    hotkeys: list[HotkeyData]


initial_state = {
    "hotkeys": []
}


class DataStore:
    def __init__(self):
        self.__data: Data = initial_state

        self.__setup()

    def __setup(self):
        if not os.path.exists(cvars.DATA_PATH):
            with open(cvars.DATA_PATH, 'w') as f:
                json.dump(self.__data, f, indent=4)

        # if data file already exists, load the data instead
        else:
            self.__load()

    def __save(self):
        with open(cvars.DATA_PATH, 'w') as f:
            json.dump(self.__data, f, indent=4)

    def __load(self):
        with open(cvars.DATA_PATH) as f:
            self.__data = json.load(f)

    def get_hotkeys(self) -> list[HotkeyData]:
        return self.__data['hotkeys']

    def save_hotkeys(self, hotkeys: list[HotkeyData]):
        self.__data['hotkeys'] = hotkeys
        self.__save()

    def update_hotkey(self, hotkey_data: HotkeyData):
        hotkeys = self.get_hotkeys()
        for i, hotkey in enumerate(hotkeys):
            if hotkey['id'] == hotkey_data['id']:
                hotkeys[i] = hotkey_data
                self.save_hotkeys(hotkeys)
                return

        # if hotkey does not exist yet, add it to the list
        hotkeys.append(hotkey_data)
        self.save_hotkeys(hotkeys)

    def remove_hotkey(self, hotkey_id: int):
        hotkeys = self.get_hotkeys()
        for hotkey in hotkeys:
            if hotkey['id'] == hotkey_id:
                hotkeys.remove(hotkey)
        self.save_hotkeys(hotkeys)

    def get_new_hotkey_data(self) -> HotkeyData:
        # Determines new id of a hotkey and returns initial hotkey state

        hotkeys = self.get_hotkeys()
        hotkey_id = 0

        if len(hotkeys) != 0:
            hotkey_id = hotkeys[-1]['id'] + 1

        return {
            "id": hotkey_id,
            "key_sequence": "",
            "path": ""
        }

    def get_listener_data(self) -> list[ListenerData]:
        hotkeys = self.get_hotkeys()
        listener_data = []

        for hotkey in hotkeys:
            listener_data.append({
                "key_sequence": hotkey["key_sequence"],
                "path": hotkey["path"]
            })

        return listener_data
