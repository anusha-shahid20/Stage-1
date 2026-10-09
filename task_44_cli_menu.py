import os
import shutil
import time
from datetime import datetime


# ---------- File Organizer ----------
def organize_files():
    folder = input("Enter folder path to organize: ")

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx"],
        "Music": [".mp3", ".wav", ".flac"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar"]
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            for folder_name, extensions in file_types.items():
                if extension in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)

                    target_path = os.path.join(target_folder, filename)
                    shutil.move(file_path, target_path)
                    print(f"Moved: {filename} -> {folder_name}/")
                    break


# ---------- Logger ----------
def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")


def view_logs():
    if not os.path.exists("app.log"):
        print("No logs yet.")
        return

    print("\n--- Logs ---")
    with open("app.log", "r") as file:
        print(file.read())


# ---------- File Monitor ----------
def monitor_folder():
    folder = input("Enter folder path to monitor: ")
    known_files = set(os.listdir(folder))

    print(f"Monitoring: {folder}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(2)
            current_files = set(os.listdir(folder))
            new_files = current_files - known_files

            for file in new_files:
                print(f"New file detected: {file}")
                write_log(f"New file detected: {file}")

            known_files = current_files
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


# ---------- Reminder ----------
def reminder():
    message = input("Enter reminder message: ")
    interval = int(input("Enter interval in seconds: "))
    count = int(input("How many times: "))

    for i in range(count):
        print(f"[Reminder {i + 1}/{count}] {message}")
        write_log(f"Reminder shown: {message}")

        if i < count - 1:
            time.sleep(interval)


# ---------- Main Menu ----------
def main_menu():
    while True:
        print("\n===== AUTOMATION TOOL =====")
        print("1. Organize files")
        print("2. View logs")
        print("3. Monitor folder")
        print("4. Reminder")
        print("5. Exit")
        print("===========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            organize_files()
            write_log("Organized files")
        elif choice == "2":
            view_logs()
        elif choice == "3":
            monitor_folder()
        elif choice == "4":
            reminder()
        elif choice == "5":
            print("Goodbye!")
            write_log("Program exited")
            break
        else:
            print("Invalid choice. Try again.")


# Start the program
main_menu()