"""
daily_reminder.py
ALX Backend: control flow practice with match-case, conditionals, and loops.

Prompts the user for a single task, its priority, and whether it is time-bound,
then prints a customized reminder.
"""

def main():
    # Prompt user for inputs
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match-case on priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please choose high, medium, or low.")
            return

    # Add time sensitivity using if
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder = f"Note: {reminder}. Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please answer with yes or no.")
        return

    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
