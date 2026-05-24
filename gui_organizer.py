import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# File categories
file_types = {

    "Images": [
        ".jpg", ".jpeg", ".png",
        ".gif", ".webp",".jfif",".svg",".ico"
    ],

    "PDFs": [
        ".pdf"
    ],

    "Music": [
        ".mp3", ".wav"
    ],

    "Videos": [
        ".mp4", ".mkv"
    ],

    "Documents": [
        ".txt", ".docx", ".pptx",
        ".xlsx"
    ],
    "Archives": [
        ".zip", ".rar", ".7z"
    ],
        "Code": [
        ".py", ".html", ".css",
        ".js", ".json"
    ],

    "Applications": [
        ".exe", ".msi"
    ]

}

selected_folder = ""

# Select folder function
def select_folder():

    global selected_folder

    selected_folder = filedialog.askdirectory()

    folder_label.config(
        text=f"Selected Folder:\n{selected_folder}"
    )

# Organize function
def organize_files():

    if not selected_folder:

        messagebox.showwarning(
            "Warning",
            "Please select a folder first!"
        )

        return

    # Create folders
    for folder_name in file_types:

        folder_path = os.path.join(
            selected_folder,
            folder_name
        )

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Scan files
    for file_name in os.listdir(selected_folder):

        file_path = os.path.join(
            selected_folder,
            file_name
        )

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get extension
        _, extension = os.path.splitext(file_name)
        print(file_name, extension)

        # Match category
        for folder_name, extensions in file_types.items():

            if extension.lower() in extensions:

                destination = os.path.join(
                    selected_folder,
                    folder_name,
                    file_name
                )

                # Duplicate handling
                if os.path.exists(destination):

                    name, ext = os.path.splitext(file_name)

                    counter = 1

                    while os.path.exists(destination):

                        new_name = f"{name}_{counter}{ext}"

                        destination = os.path.join(
                            selected_folder,
                            folder_name,
                            new_name
                        )

                        counter += 1

                shutil.move(file_path, destination)

                break

    messagebox.showinfo(
        "Success",
        "Files organized successfully!"
    )

# Main window
root = tk.Tk()

root.title("File Organizer Automation")
root.geometry("500x300")

# Heading
title_label = tk.Label(
    root,
    text="File Organizer Automation",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)

# Select button
select_button = tk.Button(
    root,
    text="Select Folder",
    font=("Arial", 12),
    command=select_folder
)

select_button.pack(pady=10)

# Folder label
folder_label = tk.Label(
    root,
    text="No folder selected",
    wraplength=400
)

folder_label.pack(pady=10)

# Organize button
organize_button = tk.Button(
    root,
    text="Organize Files",
    font=("Arial", 12),
    command=organize_files
)

organize_button.pack(pady=20)

# Run app
root.mainloop()