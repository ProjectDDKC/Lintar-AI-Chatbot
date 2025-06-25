import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import time

def open_crop_and_save_window(image_path: str, output_dir: str = "profile_crop") -> str | None:
    os.makedirs(output_dir, exist_ok=True)

    original_img = Image.open(image_path)
    orig_width, orig_height = original_img.size

    display_max = 750
    padding_bottom = 60

    scale = min(display_max / orig_width, display_max / orig_height, 1)
    disp_width = int(orig_width * scale)
    disp_height = int(orig_height * scale)
    display_img = original_img.resize((disp_width, disp_height), Image.LANCZOS)

    win_width = disp_width
    win_height = disp_height + padding_bottom

    crop_gui = tk.Toplevel()
    crop_gui.title("Crop Image")
    crop_gui.geometry(f"{win_width}x{win_height}")
    crop_gui.resizable(False, False)

    crop_gui.lift()
    crop_gui.attributes('-topmost', True)
    crop_gui.focus_force()
    crop_gui.after(200, lambda: crop_gui.attributes('-topmost', False))

    canvas = tk.Canvas(crop_gui, width=disp_width, height=disp_height, cursor="cross")
    canvas.pack()

    tk_img = ImageTk.PhotoImage(display_img)
    canvas.create_image(0, 0, anchor="nw", image=tk_img)

    rect = None
    start_x = start_y = end_x = end_y = 0
    result_path = None

    def on_mouse_down(event):
        nonlocal start_x, start_y, rect
        start_x, start_y = event.x, event.y
        if rect:
            canvas.delete(rect)
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red")

    def on_mouse_move(event):
        if rect:
            canvas.coords(rect, start_x, start_y, event.x, event.y)

    def on_mouse_up(event):
        nonlocal end_x, end_y
        end_x, end_y = event.x, event.y

    def on_crop():
        nonlocal result_path
        crop_x1 = int(min(start_x, end_x) / scale)
        crop_y1 = int(min(start_y, end_y) / scale)
        crop_x2 = int(max(start_x, end_x) / scale)
        crop_y2 = int(max(start_y, end_y) / scale)

        box = (crop_x1, crop_y1, crop_x2, crop_y2)
        cropped_img = original_img.crop(box)

        filename = f"cropped_{int(time.time())}.png"
        result_path = os.path.join(output_dir, filename)
        cropped_img.save(result_path)

        crop_gui.destroy()

    def on_cancel():
        crop_gui.destroy()

    btn_frame = tk.Frame(crop_gui)
    btn_frame.pack(pady=10)

    crop_btn = tk.Button(btn_frame, text="Crop and Save", command=on_crop, width=15)
    crop_btn.pack(side="left", padx=10)

    cancel_btn = tk.Button(btn_frame, text="Cancel", command=on_cancel, width=15)
    cancel_btn.pack(side="right", padx=10)

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_move)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    crop_gui.grab_set()
    crop_gui.wait_window()

    return result_path



