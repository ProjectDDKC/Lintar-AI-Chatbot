import customtkinter as ctk
#### MAIN LIB AND GUI LIB ####
from main.Framework.function import profilesetting
from main.Framework.function import apisetting as apis
from main.Framework import gui_lib
from main import save_lib
from save import save_engine

settingbox = None
### สร้าง instant จาก Lib ###
guilib = gui_lib.gui_lib()
savelib = save_lib.savelib()

def settingframework(gui, framesetting):
    global settingbox
    if settingbox is None:
        settingbox = ctk.CTkScrollableFrame(framesetting)
        settingbox.place(relx=0, rely=0.09, relwidth=1, relheight=0.9)
        ctk.CTkLabel(framesetting, text="Setting", font=("Arial", 34)).place(relx=0.35,rely=0.005)
        #==================== Command Zone ===============================#
        def save():
            username = usersetting.get()
            save_engine.loader["username"] = username
            guilib.save_button()

        def delete():
            guilib.delete_button()

        def restart():
            guilib.restart_button()

        ##################### ZONE SETTING TOOL ###########################
        savebn = ctk.CTkButton(framesetting, text="Save", font=("Arial Unicode MS", 20),command=save, fg_color="Green")
        savebn.place(relx=0.88, rely=0.02, relwidth=0.1, relheight=0.05)

        restartbn = ctk.CTkButton(framesetting, text="Restart", font=("Arial Unicode MS", 20),command=restart, fg_color="Blue")
        restartbn.place(relx=0.76, rely=0.02, relwidth=0.1, relheight=0.05)

        resetbn = ctk.CTkButton(framesetting, text="Reset", font=("Arial Unicode MS", 20),command=delete, fg_color="Red")
        resetbn.place(relx=0.64, rely=0.02, relwidth=0.1, relheight=0.05)

        usersetting = ctk.CTkEntry(settingbox, placeholder_text="ใส่ชื่อผู้ใช้", width=300, height=35)
        usersetting.grid(row=0, column=0, padx=20, pady=10, sticky="w")  # ใช้ grid แทน place
        userlabel = ctk.CTkLabel(settingbox, text="เปลี่ยนหรือแก้ไขชื่อผู้ใช้", font=("Arial Unicode MS", 20))
        userlabel.grid(row=0, column=1, padx=0, pady=10, sticky="w")

        profile = ctk.CTkButton(settingbox, text="Open", font=("Arial Unicode MS", 20),command=lambda: profilesetting.profilesetting(gui), fg_color="Green")
        profile.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        profilelabel = ctk.CTkLabel(settingbox, text="เปลี่ยนโปรไฟล์ให้กับ AI", font=("Arial Unicode MS", 20))
        profilelabel.grid(row=1, column=1, padx=0, pady=10, sticky="w")

        apisetting = ctk.CTkButton(settingbox, text="Open", font=("Arial Unicode MS", 20),command=lambda: apis.apisetting(gui), fg_color="Green")
        apisetting.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        apisettinglabel = ctk.CTkLabel(settingbox, text="ตั้งค่า API Model", font=("Arial Unicode MS", 20))
        apisettinglabel.grid(row=2, column=1, padx=0, pady=10, sticky="w")

        #=========== key function load from save ================#   
        usersetting.insert(0, save_engine.loader["username"])


