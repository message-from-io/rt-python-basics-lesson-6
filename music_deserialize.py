
import json, pickle

def read_json_file():
    with open('group.json', 'r', encoding='utf-8') as f:
        json_file_data = json.load(f)
        return json_file_data

def read_pickle_file():
    with open('group.pickle', 'rb') as f:
        pickle_file_data = pickle.load(f)
        return pickle_file_data
