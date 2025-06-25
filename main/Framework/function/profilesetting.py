import customtkinter as ctk
from save import save_engine as save

### MAINLIB AND GUILIB ###
from main.Framework import gui_lib
from save import save_engine

profilegui = None

### สร้าง instant lib ###
guilib = gui_lib.gui_lib()

def profilesetting(gui):
    global profilegui
    if profilegui is None or not profilegui.winfo_exists():
        profilegui = ctk.CTkToplevel(gui)
        profilegui.title("Profile Setting")
        profilegui.geometry("450x450")
        profilegui.attributes("-alpha", 0.9)
        profilegui.resizable(False, False)

        def force_focus():
            profilegui.lift()
            profilegui.attributes('-topmost', True)
            profilegui.focus_force()
            profilegui.after(200, lambda: profilegui.attributes('-topmost', False))

        profilegui.after(100, force_focus)

        profilegui.update_idletasks()
        w = 450
        h = 450
        x = (profilegui.winfo_screenwidth() // 2) - (w // 2)
        y = (profilegui.winfo_screenheight() // 2) - (h // 2)
        profilegui.geometry(f"{w}x{h}+{x}+{y}")

        frameprofile = ctk.CTkFrame(profilegui, fg_color="transparent")
        frameprofile.place(relx=0, rely=0, relwidth=1, relheight=1)

        profilebox = ctk.CTkScrollableFrame(frameprofile)
        profilebox.place(relx=0, rely=0, relwidth=1, relheight=1)

        #============= สร้างคำสั่ง ===============#
        def choose_profile():
            newimage = guilib.choose_profile(size=(96, 96))
            profileimage.configure(image=newimage)
            profileimage.image = newimage
            profilegui.after(10, lambda: profilegui.focus_force())

        def save_profile():
            save_engine.loader["nameai"] = nameL1entry.get()
            save_engine.loader["title"] = nameL2entry.get()
            profilelabel.configure(text= save_engine.loader["nameai"])
            profilelabel1.configure(text= save_engine.loader["title"])



        #============= สร้าง Widget ==============#
        circle_image = guilib.create_circle_image(save_engine.loader["locationprofile"], size=(96, 96))

        profileimage = ctk.CTkButton(
            profilebox,
            image=circle_image,
            text="",
            width=96,
            height=96,
            fg_color="transparent",
            hover_color="#d0d0d0",
            command=choose_profile
        )
        profileimage.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        profilelabel = ctk.CTkLabel(profilebox, text=save_engine.loader["nameai"], font=("Arial Unicode MS", 35), text_color="lightblue")
        profilelabel.grid(row=0, column=0, padx=140, pady=20, sticky="wn")

        profilelabel1 = ctk.CTkLabel(profilebox, text=save_engine.loader["title"], font=("Arial Unicode MS", 17))
        profilelabel1.grid(row=0, column=0, padx=140, pady=50, sticky="ws")

        nameL1entry = ctk.CTkEntry(profilebox, placeholder_text="ชื่อ", width=300, height=35)
        nameL2entry = ctk.CTkEntry(profilebox, placeholder_text="status", width=300, height=35)
        nameL1entry.grid(row=1, column=0, padx=30, pady=5, sticky="ws")
        nameL2entry.grid(row=2, column=0, padx=30, pady=5, sticky="ws")
        savebutton = ctk.CTkButton(profilebox, text="Update", font=("Arial Unicode MS", 20), fg_color="Purple", width=50, height=35, command=save_profile)
        savebutton.grid(row=1, column=0, padx=340, pady=0, sticky="e")

        nameL1entry.insert(0, save_engine.loader["nameai"])
        nameL2entry.insert(0, save_engine.loader["title"])



