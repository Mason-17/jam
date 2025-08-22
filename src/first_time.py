import json
from globals import Globals

def first_time():
    if Globals.first_time:
        settings = {
            "theme": "purple_dark_default",
            "font" : 12,
            "language" : "English"
        }

    file_path = "default_settings.json"
    with open(file_path, 'w') as json_file:
        json.dump(settings, json_file, indent=4)