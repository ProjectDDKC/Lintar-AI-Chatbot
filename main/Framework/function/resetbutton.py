import os

def ClearRAM():
    fileMEM = "ai_setup/chat_memory.json"
    if os.path.exists(fileMEM):
       os.remove(fileMEM)