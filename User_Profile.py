def user_profile():
    import os
    import json
    import time
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "user_profile.json")
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                user_data = json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            print("User profile file is empty or corrupted. PLease create a new profile.")
            user_data = {}
    else:
        user_data = {}

    print("\nUser Profile:")
    if not user_data:
        print("No user data found.")
        time.sleep(1)
    else:
        for key, value in user_data.items():
            print(f"{key}: {value}")
        time.sleep(1)
