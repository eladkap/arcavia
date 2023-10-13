import json


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def write_dicts_to_json(dicts: list, file_path):
        with open(file_path, 'w') as fp:
            json.dump(dicts, fp, indent=2)
