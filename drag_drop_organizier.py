import os
import shutil

from tkinter import *
from tkinter import messagebox

from tkinterdnd2 import DND_FILES
from tkinterdnd2 import TkinterDnD

# File categories
file_types = {

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".webp", ".bmp", ".svg", ".tiff",
        ".ico", ".heic"
    ],

    "PDFs": [
        ".pdf"
    ],

    "Music": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg", ".m4a", ".wma"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm",
        ".mpeg", ".3gp"
    ],

    "Documents": [
        ".txt", ".doc", ".docx",
        ".rtf", ".odt", ".tex"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx",
        ".csv", ".ods"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".odp"
    ],

    "Compressed": [
        ".zip", ".rar", ".7z",
        ".tar", ".gz", ".iso"
    ],

    "Programming": [
        ".py", ".js", ".html",
        ".css", ".php", ".java",
        ".cpp", ".c", ".json",
        ".xml", ".sql", ".sh",
        ".bat"
    ],

    "Executables": [
        ".exe", ".msi",
        ".dll", ".apk",
        ".app", ".deb"
    ],

    "Databases": [
        ".db", ".sqlite",
        ".mdb", ".accdb"
    ],

    "DesignFiles": [
        ".psd", ".ai",
        ".xd", ".fig",
        ".blend"
    ],

    "Fonts": [
        ".ttf", ".otf",
        ".woff"
    ],

    "Misc": [
        ".log", ".bak",
        ".tmp", ".dat",
        ".torrent"
    ]
}

selected_folder = ""

# Organize function
def organize_files(folder_path):

    # Create folders
    for folder_name in file_types:

        folder_dir = os.path.join(
            folder_path,
            folder_name
        )

        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

    # Scan files
    for file_name in os.listdir(folder_path):

        file_path = os.path.join(
            folder_path,
            file_name
        )

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get extension
        _, extension = os.path.splitext(file_name)

        # Match categories
        for folder_name, extensions in file_types.items():

            if extension.lower() in extensions:

                destination = os.path.join(
                    folder_path,
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
                            folder_path,
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

# Handle drop
def drop(event):

    folder_path = event.data.strip("{}")

    drop_label.config(
        text=f"Selected Folder:\n{folder_path}"
    )

    organize_files(folder_path)

# Main window
root = TkinterDnD.Tk()

root.title("Drag & Drop File Organizer")

root.geometry("600x400")

# Title
title_label = Label(
    root,
    text="Drag & Drop File Organizer",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)

# Drop area
drop_label = Label(
    root,
    text="Drag Folder Here",
    width=40,
    height=10,
    bg="lightgray",
    relief="ridge",
    font=("Arial", 14)
)

drop_label.pack(pady=30)

# Enable drag & drop
drop_label.drop_target_register(DND_FILES)

drop_label.dnd_bind('<<Drop>>', drop)

# Run app
root.mainloop()