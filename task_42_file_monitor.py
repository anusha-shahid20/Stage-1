import os
import time


def monitor_folder(folder_path):
    # Get the initial list of files
    known_files = set(os.listdir(folder_path))
    print(f"Monitoring: {folder_path}")
    print("Press Ctrl+C to stop.\n")

    # Keep checking for new files
    while True:
        time.sleep(2)  # wait 2 seconds between checks

        current_files = set(os.listdir(folder_path))
        new_files = current_files - known_files

        for file in new_files:
            print(f"New file detected: {file}")

        # Update the known files list
        known_files = current_files


folder = input("Enter folder path to monitor: ")
monitor_folder(folder)