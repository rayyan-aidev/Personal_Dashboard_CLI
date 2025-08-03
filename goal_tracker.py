def goal_tracker():
    import json
    import os
    from datetime import datetime
    import time
    goal_file_path = "Personal_Dashboard_CLI/goals.json"
    print("This is the goal tracker.")
    while True:
        print("\n\nTo go [B]ack")
        command = input(
            "What do you want to do?\n1-Add a goal\n2-View goals\n3-Update a goal\n4-Delete a goal\n").strip()
        if command.lower() == "b":
            print("Going back to the main menu.")
            break
        elif command == "1":
            goal = input("Enter your goal: ")
            deadline = input("Enter the deadline (DD-MM-YYYY): ").strip()
            if deadline.lower() == "b":
                print("Going back to the main menu.")
                break
            try:
                datetime.strptime(deadline, "%d-%m-%Y")
                goal_add_day = datetime.now().strftime("%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.")
                continue
            goal_data = {"goal": goal, "deadline": deadline, "status": "0%"}
            if os.path.exists(goal_file_path):
                with open(goal_file_path, "r") as file:
                    goals = json.load(file)
            else:
                goals = {}
            goals[goal_add_day] = goal_data
            with open(goal_file_path, "w") as file:
                json.dump(goals, file, indent=4, sort_keys=True)
            print("Goal added successfully.")
            time.sleep(2)
        elif command == "2":
            if os.path.exists(goal_file_path):
                with open(goal_file_path, "r") as file:
                    goals = json.load(file)
                if not goals:
                    print("No goals found.")
                else:
                    for date, goal in goals.items():
                        print(
                            f"{date}: {goal['goal']} (Deadline: {goal['deadline']}, Status: {goal['status']})")
                        time.sleep(2)
            else:
                print("No goals found.")
        elif command == "3":
            goal_update_command = input(
                "Do you want to\n1-Update a goal\n2-Updatea goal's status\n").strip()
            if goal_update_command.lower() == "b":
                break
            elif goal_update_command == "1":
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    if not goals:
                        print("No goals to update.")
                    else:
                        goal_to_update = input(
                            "Enter the date of the goal to update (DD-MM-YYYY): ")
                        if goal_to_update in goals:
                            new_goal = input("Enter the new goal: ")
                            new_deadline = input(
                                "Enter the new deadline (DD-MM-YYYY): ")
                            try:
                                datetime.strptime(new_deadline, "%d-%m-%Y")
                                goals[goal_to_update]["goal"] = new_goal
                                goals[goal_to_update]["deadline"] = new_deadline
                                goals[goal_to_update]["status"] = "0%"
                                print("Goal updated successfully.")
                            except ValueError:
                                print("Invalid date format. Please use DD-MM-YYYY.")
                        else:
                            print("Goal not found.")
                    with open(goal_file_path, "w") as file:
                        json.dump(goals, file, indent=4, sort_keys=True)
                else:
                    print("No goals found.")
