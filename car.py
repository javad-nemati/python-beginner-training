command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started ...")
        else:
            started = True
            print("Car start")
    elif command == "stop":
        if not started:
            print("Car is Already Stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
start- for start the car
stop- for stop the car
quit- for quit
        
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I dont Understand")
