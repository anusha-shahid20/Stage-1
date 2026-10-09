import os
import shutil


def organize_folder(folder_path):
    # Map each category to its file extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx"],
        "Music": [".mp3", ".wav", ".flac"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar"]
    }

    # Loop through every item in the folder
    for filename in os.listdir(folder_path):
        # Build full path to the item
        file_path = os.path.join(folder_path, filename)

        # Only process files (skip subfolders)
        if os.path.isfile(file_path):
            # Get the file extension (like ".jpg") in lowercase
            extension = os.path.splitext(filename)[1].lower()

            # Check which category this extension belongs to
            for folder_name, extensions in file_types.items():
                if extension in extensions:
                    # Build target folder path
                    target_folder = os.path.join(folder_path, folder_name)

                    # Create target folder if it doesn't exist
                    os.makedirs(target_folder, exist_ok=True)

                    # Build full target path for the file
                    target_path = os.path.join(target_folder, filename)

                    # Move the file to its target folder
                    shutil.move(file_path, target_path)
                    print(f"Moved: {filename} -> {folder_name}/")

                    # Stop checking other categories
                    break


# Ask user for folder path
folder = input("Enter folder path to organize: ")

# Run the organizer
organize_folder(folder)