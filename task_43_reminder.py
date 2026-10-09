import time


def reminder(message, interval, count):
    # Loop 'count' times
    for i in range(count):
        # Print the reminder message with counter
        print(f"[Reminder {i + 1}/{count}] {message}")

        # Sleep between reminders (but not after the last one)
        if i < count - 1:
            time.sleep(interval)


# Get user input
message = input("Enter reminder message: ")
interval = int(input("Enter interval in seconds: "))
count = int(input("How many times: "))

print(f"\nStarting reminders every {interval} seconds...\n")

# Call the function
reminder(message, interval, count)

print("\nDone!")