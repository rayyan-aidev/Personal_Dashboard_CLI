import Simple_Calculator_upd
import notes_app
import timer
import goal_tracker
if __name__ == "__main__":
    print("This is the personal dashboard CLI.")
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
            pass
        elif command == "5":
            goal_tracker.goal_tracker()
        elif command == "6":
            pass
