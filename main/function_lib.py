import os

class funtionlib:
    def __init__(self):
        pass

    def clear_memory(self):
        fileMEM = "AI_profile/chat_memory.json"
        if os.path.exists(fileMEM):
            os.remove(fileMEM)