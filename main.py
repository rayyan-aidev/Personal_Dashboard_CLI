if __name__ == "__main__":
    print("This is the personal dashboard CLI.")
    while True:
        print("To [E]xit")
        command = input(
            "What do you want to do?\n1-Clock and Timer\n2-Notes\n3-Calculator\n4-To-do app\n5-Goal tracker\n6-User profile").strip()
        if command.lower() == "e":
            print("Exiting the personal dashboard CLI.")
            break
        elif command == "1":
            import timer
