import json
import os

def get_json_var(file_id : int, key : str):
    file_path = "./data/" + str(file_id) + ".json"

    # IF FILE DOES NOT EXIST
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({}, file)

    file = open( file_path, "r")
    data : dict = json.load(file)

    return data.get(key, None)

def set_json_var(file_id : int, key : str, value):
    file_path = "./data/" + str(file_id) + ".json"

    # IF FILE DOES NOT EXIST
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({}, file)

    file = open(file_path, "r")
    data: dict = json.load(file)
    data[str(key)] = value
    file = open(file_path, "w")
    json.dump(data, file, indent=4)

