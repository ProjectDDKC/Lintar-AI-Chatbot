import customtkinter as ctk

from PIL import Image, ImageTk, ImageDraw

def create_circle_image(path, size=(100, 100)):
    img = Image.open(path).convert("RGBA").resize(size)
    
    # สร้างหน้ากากวงกลม
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    # วางหน้ากากลงบนรูปภาพ
    result = Image.new("RGBA", size)
    result.paste(img, (0, 0), mask=mask)
    return ImageTk.PhotoImage(result)
