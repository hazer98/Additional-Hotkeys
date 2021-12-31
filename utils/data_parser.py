import json
from typing import TypedDict
import os

import cvars


class HotkeyData(TypedDict):
    id: int
    key_sequence: str
    path: str


class Data(TypedDict):
    hotkeys: list[HotkeyData]


default_data: Data = {
    "hotkeys": []
}


def setup_data():
    if not os.path.exists(cvars.DATA_PATH):
        with open(cvars.DATA_PATH, 'w') as f:
            json.dump(default_data, f, indent=4)


setup_data()


def get_json_data() -> Data:
    with open(cvars.DATA_PATH) as f:
        data = json.load(f)

    return data


def save_json_data(data: Data):
    with open(cvars.DATA_PATH, 'w') as f:
        json.dump(data, f, indent=4)


def get_hotkeys_data() -> list[HotkeyData]:
    data = get_json_data()
    return data['hotkeys']


def save_hotkeys_data(hotkeys_data: list[HotkeyData]):
    data = get_json_data()
    data['hotkeys'] = hotkeys_data
    save_json_data(data)


def update_hotkey_data(hotkey_data: HotkeyData):
    hotkeys_data = get_hotkeys_data()
    for i, hotkey in enumerate(hotkeys_data):
        if hotkey['id'] == hotkey_data['id']:
            hotkeys_data[i] = hotkey_data
            save_hotkeys_data(hotkeys_data)
            return
    add_hotkey_data(hotkey_data)


def add_hotkey_data(hotkey_data: HotkeyData):
    hotkeys_data = get_hotkeys_data()
    hotkeys_data.append(hotkey_data)
    save_hotkeys_data(hotkeys_data)


def remove_hotkey_data(hotkey_id: int):
    hotkeys_data = get_hotkeys_data()
    for hotkey in hotkeys_data:
        if hotkey['id'] == hotkey_id:
            hotkeys_data.remove(hotkey)
    save_hotkeys_data(hotkeys_data)


def get_new_hotkey_data() -> HotkeyData:
    hotkeys_data = get_hotkeys_data()
    hotkey_id = 0

    if len(hotkeys_data) != 0:
        hotkey_id = hotkeys_data[-1]['id'] + 1

    return {
        "id": hotkey_id,
        "key_sequence": "",
        "path": ""
    }
