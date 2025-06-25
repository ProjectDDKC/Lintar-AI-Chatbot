import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import os
import subprocess
import tkinter.filedialog as fd
import tkinter as tk
import pyperclip
### MAIN LIB ###
from main import save_lib
from save import save_engine
from main.Framework.function import crop
from main import function_lib


class gui_lib:
    def __init__(self):
        self.loadsave = save_lib.savelib() 
        self.functionlib = function_lib.funtionlib()

    def save_button(self):
        print("กำลังบันทึกข้อมูล...")
        self.loadsave.save_function()
        messagebox.showinfo("Message Box", "บันทึกข้อมูลเรียบร้อยแล้ว!")

    def delete_button(self):
        result = messagebox.askokcancel("Message Box", "คุณต้องการรีเช็ทค่า config หรือไม่?")
        if result:
            save_engine.delete_save()
            messagebox.showinfo("Message Box", "ทำการล้างค่าเรียบร้อย โปรด Restart ใหม่!")
        else:
            pass

    def restart_button(self):
        result = messagebox.askokcancel("Message Box", "คุณต้องการ Restart หรือไม่?")
        if result:
            subprocess.Popen([r"A-StartChat.bat"], shell=True)
            os._exit(0)
        else:
            pass

    def clear_memory(self):
        result = messagebox.askokcancel("Message Box", "คุณต้องการล้างค่าความทรงจำของ AI หรือไม่?")
        if result:
            self.functionlib.clear_memory()
            messagebox.showinfo("Message Box", "ทำการล้างความทรงจำเรียบร้อย")
        else:
            pass

    def choose_profile(self,size):
        file_path = fd.askopenfilename(
        title="เลือกภาพโปรไฟล์",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

        if not file_path:
            image = self.create_circle_image(save_engine.loader["locationprofile"], size)
            return image

        if file_path:
            cropimage = crop.open_crop_and_save_window(file_path, output_dir="AI_profile/profile/crop_cache")
            save_engine.loader["locationprofile"] = cropimage
            new_image = self.create_circle_image(cropimage, size)
            return new_image
    
    def keyrush(self, widget):
        try:
            real_widget = getattr(widget, "_entry", None) or getattr(widget, "_textbox", None) or widget

            def copy(event):
                try:
                    real_widget.event_generate("<<Copy>>")
                except:
                    pass
                return "break"

            def paste(event):
                try:
                    real_widget.event_generate("<<Paste>>")
                except:
                    pass
                return "break"

            def cut(event):
                try:
                    real_widget.event_generate("<<Cut>>")
                except:
                    pass
                return "break"

            def select_all(event):
                try:
                    if isinstance(real_widget, tk.Text):
                        real_widget.tag_add("sel", "1.0", "end")
                    else:
                        real_widget.select_range(0, 'end')
                        real_widget.icursor('end')
                except:
                    pass
                return "break"

            # Bind key shortcut
            real_widget.bind("<Control-c>", copy, add="+")
            real_widget.bind("<Control-v>", paste, add="+")
            real_widget.bind("<Control-x>", cut, add="+")
            real_widget.bind("<Control-a>", select_all, add="+")
        except:
            pass

    def create_circle_image(self, path, size=(100, 100)):
        img = Image.open(path).convert("RGBA").resize(size)
        
        # สร้างหน้ากากวงกลม
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)

        # วางหน้ากากลงบนรูปภาพ
        result = Image.new("RGBA", size)
        result.paste(img, (0, 0), mask=mask)
        return ImageTk.PhotoImage(result)



