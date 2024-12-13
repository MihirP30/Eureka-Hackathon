import tkinter as tk
from tkinter import filedialog

def get_folder_path():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Folder path:", folder_path)

root = tk.Tk()
root.title("Folder Path Input")
root.geometry("300x100")

label = tk.Label(root, text="Please select a folder:")
label.pack(pady=10)

button = tk.Button(root, text="Browse", command=get_folder_path)
button.pack(pady=5)

root.mainloop()