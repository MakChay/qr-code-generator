import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

# Keep a reference to avoid garbage collection
qr_preview_image = None

def generate_preview():
    global qr_preview_image

    data = entry.get().strip()

    if not data:
        messagebox.showwarning("Input Error", "Please enter text or a URL.")
        return

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize for preview
    img = img.resize((180, 180))

    qr_preview_image = ImageTk.PhotoImage(img)
    preview_label.config(image=qr_preview_image)

def save_qr():
    data = entry.get().strip()

    if not data:
        messagebox.showwarning("Input Error", "Please enter text or a URL.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save QR Code As"
    )

    if not file_path:
        return

    img = qrcode.make(data)
    img.save(file_path)

    messagebox.showinfo("Success", "QR code saved successfully!")

# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("460x420")
root.resizable(False, False)

# Title
title = tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Entry
entry = tk.Entry(root, width=45, font=("Arial", 12))
entry.pack(pady=10)

# Preview Button
preview_btn = tk.Button(
    root,
    text="Preview QR Code",
    font=("Arial", 11),
    command=generate_preview
)
preview_btn.pack(pady=5)

# Preview Area
preview_label = tk.Label(root)
preview_label.pack(pady=10)

# Save Button
save_btn = tk.Button(
    root,
    text="Save QR Code",
    font=("Arial", 12),
    command=save_qr
)
save_btn.pack(pady=10)

root.mainloop()
