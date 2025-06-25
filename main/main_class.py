import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from main import llm_lib
from main import save_lib
from main.Framework import main_gui
from main.Framework import gui_lib

class Lintar_Chat_Helper_Lib:
    def __init__(self):
        #=========== สร้าง instant ===========#
        llmlib = llm_lib.llmlib()
        #============ โชนใช้งาน ===========#
        llmlib.autorun() # เปิด llm อัตโนมัติ

    def start(self):
        #=========== แสดงข้อความว่าใช้งานได้ ============#
        print("Ready (Pass)")

def start():
    ### RUN LINTAR_CHAT_HELPER (First Run State) ###
    app_lib = Lintar_Chat_Helper_Lib()
    app_lib.start()
    ### RUN GUI (STATE 2)###
    savelib = save_lib.savelib()
    savelib.loadsave_function()
    gui = main_gui.gui()
    gui.lintar_gui()
