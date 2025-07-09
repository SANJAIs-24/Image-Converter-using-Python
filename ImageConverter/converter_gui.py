import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

selected_image_paths = []
window = tk.Tk()
window.title("Image Converter By SANJAI S")
window.geometry("420x450")
label = tk.Label(window, text="No image selected")
label.pack(pady=10)
format_var = tk.StringVar()
format_var.set("PNG")
formats = ["PNG", "JPG", "BMP", "GIF"]
format_menu = tk.OptionMenu(window, format_var, *formats)
format_menu.pack(pady=5)
width_label = tk.Label(window, text="Resize Width (px):")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack(pady=3)
height_label = tk.Label(window, text="Resize Height (px):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack(pady=3)
quality_label = tk.Label(window, text="JPG Compression Quality (1-100):")
quality_label.pack()
quality_entry = tk.Entry(window)
quality_entry.insert(0, "90") 
quality_entry.pack(pady=3)

def select_image():
    global selected_image_paths
    selected_image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if selected_image_paths:
        label.config(text=f"{len(selected_image_paths)} images selected")


def convert_image():
    if not selected_image_paths:
        messagebox.showwarning("No Image", "Please select at least one image.")
        return

    new_format = format_var.get().lower()
    width = width_entry.get()
    height = height_entry.get()
    quality = quality_entry.get()

    try:
        width = int(width) if width else None
        height = int(height) if height else None
        quality = int(quality) if quality else 90
    except ValueError:
        messagebox.showerror("Invalid Input", "Width, height, and quality must be numbers.")
        return

    converted_count = 0

    for path in selected_image_paths:
        try:
            img = Image.open(path)

            
            if width and height:
                img = img.resize((width, height))

            base = os.path.splitext(path)[0]
            new_path = f"{base}_converted.{new_format}"

            
            if new_format == "jpg":
                img = img.convert("RGB") 
                img.save(new_path, format="JPEG", quality=quality)
            else:
                img.save(new_path, format=new_format.upper())

            converted_count += 1

        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert:\n{path}\n{str(e)}")

    messagebox.showinfo("Done", f"Converted {converted_count} image(s) to {new_format.upper()}")

browse_btn = tk.Button(window, text="Browse Images", command=select_image)
browse_btn.pack(pady=10)
convert_btn = tk.Button(window, text="Convert Images", command=convert_image)
convert_btn.pack(pady=10)
window.mainloop()

