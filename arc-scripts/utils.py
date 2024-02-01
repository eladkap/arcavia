import json
import os


class Utils:
    @staticmethod
    def write_dicts_to_json(dicts: list, file_path: str):
        with open(file_path, 'w') as fp:
            json.dump(dicts, fp, indent=2)

    def read_json_to_dicts(json_file: str):
        data = {}
        with open(json_file, 'r') as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def create_folders(folders: list):
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
