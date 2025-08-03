import time
from datetime import datetime, timezone

print("This is the clock app.")
while True:
    print("To go [B]ack.")
    timer_command = input(
        "What do you want to view\n1-World Clock\n2-Timer\n3-Stopwatch\n").strip()
    if timer_command.lower() == "b":
        break
    if timer_command == "1":
        print("World Clock")
        print("Current time in UTC:", datetime.now(
            timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
        print("Current time in your local timezone:",
              datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("To [B]ack")
        if input().strip().lower() == "b":
            continue
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
    elif timer_command == "3":
        start = input("Press [s] to start.\n")
        if start.lower().strip() == "b":
            break
        if start.strip().lower() == "s":
            start_time = time.time()
            print("Stopwatch started. Press [s] to stop.")
            while True:
                if input().strip().lower() == "s":
                    break
            elapsed_time = time.time() - start_time
            if elapsed_time < 60:
                print(
                    f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
            elif elapsed_time < 3600:
                print(
                    f"Stopwatch stopped. Elapsed time: {elapsed_time / 60:.2f} minutes.")
            else:
                print(
                    f"Stopwatch stopped. Elapsed time: {elapsed_time / 3600:.2f} hours.")
        continue
    else:
        print("Invalid command. Please try again.")
        continue
