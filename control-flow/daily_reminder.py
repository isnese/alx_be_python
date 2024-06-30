task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Convert input to lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Reminder message based on priority and time sensitivity
match priority:
    case "high":
        reminder_text = "a high priority task"
        if time_bound == "yes":
            reminder_text += " that requires immediate attention today!"
        else:
            reminder_text += "."
    case "medium":
        reminder_text = "a medium priority task."
    case "low":
        reminder_text = "a low priority task. Consider completing it when you have free time."

print(f"Reminder: '{task}' is {reminder_text}")
