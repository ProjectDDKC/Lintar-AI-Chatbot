import json
import os

loader = {
    ### GUI CONFIG ###
    "username": "User",
    "nameai": "Lintar",
    "title": "Ai Assistant",
    "locationprofile": "AI_profile/profile/Lintar.png",
    ### MAIN CONFIG ###
    "api_url":"http://localhost:5001/v1/chat/completions",
    "gimini_key":"AIzaSyA_CeQsagUef5FvnUfRxFk1PIh2b8q2VLE",
    "gimini_model":"gemini-2.0-flash", 
    "apichoice": "2",
    "autorun_switch": {
        "check": False,
        "cpu": False,
    },
}

def save():
    with open("save/save_file/config.json", "w") as file:
        json.dump(loader, file, indent=4)
def loadsave():
    try:
        with open("save/save_file/config.json", "r") as file:
            global loader
            mainload = json.load(file) ### main load data
            loader.update(mainload)
    except FileNotFoundError:
        return
    
def delete_save():
    filesave = "save/save_file/config.json"
    if os.path.exists(filesave):
       os.remove(filesave)