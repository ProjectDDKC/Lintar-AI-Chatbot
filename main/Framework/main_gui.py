import customtkinter as ctk
import sys
import ctypes
import tkinter as tk
import os
### GUI LIB ###
from main.Framework import gui_lib
from save import save_engine
### Framework LIB ###
from main.Framework import control_panel as cpn
from main.Framework import setting
from main.Framework import chat

class gui:
    def __init__(self):
        self.guilib = gui_lib.gui_lib()
        self.username = save_engine.loader["username"]
        self.locationprofile = save_engine.loader["locationprofile"]
        self.initialized = {"chat": False, "setting": False, "console": False}
        self.allframe = {}

    def setup_window(self):
        self.gui = ctk.CTk()
        self.gui.geometry("950x600")
        self.gui.title("Lintar Chat Helper")
        self.gui.attributes("-alpha", 0.9)
        self.gui.minsize(950, 600)

        if sys.platform == "win32":
            myappid = 'mycompany.lintar.chathelper.1.0'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path_png = "config/Icon/LintarIcon.png"
        icon_path_ico = "config/Icon/LintarIcon.ico"
        icon_image = tk.PhotoImage(file=icon_path_png)
        self.gui.iconphoto(True, icon_image)
        self.gui.iconbitmap(icon_path_ico)

    def setup_frames(self):
        self.framemenu = ctk.CTkFrame(self.gui, height=8640)
        self.framemenu.place(x=0, y=0, relwidth=0.17)
        self.framechat = ctk.CTkFrame(self.gui, fg_color="transparent")
        self.framesetting = ctk.CTkFrame(self.gui, fg_color="transparent")
        self.frameconsole = ctk.CTkFrame(self.gui, fg_color="transparent")
        self.allframe = [self.framechat, self.frameconsole, self.framesetting]

    def setup_menu(self):
        ctk.CTkLabel(self.framemenu, text="Menu", font=("Arial", 18), fg_color="transparent", bg_color="transparent").place(relx=0.36, y=20)
        ctk.CTkButton(self.gui, text="Lintar Chat", command=self.show_chat).place(x=10, y=70, relwidth=0.147)
        ctk.CTkButton(self.gui, text="Clear Memory AI", command=self.clear_memory).place(x=10, y=110, relwidth=0.147)
        ctk.CTkButton(self.gui, text="Console", command=self.show_console).place(x=10, rely=0.85, relwidth=0.147)
        ctk.CTkButton(self.gui, text="Setting", command=self.show_setting).place(x=10, rely=0.92, relwidth=0.147)

    def hide_all_frames(self):
        for frame in self.allframe:
            frame.place_forget()

    def show_chat(self):
        self.hide_all_frames()
        if not self.initialized["chat"]:
            chat.chatframework(self.gui, self.framechat, self.username, self.locationprofile)
            self.initialized["chat"] = True
        self.framechat.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def show_console(self):
        self.hide_all_frames()
        if not self.initialized["console"]:
            cpn.consoleframework(self.gui, self.frameconsole)
            self.initialized["console"] = True
        self.frameconsole.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def show_setting(self, event=None):
        self.hide_all_frames()
        if not self.initialized["setting"]:
            setting.settingframework(self.gui, self.framesetting)
            self.initialized["setting"] = True
        self.framesetting.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def clear_memory(self):
        self.guilib.clear_memory()

    def lintar_gui(self):
        self.setup_window()
        self.setup_frames()
        self.setup_menu()
        self.show_chat()
        self.gui.mainloop()