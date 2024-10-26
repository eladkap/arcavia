import json
import os
import random


class Utils:
    @staticmethod
    def write_dicts_to_json(dicts: list, file_path: str):
        with open(file_path, 'w') as fp:
            json.dump(dicts, fp, indent=2)

    @staticmethod
    def read_json_to_dicts(json_file: str):
        data = {}
        with open(json_file, 'r') as fp:
            data = json.load(fp)
        return data

    @staticmethod
    def create_folders(folders: list):
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

    @staticmethod
    def shuffle(arr: list):
        for i in range(len(arr)):
            j = random.randint(0, len(arr) - 1)
            arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def get_cuntry_acronym(country_name: str):
        parts = country_name.split()
        if len(parts) == 1:
            return country_name[:3].upper()
        return ''.join([part[0].upper() for part in parts])
