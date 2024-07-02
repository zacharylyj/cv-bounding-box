import ctypes
import pytesseract
import tkinter as tk
from PIL import ImageGrab, Image, ImageTk
import cv2
import numpy as np
import time

debug = False

# Set DPI Awareness to handle different screen scales use 1 or 2 idk what it does but 2 works LOL
ctypes.windll.shcore.SetProcessDpiAwareness(2)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def parse_geometry(geometry):
    width_height, x_y = geometry.split("+", 1)
    width, height = map(int, width_height.split("x"))
    x, y = map(int, x_y.split("+"))
    return width, height, x, y


def capture_and_ocr():
    root.withdraw()
    root.update()
    time.sleep(0.05)
    geometry = root.geometry()
    if debug:
        print(f"Current geometry: {geometry}")
    _, height, _, _ = parse_geometry(geometry)

    manual_y_offset = -height + 5  # 5 cause this
    if debug:
        print(manual_y_offset)
    x1 = root.winfo_rootx() + 5  # 5 cause this
    y1 = root.winfo_rooty() + root.winfo_height() + manual_y_offset
    x2 = x1 + root.winfo_width() - 10
    y2 = y1 + (root.winfo_height() - 10)
    if debug:
        print(f"Capture coords: x1={x1}, y1={y1}, x2={x2}, y2={y2}")

    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    root.deiconify()

    img_np = np.array(img)
    img_show = Image.fromarray(img_np)
    photo = ImageTk.PhotoImage(image=img_show)
    label.config(image=photo)
    label.image = photo

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(frame)
    print(f"{"‾"*30}\n{text}\n{"_"*30}")

    root.after(3000, capture_and_ocr)


root = tk.Tk()
root.title("Text Viewer")
root.geometry("100x50")
root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(bg="#5ce65c")

label = tk.Label(root, bd=1, relief="solid", bg="#5ce65c")
label.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)


def dragwin(event):
    root.geometry(f"+{event.x_root - offset_x}+{event.y_root - offset_y}")


def clickwin(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y


root.bind("<Button-1>", clickwin)
root.bind("<B1-Motion>", dragwin)

root.after(500, capture_and_ocr)
root.mainloop()
