import customtkinter as ctk
import threading
import time
import itertools
### lib +++ ###
from ai_setup.api import localapi
from ai_setup.api import giminiapi
from main.Framework.function import profile
from main.Framework.function import keyrush
from save import save

chatbox = None

def chatframework(gui, framechat, username, locationprofile):
    global chatbox

    if chatbox is None:
        #====================== Zone GUI =======================#
        chatbox = ctk.CTkScrollableFrame(framechat)
        chatbox.place(relx=0, rely=0.12, relwidth=1, relheight=0.78)

        chatentry = ctk.CTkEntry(framechat, font=("Arial Unicode MS", 16))
        chatentry.place(relx=0, rely=0.92, relwidth=0.8, relheight=0.05)

        keyrush.enable_copy_paste(chatentry)

        send_btn = ctk.CTkButton(framechat, text="🚀 ส่ง", font=("Arial Unicode MS", 16))
        send_btn.place(relx=0.82, rely=0.92, relwidth=0.17, relheight=0.05)

        circle_image = profile.create_circle_image(locationprofile, size=(56, 56))

        profileimage = ctk.CTkLabel(framechat, image=circle_image, text="")
        profileimage.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)

        profilelabel = ctk.CTkLabel(framechat, text="Lintar", font=("Arial Unicode MS", 30), text_color="lightblue")
        profilelabel.place(relx=0.11, rely=0)

        profilelabel1 = ctk.CTkLabel(framechat, text="AI Assistant", font=("Arial Unicode MS", 15))
        profilelabel1.place(relx=0.11, rely=0.05)

        #===================== Command =========================#
        def send_message(event=None): 
            user_msg = chatentry.get()
            if user_msg.strip():
                show_message(f"👤 {username}: {user_msg}", "user")
                chatentry.delete(0, "end")

                loading_label = ctk.CTkLabel(chatbox, text="🤖 Lintar: ⣶", text_color="lightblue",
                                            font=("Arial Unicode MS", 20), anchor="w",
                                            wraplength=700, justify="left")
                loading_label.pack(fill="x", padx=10, pady=2)
                chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

                loading = True 

                def animate_loading():
                    symbols = itertools.cycle(["⣷", "⣾", "⣽", "⣻", "⣟", "⣯"])
                    while loading:
                        current = next(symbols)
                        chatbox.after(0, lambda c=current: loading_label.configure(text=f"🤖 Lintar: {c}"))
                        time.sleep(0.15)

                def background_task():
                    nonlocal loading
                    anim_thread = threading.Thread(target=animate_loading)
                    anim_thread.start()
                    
                    ### API MODE FIX ###
                    if  save.loader["apichoice"] == "1":
                        reply = localapi.chat_with_local(f"{username}:{user_msg}")
                    else:
                        reply = giminiapi.chat_with_gimini(f"{username}:{user_msg}")

                    loading = False
                    anim_thread.join()

                    chatbox.after(0, lambda: loading_label.configure(text=f"🤖 Lintar: {reply}"))
                    chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

                threading.Thread(target=background_task).start()

        def show_message(msg, sender):
            color = "lightgreen" if sender == "user" else "lightblue"
            label = ctk.CTkLabel(chatbox, text=msg, text_color=color, font=("Arial Unicode MS", 20), anchor="w",
                                 wraplength=700, justify="left")
            label.pack(fill="x", padx=10, pady=2)
            chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

        send_btn.configure(command=send_message)
        chatentry.bind("<Return>", send_message)

