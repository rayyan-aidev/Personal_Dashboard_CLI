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
            goal_data = {"date added": goal_add_day,
                         "deadline": deadline, "status": "0%"}
            if os.path.exists(goal_file_path):
                with open(goal_file_path, "r") as file:
                    goals = json.load(file)
            else:
                goals = {}
            goals[goal.title().strip()] = goal_data
            with open(goal_file_path, "w") as file:
                json.dump(goals, file, indent=4, sort_keys=True)
            print("Goal added successfully.")
            time.sleep(1)
        elif command == "2":
            view_command = input("1-View all goals\n2-View one goal\n").strip()
            if view_command.lower() == "b":
                print("Going back to the main menu.")
                break
            elif view_command == "1":
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    if not goals:
                        print("No goals found.")
                    else:
                        for goal, goal_data in goals.items():
                            print(
                                f"{goal}: (Date Added: {goal_data['date added']}, Deadline: {goal_data['deadline']}, Status: {goal_data['status']})")
                        time.sleep(1)
            elif view_command == "2":
                goal_to_view = input("Enter the goal to view: ")
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    goal_found = False
                    for goal, goal_data in goals.items():
                        if goal.lower().strip().replace(" ", "") == goal_to_view.lower().strip().replace(" ", ""):
                            print(
                                f"{goal}: (Date Added: {goal_data['date added']}, Deadline: {goal_data['deadline']}, Status: {goal_data['status']})")
                            goal_found = True
                            break
                    if not goal_found:
                        print("Goal not found.")
                else:
                    print("No goals found.")
            else:
                print("Please enter avalid action.")
        elif command == "3":
            goal_update_command = input(
                "Do you want to\n1-Update a goal\n2-Update a goal's status\n").strip()
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
                            "Enter the goal to update: ")
                        goal_found = False
                        for goal in list(goals):
                            if goal.lower().strip().replace(" ", "") == goal_to_update.lower().strip().replace(" ", ""):
                                new_goal = input(
                                    "Enter the new goal: ")
                                new_deadline = input(
                                    "Enter the new deadline (DD-MM-YYYY): ")
                                try:
                                    datetime.strptime(
                                        new_deadline, "%d-%m-%Y")
                                    updated_goal_data = goals[goal].copy()
                                    updated_goal_data["status"] = "0%"
                                    updated_goal_data["deadline"] = str(
                                        new_deadline)
                                    updated_goal_data["date added"] = datetime.now().strftime(
                                        "%d-%m-%Y")
                                    del goals[goal]
                                    goals[new_goal.title().strip()
                                          ] = updated_goal_data
                                    print("Goal updated successfully.")
                                    goal_found = True
                                    break
                                except ValueError:
                                    print(
                                        "Invalid date format. Please use DD-MM-YYYY.")
                                    break
                        if not goal_found:
                            print("Goal not found.")
                        with open(goal_file_path, "w") as file:
                            json.dump(goals, file, indent=4, sort_keys=True)
                        time.sleep(1)
                else:
                    print("No goals found.")
            elif goal_update_command == "2":
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    if not goals:
                        print("No goals to update status.")
                    else:
                        goal_to_update = input(
                            "Enter the goal to update status: ")
                        goal_found = False
                        for goal in list(goals):
                            if goal.lower().strip().replace(" ", "") == goal_to_update.lower().strip().replace(" ", ""):
                                new_status = input(
                                    "Enter the new status (e.g., 50%): ")
                                goals[goal]["status"] = new_status.strip()
                                print("Goal status updated successfully.")
                                goal_found = True
                                break
                        if not goal_found:
                            print("Goal not found.")
                        with open(goal_file_path, "w") as file:
                            json.dump(goals, file, indent=4, sort_keys=True)
                        time.sleep(1)
                else:
                    print("No goals found.")
            else:
                print("Please enter a valid action.")
        elif command == "4":
            delete_command = input("1-Delete one goal\n2-Delete all goals\n")
            if delete_command.lower() == "b":
                print("Going back to the main menu.")
                break
            elif delete_command == "1":
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    if not goals:
                        print("No goals to delete.")
                    else:
                        goal_to_delete = input(
                            "Enter the goal to delete: ")
                        goal_found = False
                        for goal in list(goals):
                            if goal.lower().strip().replace(" ", "") == goal_to_delete.lower().strip().replace(" ", ""):
                                del goals[goal]
                                print("Goal deleted successfully.")
                                goal_found = True
                                break
                        if not goal_found:
                            print("Goal not found.")
                    with open(goal_file_path, "w") as file:
                        json.dump(goals, file, indent=4, sort_keys=True)
                    time.sleep(1)
                else:
                    print("No goals found.")
            elif delete_command == "2":
                if os.path.exists(goal_file_path):
                    with open(goal_file_path, "r") as file:
                        goals = json.load(file)
                    if not goals:
                        print("No goals to delete.")
                    else:
                        goals.clear()
                        print("All goals deleted successfully.")
                    with open(goal_file_path, "w") as file:
                        json.dump(goals, file, indent=4, sort_keys=True)
                    time.sleep(1)
            else:
                print("Invalid command. Please try again.")
        else:
            print("Invalid command. Please try again.")
    print("Exiting goal tracker.")
