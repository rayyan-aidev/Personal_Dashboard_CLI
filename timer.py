import time
from datetime import datetime

print("This is the clock app.")
while True:
    print("To go [B]ack.")
    timer_command = input(
        "What do you want to view\n1-World Clock\n2-Timer\n3-Stopwatch\n").strip()
    if timer_command.lower() == "b":
        break
    if timer_command == "1":
        pass
    elif timer_command == "2":
        countdown_time = input(
            "Where to start countdown from(Format hours-minutes-seconds): ")
        if countdown_time.lower().strip() == "b":
            break
        countdown_time = countdown_time.split("-")
        countdown_time_list = [int(times) for times in countdown_time]
        countdown_time_seconds = (countdown_time_list[0] * 60 * 60) + (
            countdown_time_list[1] * 60) + countdown_time_list[-1]
        for i in range(countdown_time_seconds, 0, -1):
            if i > 60:
                print(f"{i // 60} minutes remaining")
            elif i < 60:
                print(f"{i} seconds remaining")
            time.sleep(1)
        print("Timer completed!")
        continue
