from datetime import datetime


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")
    print(f"Logged: {message}")


log("Program started")
log("User logged in")
log("Task completed")
log("Program ended")

print("\n--- Contents of app.log ---")
with open("app.log", "r") as file:
    print(file.read())