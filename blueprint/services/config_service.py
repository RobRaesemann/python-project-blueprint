import os
import json

PROJECT_PATH = os.getcwd()
CONFIG_PATH = os.path.join(PROJECT_PATH, 'config')
CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, 'config.json')

def _get_config(key):
    with open(CONFIG_FILE_PATH) as json_data_file:
        data = json.load(json_data_file)
    return data[key]

def get_email_recipients():
    return _get_config("email")["recipients"]

def get_email_to():
    return _get_config("email")["to"]

def get_email_from():
    return _get_config("email")["from"]

def get_email_server():
    return _get_config("email")["server"]

def get_email_port():
    return _get_config("email")["port"]

def get_pi_collective():
    return _get_config("pi")["collective"]