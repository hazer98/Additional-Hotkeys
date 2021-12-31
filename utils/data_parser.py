import json
import cvars


def get_json_data() -> dict:
    with open(cvars.DATA_PATH) as f:
        data = json.load(f)
    return data


def save_json_data(data: dict):
    with open(cvars.DATA_PATH, 'w') as f:
        json.dump(data, f, indent=4)
