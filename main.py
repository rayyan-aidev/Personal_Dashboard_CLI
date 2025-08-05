import Simple_Calculator_upd
import notes_app
import timer
import goal_tracker
import login_system
import todo_app
import json
import User_Profile
from datetime import datetime, timedelta


if __name__ == "__main__":
    print("This is the personal dashboard CLI.")
    login_successful, username = login_system.login_screen()
    if login_successful:
        user_profile_path = "Personal_Dashboard_CLI/user_profile.json"
        today = datetime.now().date()
        try:
            with open(user_profile_path, "r") as file:
                user_data = json.load(file)
                if not user_data:
                    print("No user profile found. Creating a new profile.")
                    user_data = {"username": username, "login_time": today.strftime(
                        "%Y-%m-%d"), "streak": 1}
                last_login = datetime.strptime(
                    user_data.get("login_time", ""), "%Y-%m-%d").date()
                streak = user_data.get("streak", 1)
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            last_login = None
            streak = 1

        if last_login is not None:
            if today == last_login:
                print(f"Welcome back! Your current streak is {streak}.")
            elif today == last_login + timedelta(days=1):
                streak += 1
                print(f"Streak increased! Your current streak is {streak}.")
            else:
                streak = 1
                print("Streak reset. Welcome back! Your current streak is 1.")
        else:
            print("Welcome! Starting your streak.")

        user_data = {
            "username": username,
            "login_time": today.strftime("%Y-%m-%d"),
            "streak": streak
        }
        with open(user_profile_path, "w") as file:
            json.dump(user_data, file, indent=4)
        while True:
            print("\n\nTo [E]xit")
            command = input(
                "What do you want to do?\n1-Clock and Timer\n2-Notes\n3-Calculator\n4-To-do app\n5-Goal tracker\n6-User profile\n").strip()
            if command.lower() == "e":
                print("Exiting the personal dashboard CLI.")
                break
            elif command == "1":
                timer.timer()
            elif command == "2":
                notes_app.notes()
            elif command == "3":
                Simple_Calculator_upd.calculator()
            elif command == "4":
                todo_app.todo_start()
            elif command == "5":
                goal_tracker.goal_tracker()
            elif command == "6":
                User_Profile.user_profile()
            else:
                print("Invalid command. Please try again.")
    else:
        print("Login failed. Please try again.")
print("You have exited the Personal Dashboard CLI.")
