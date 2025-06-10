import json

loader = {
    "username": "User",
    "locationprofile": "config/profile/Lintar.png",
    "api_url":"http://localhost:5001/v1/chat/completions",
    "gimini_key":"",
    "gimini_model":"", 
    "apichoice": "1",
    "cpu_switch": {
        "check": False,
    },
    "autorun_switch": {
        "check": False,
    },
}

def save():
    with open("save/LintarChatHelper/config.json", "w") as file:
        json.dump(loader, file, indent=4)
def loadsave():
    try:
        with open("save/LintarChatHelper/config.json", "r") as file:
            global loader
            mainload = json.load(file) ### main load data
            loader.update(mainload)
    except FileNotFoundError:
        return