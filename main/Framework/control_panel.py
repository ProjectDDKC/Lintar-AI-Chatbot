import customtkinter as ctk

console = None

def consoleframework(gui, frameconsole):
    global console
    if console is None:
        ctk.CTkLabel(frameconsole, text="Control Panel", font=("Arial", 34)).place(relx=0.4,rely=0.005)

        consolebox = ctk.CTkScrollableFrame(frameconsole)
        consolebox.place(relx=0, rely=0.09, relwidth=1, relheight=0.81)

        ctk.CTkLabel(consolebox, text="System: /help for command", text_color="red", font=("Arial Unicode MS", 20), anchor="w", justify="left").pack(fill="x", padx=10, pady=2)

        consoleentry = ctk.CTkEntry(frameconsole, font=("Arial Unicode MS",16))
        consoleentry.place(relx=0,rely=0.92,relwidth=0.8,relheight=0.05)

        consolesend = ctk.CTkButton(frameconsole, text="🚀 ส่ง", font=("Arial Unicode MS", 16))
        consolesend.place(relx=0.82,rely=0.92,relwidth=0.17,relheight=0.05)

        def control_show(admintext):
            label = ctk.CTkLabel(consolebox, text=admintext, text_color="lightgreen",
                                font=("Arial Unicode MS", 20), anchor="w",
                                wraplength=700, justify="left")
            label.pack(fill="x", padx=10, pady=2)
            consolebox.update_idletasks()
            consolebox._parent_canvas.yview_moveto(1)

        def control_message(event=None):
            admintext = consoleentry.get()
            control_show(admintext)
            consoleentry.delete(0, "end")
        
        consolesend.configure(command=control_message)
        consoleentry.bind("<Return>", control_message)

    