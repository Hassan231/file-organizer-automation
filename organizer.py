import os
import shutil

# Current project folder
base_folder = os.path.dirname(os.path.abspath(__file__))

# downloads folder inside project
source_folder = os.path.join(base_folder, "downloads")

# Categories
file_types = {

    "Images": [
        ".jpg", ".jpeg", ".png",
        ".gif", ".webp", ".svg"
    ],

    "PDFs": [
        ".pdf"
    ],

    "Music": [
        ".mp3", ".wav", ".aac"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov"
    ],

    "Documents": [
        ".txt", ".docx", ".pptx",
        ".xlsx", ".csv"
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

# Create folders
for folder_name in file_types:

    folder_path = os.path.join(source_folder, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Scan files
for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get extension
    _, extension = os.path.splitext(file_name)

    # Check categories
    for folder_name, extensions in file_types.items():

        if extension.lower() in extensions:

            destination = os.path.join(
                source_folder,
                folder_name,
                file_name
            )

            # DUPLICATE HANDLING
            if os.path.exists(destination):

                name, ext = os.path.splitext(file_name)

                counter = 1

                while os.path.exists(destination):

                    new_name = f"{name}_{counter}{ext}"

                    destination = os.path.join(
                        source_folder,
                        folder_name,
                        new_name
                    )

                    counter += 1

            shutil.move(file_path, destination)

            print(f"Moved {file_name} -> {folder_name}")

            break