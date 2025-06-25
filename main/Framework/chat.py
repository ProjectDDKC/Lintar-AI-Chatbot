import customtkinter as ctk
import tkinter as tk
import threading

# GUI LIB และ MAIN LIB
from main import llm_lib
from main.Framework import gui_lib
from save import save_engine

chatbox = None  # เปิดครั้งเดียว

llmlib = llm_lib.llmlib()
guilib = gui_lib.gui_lib()

# global สำหรับ animation
loading = False
animation_after_id = None

def chatframework(gui, framechat, username, locationprofile):
    global chatbox, loading, animation_after_id, chatentry

    if chatbox is None:
        chatbox = ctk.CTkScrollableFrame(framechat)
        chatbox.place(relx=0, rely=0.12, relwidth=1, relheight=0.78)

        chatentry = ctk.CTkEntry(framechat, font=("Arial Unicode MS", 16))
        chatentry.place(relx=0, rely=0.92, relwidth=0.8, relheight=0.05)
        chatentry.focus_set()

        send_btn = ctk.CTkButton(framechat, text="🚀 ส่ง", font=("Arial Unicode MS", 16))
        send_btn.place(relx=0.82, rely=0.92, relwidth=0.17, relheight=0.05)

        circle_image = guilib.create_circle_image(locationprofile, size=(56, 56))
        profileimage = ctk.CTkLabel(framechat, image=circle_image, text="")
        profileimage.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)

        profilelabel = ctk.CTkLabel(framechat, text=save_engine.loader["nameai"], font=("Arial Unicode MS", 30), text_color="lightblue")
        profilelabel.place(relx=0.11, rely=0)

        profilelabel1 = ctk.CTkLabel(framechat, text=save_engine.loader["title"], font=("Arial Unicode MS", 15))
        profilelabel1.place(relx=0.11, rely=0.05)

        hi_lintartext = ctk.CTkLabel(chatbox, text=f"🤖 {save_engine.loader['nameai']}: สวัสดี {save_engine.loader['username']}!!!",
                                     text_color="lightblue", font=("Arial Unicode MS", 20), anchor="w",
                                     wraplength=700, justify="left")
        hi_lintartext.pack(fill="x", padx=10, pady=2)

        guilib.keyrush(chatentry)

        def animate_loading(label, symbols, index=0):
            global animation_after_id, loading
            if not loading or not label.winfo_exists():
                return
            label.configure(text=f"🤖 {save_engine.loader['nameai']}: {symbols[index]}")
            next_index = (index + 1) % len(symbols)
            animation_after_id = label.after(150, lambda: animate_loading(label, symbols, next_index))

        def show_message(msg, sender):
            color = "lightgreen" if sender == "user" else "lightblue"
            label = ctk.CTkLabel(chatbox, text=msg, text_color=color, font=("Arial Unicode MS", 20), anchor="w",
                                 wraplength=700, justify="left")
            label.pack(fill="x", padx=10, pady=2)
            chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

        def send_message(event=None):
            global loading, animation_after_id
            user_msg = chatentry.get()
            if user_msg.strip():
                show_message(f"👤 {username}: {user_msg}", "user")
                chatentry.delete(0, "end")
                chatentry.focus_set()

                loading_label = ctk.CTkLabel(chatbox, text=f"🤖 {save_engine.loader['nameai']}: ⠶", text_color="lightblue",
                                             font=("Arial Unicode MS", 20), anchor="w",
                                             wraplength=700, justify="left")
                loading_label.pack(fill="x", padx=10, pady=2)
                chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

                symbols = ["⣷", "⣾", "⣽", "⣻", "⣟", "⣯"]
                loading = True
                animate_loading(loading_label, symbols)

                def background_task():
                    global loading, animation_after_id
                    reply = llmlib.response(f"{username}:{user_msg}")

                    def show_reply():
                        global loading, animation_after_id
                        loading = False
                        if animation_after_id:
                            try:
                                loading_label.after_cancel(animation_after_id)
                            except Exception:
                                pass
                        if loading_label.winfo_exists():
                            loading_label.destroy()

                        # 👇 เพิ่ม reply frame พร้อมปุ่มคัดลอก
                        reply_text = reply
                        reply_frame = ctk.CTkFrame(chatbox, fg_color="transparent")
                        reply_frame.pack(fill="x", padx=10, pady=2)

                        reply_label = ctk.CTkLabel(reply_frame, text=f"🤖 {save_engine.loader['nameai']}: {reply_text}",
                                                   text_color="lightblue", font=("Arial Unicode MS", 20),
                                                   anchor="w", wraplength=660, justify="left")
                        reply_label.pack(side="left", fill="x", expand=True)

                        def copy_reply():
                            root = chatentry.winfo_toplevel()
                            root.clipboard_clear()
                            root.clipboard_append(reply_text)
                            root.update()

                        copy_btn = ctk.CTkButton(reply_frame, text="📋", width=32, height=28, fg_color="#444",
                                                 text_color="white", font=("Arial Unicode MS", 14), command=copy_reply)
                        copy_btn.pack(side="right", padx=(5, 0))

                        chatentry.focus_set()

                    chatbox.after(0, show_reply)
                    chatbox.after(10, lambda: chatbox._parent_canvas.yview_moveto(1.0))

                threading.Thread(target=background_task, daemon=True).start()

        send_btn.configure(command=send_message)
        chatentry.bind("<Return>", send_message)







