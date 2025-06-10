def run_app():
    import customtkinter as ctk
    import tkinter as tk
    import os
    import ctypes
    import sys

    #### ตั้งตำแหน่ง path ไว้ให้ import ได้ทุกโมดูล ####
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

    # === Feature Lib ===
    from save import save
    from main.Root import control_panel as cpn
    from main.Framework import setting
    from ai_setup.api import giminiapi
    from ai_setup.api import localapi
    from main.Framework.function import autorunlocalllm as at
    #=== โหลดเชฟ 
    save.loadsave()
    username = save.loader["username"]
    locationprofile = save.loader["locationprofile"]

    at.autorun()

    if save.loader["apichoice"] == "1":
        localapi.localapi()
    else:
        giminiapi.giminiapi()

    # === Feature Lib โหลดหลัง saveloder กัน saveloader===# 
    from main.Framework import chat

    # === GUI Init ===
    gui = ctk.CTk()
    gui.geometry("950x600")
    gui.title("Lintar Chat Helper")
    gui.attributes("-alpha", 0.9)
    gui.minsize(950, 600)

    if sys.platform == "win32":
        myappid = 'mycompany.lintar.chathelper.1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    icon_path_png = "config/Icon/LintarIcon.png"
    icon_path_ico = "config/Icon/LintarIcon.ico"
    icon_image = tk.PhotoImage(file=icon_path_png)
    gui.iconphoto(True, icon_image)
    gui.iconbitmap(icon_path_ico)

    framemenu = ctk.CTkFrame(gui, height=8640)
    framemenu.place(x=0, y=0, relwidth=0.17)
    framechat = ctk.CTkFrame(gui, fg_color="transparent")
    framesetting = ctk.CTkFrame(gui, fg_color="transparent")
    frameconsole = ctk.CTkFrame(gui, fg_color="transparent")

    allframe = [framechat, frameconsole, framesetting]
    initialized = {"chat": False, "setting": False, "console": False, "feature": False}

    def hide_frame():
        for frame in allframe:
            frame.place_forget()

    def consoleframework():
        hide_frame()
        if not initialized["console"]:
            cpn.consoleframework(gui, frameconsole)
            initialized["console"] = True
        frameconsole.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def settingframework(event=None):
        hide_frame()
        if not initialized["setting"]:
            setting.settingframework(gui, framesetting)
            initialized["setting"] = True
        framesetting.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def chatframework():
        hide_frame()
        if not initialized["chat"]:
            chat.chatframework(gui, framechat, username, locationprofile)
            initialized["chat"] = True
        framechat.place(relx=0.18, rely=0, relwidth=0.815, relheight=1)

    def ClearRAM():
        fileMEM = "ai_setup/chat_memory.json"
        if os.path.exists(fileMEM):
            os.remove(fileMEM)

    ctk.CTkLabel(gui, text="Menu", font=("Arial", 18)).place(relx=0.065, y=20)
    ctk.CTkButton(gui, text="Lintar Chat", command=chatframework).place(x=10, y=70, relwidth=0.147)
    ctk.CTkButton(gui, text="ClearMEM", command=ClearRAM).place(x=10, y=110, relwidth=0.147)
    ctk.CTkButton(gui, text="Console", command=consoleframework).place(x=10, rely=0.85, relwidth=0.147)
    ctk.CTkButton(gui, text="Setting", command=settingframework).place(x=10, rely=0.92, relwidth=0.147)

    gui.mainloop()


# ==========================#
# จะรันเมื่อเรียกตรงจากไฟล์นี้เท่านั้น #
# ==========================#
if __name__ == "__main__":
    run_app()