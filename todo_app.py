def todo_start():
    import os
    import json
    import time
    import datetime

    if not os.path.exists("Personal_Dashboard_CLI/todo_lists"):
        os.mkdir("Personal_Dashboard_CLI/todo_lists")

    with open("Personal_Dashboard_CLI/user_profile.json", "r") as file:
        user_data = json.load(file)
        username = user_data.get("username", "Please login again")

    if not os.path.exists(f"Personal_Dashboard_CLI/todo_lists/{username}_todo_list"):
        os.mkdir(f"Personal_Dashboard_CLI/todo_lists/{username}_todo_list")

    file_path = f"Personal_Dashboard_CLI/todo_lists/{username}_todo_list/todo_list.json"

    print("This is the to-Do app.")
    while True:
        print("\n\nTo go [B]ack")
        command = input(
            "Enter your command: \n1-Add a task\n2-View tasks\n3-Update tasks status\n4-Delete a task\n").strip()
        if command.lower() == "b":
            print("Going back to main menu.")
            time.sleep(1)
            break
        elif command == "1":
            task = input("Enter the task you want to add: ")
            if task.lower().strip() == "b":
                print("Going back to main menu.")
                time.sleep(1)
                break
            if not task:
                print("Task cannot be empty. Please try again.")
                continue
            due_date = input("Enter the due date (DD-MM-YYYY): ")
            if due_date.lower().strip() == "b":
                print("Going back to main menu")
                time.sleep(1)
                break
            try:
                datetime.datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY.")
                continue
            todo_item = {"Due_date": due_date, "status": "Incomplete", "Date_added":
                         datetime.datetime.now().strftime("%d-%m-%Y")}
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as file:
                        todo_list = json.load(file)
                except json.decoder.JSONDecodeError:
                    todo_list = {}
            else:
                todo_list = {}
            todo_list[task.title().strip()] = todo_item
            with open(file_path, "w") as file:
                json.dump(todo_list, file, indent=4, sort_keys=True)
            print("Task added successfully.")
            time.sleep(1)
        elif command == "2":
            view_command = input(
                "1-View one task\n2-View all tasks\n").strip()
            if view_command.lower() == "b":
                print("Going back to the main menu.")
                break
            elif view_command == "1":
                task_to_update = input("Enter the task to view: ")
                if task_to_update.lower().strip() == "b":
                    print("Going back to main menu.")
                    time.sleep(1)
                    break
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r") as file:
                            todo_list = json.load(file)
                    except json.decoder.JSONDecodeError:
                        print("There are no tasks.")
                        continue
                    if not todo_list:
                        print("No tasks found.")
                        continue
                    if task_to_update.title().strip() in todo_list:
                        details = todo_list[task_to_update.title().strip()]
                        print(
                            f"{task_to_update}: (Due Date: {details['Due_date']}, Status: {details['status']}, Date Added: {details['Date_added']})")
                    else:
                        print("Task not found.")
                        continue
                else:
                    print("No tasks found.")
                    continue
            elif view_command == "2":
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r") as file:
                            todo_list = json.load(file)
                    except json.decoder.JSONDecodeError:
                        print("There are no tasks.")
                        continue
                    if not todo_list:
                        print("No tasks found.")
                    else:
                        for task, details in todo_list.items():
                            print(
                                f"{task}: (Due Date: {details['Due_date']}, Status: {details['status']}, Date Added: {details['Date_added']})")
                        time.sleep(1)
                else:
                    print("No tasks found.")
            else:
                print("Invalid command. please try again.")
                continue
        elif command == "3":
            task_to_update = input("Enter the task to view: ")
            if task_to_update.lower().strip() == "b":
                print("Going back to main menu.")
                time.sleep(1)
                break
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as file:
                        todo_list = json.load(file)
                except json.decoder.JSONDecodeError:
                    print("There are not tasks.")
                    continue
                if not todo_list:
                    print("No tasks found.")
                    continue
                else:
                    if task_to_update.title().strip() in todo_list:
                        details = todo_list[task_to_update.title().strip()]
                        print(
                            f"{task_to_update}: (Due Date: {details['Due_date']}, Status: {details['status']}, Date Added: {details['Date_added']})")
                        status = input(
                            "Enter the tasks status(Incomplete or Done): ").strip()
                        if status.lower() == "b":
                            print("Going back to main menu.")
                            time.sleep(1)
                            break
                        if status.lower() == "done" or status.lower() == "incomplete":
                            details["status"] = status
                            todo_list[task_to_update.title().strip()] = details
                            with open(file_path, "w") as file:
                                json.dump(todo_list, file,
                                          indent=4, sort_keys=True)
                            print("Task updated successfully.")
                            time.sleep(1)
                        else:
                            print("Please enter valid status.")
                            continue
                    else:
                        print("Task not found.")
                        continue
            else:
                print("No tasks found.")
                continue
        elif command == "4":
            task_to_delete = input("Enter the task to delete: ")
            if task_to_delete.lower().strip() == "b":
                print("Going back to main menu.")
                time.sleep(1)
                break
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r") as file:
                        todo_list = json.load(file)
                except json.decoder.JSONDecodeError:
                    print("There are no tasks.")
                    continue
                if not todo_list:
                    print("No tasks found.")
                    continue
                if task_to_delete.title().strip() in todo_list:
                    del todo_list[task_to_delete.title().strip()]
                    with open(file_path, "w") as file:
                        json.dump(todo_list, file, indent=4, sort_keys=True)
                    print("Task deleted successfully.")
                    time.sleep(1)
                else:
                    print("Task not found.")
            else:
                print("No tasks found.")
