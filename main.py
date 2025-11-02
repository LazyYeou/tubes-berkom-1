import time
import random

# define base variables 
current_temp = None
is_running = True
rooms = []

# init default rooms
rooms.append(["Living Room", False, 0])
rooms.append(["Bedroom", False, 0])
rooms.append(["Kitchen", False, 0])

# code main loop 
while is_running:
    print("\n==============================")
    print("   SMART HOME CONTROLLER CLI  ")
    print("==============================")
    print("1. Temperature Control")
    print("2. Light Control")
    print("3. Security System")
    print("4. Home Status")
    print("5. Exit")
    print("==============================")

    # error handling
    try:
        choice = int(input("Select an option (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    # check conditions
    # temp system
    if choice == 1:
        if current_temp is None:
            current_temp = float(input("Enter the current temperature (°C): "))
        else:
            print(f'Current temperature: {current_temp}°C')

        change_temp = input("Do you want to change the temperature? (Y/N): ").upper()

        # check if user wants to change temperature
        if change_temp == "Y":
            target_temp = float(input("Enter the target temperature (°C): "))

            if current_temp == target_temp:
                print(f"Target and current temperature is already the same. System now idle.")
            else:
                mode = "HEATING" if current_temp < target_temp else "COOLING"
                print(f"\nSystem mode: {mode}")
                print("Adjusting temperature...")

                # adjust temperature loop
                while abs(current_temp - target_temp) > 1:
                    if current_temp < target_temp:
                        current_temp += 1
                    elif current_temp > target_temp:
                        current_temp -= 1

                    # round temperature value
                    current_temp = round(current_temp, 1)
                    print(f"Current temperature: {current_temp}°C")

                    # give time delay
                    time.sleep(0.5)

                print(f"\nTarget temperature of {target_temp}°C reached. System is now stable.")
        else:
            print("No changes made to the temperature.")
        
        input("Press Enter to continue...")
    
    # light control
    elif choice == 2:
        is_light_running = True

        # light control loop
        while is_light_running:
            print("==== LIGHT CONTROL SYSTEM ====")
            print("1. View all rooms")
            print("2. Add room")
            print("3. Remove room")
            print("4. Toggle room light")
            print("5. Adjust brightness")
            print("6. Toggle all lights")
            print("7. Back to main menu")
            print("================================")
            
            # error handling
            try:
                light_choice = int(input("Select option (1-7): "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
            # check light control user choice
            if light_choice == 1:
                # check all rooms
                if len(rooms) == 0:
                    print("\nNo rooms added yet!")
                else:
                    print("--- ROOMS IN YOUR HOME ---")

                    # iterate through rooms and display each room status
                    for i in range(len(rooms)):
                        room_name = rooms[i][0]
                        light_on = rooms[i][1]
                        brightness = rooms[i][2]
                        if light_on: 
                            status = f"ON ({brightness} %)"
                        else:
                            status = "OFF"
                        print(f"{i + 1}. {room_name}: {status}")
                    print("-" * 26)
                input("\nPress Enter to continue...")
                
            elif light_choice == 2:
                # add room
                room_name = input("\nEnter room name: ").strip()
                
                if room_name == "":
                    print("Room name cannot be empty!")
                else:
                    # check if room name already exist
                    room_exists = False
                    for i in range(len(rooms)):
                        if rooms[i][0] == room_name:
                            room_exists = True
                            break
                    
                    if room_exists:
                        print(f"Room '{room_name}' already exists!")
                    else:
                        rooms.append([room_name, False, 0])
                        print(f"Added room '{room_name}'!")
                input("Press Enter to continue...")
                
            elif light_choice == 3:
                # remove room
                if len(rooms) == 0:
                    print("\nNo rooms added yet")
                else:
                    print("\n==== ROOMS IN YOUR HOME ====")

                    # iterate through rooms and display each room status
                    for i in range(len(rooms)):
                        room_name = rooms[i][0]
                        light_on = rooms[i][1]
                        brightness = rooms[i][2]
                        status = f"ON ({brightness}%)" if light_on else "OFF"
                        print(f"{i + 1}. {room_name}: {status}")
                    print("-" * 26)
                    
                    room_name = input("\nEnter room name to remove: ").strip()
                    
                    # find and remove room
                    is_room_found = False
                    for i in range(len(rooms)):
                        if rooms[i][0] == room_name:
                            rooms.pop(i)
                            is_room_found = True
                            print(f"Room '{room_name}' removed successfully!")
                            break
                    
                    # handle if room not found
                    if not is_room_found:
                        print(f"Room '{room_name}' not found!")
                input("Press Enter to continue...")
                
            elif light_choice == 4:
                # toogle rooms light
                if len(rooms) == 0:
                    print("\nNo rooms added yet!")

                # display rooms
                else:
                    print("\n ==== ROOMS IN YOUR HOME ==== ")
                    for i in range(len(rooms)):
                        room_name = rooms[i][0]
                        light_on = rooms[i][1]
                        brightness = rooms[i][2]
                        status = f"ON ({brightness}%)" if light_on else "OFF"
                        print(f"{i + 1}. {room_name}: {status}")
                    print("-" * 26)
                    
                    room_name = input("\nEnter room name: ").strip()
                    
                    # find room name and toggle light
                    is_room_found = False
                    for i in range(len(rooms)):
                        if rooms[i][0] == room_name:
                            is_room_found = True
                            rooms[i][1] = not rooms[i][1]
                            
                            if rooms[i][1]:
                                # when light is turned on, set brightness to 100%
                                if rooms[i][2] == 0:
                                    rooms[i][2] = 100
                                print(f"Light in '{room_name}' turned ON at {rooms[i][2]}%")
                            else:
                                print(f"Light in '{room_name}' turned OFF")
                            break

                    # handle if room not found
                    if not is_room_found:
                        print(f"Room '{room_name}' not found!")
                input("Press Enter to continue...")
                
            elif light_choice == 5:
                # adjust room brightness
                if len(rooms) == 0:
                    print("\nNo rooms added yet!")
                else:
                    print("\n ==== ROOMS IN YOUR HOME ==== ")
                    
                    # display rooms
                    for i in range(len(rooms)):
                        room_name = rooms[i][0]
                        light_on = rooms[i][1]
                        brightness = rooms[i][2]
                        status = f"ON ({brightness}%)" if light_on else "OFF"
                        print(f"{i + 1}. {room_name}: {status}")
                    print("-" * 26)
                    
                    room_name = input("\nEnter room name: ").strip()
                    
                    # find room and adjust brightnes
                    is_room_found = False
                    for i in range(len(rooms)):
                        if rooms[i][0] == room_name:
                            is_room_found = True
                            
                            if not rooms[i][1]:
                                print(f"Light in '{room_name}' is OFF. Turn it on first!")
                            else:
                                try:
                                    brightness = int(input("Enter brightness level (0-100): "))
                                    if 0 <= brightness <= 100:
                                        rooms[i][2] = brightness
                                        if brightness == 0:
                                            rooms[i][1] = False
                                            print(f"Light in '{room_name}' turned OFF")
                                        else:
                                            print(f"Brightness in '{room_name}' set to {brightness}%")
                                    else:
                                        print("Brightness must be between 0 and 100!")
                                except ValueError:
                                    print("Invalid brightness value!")
                            break
                    
                    # handle if room not found
                    if not is_room_found:
                        print(f"Room '{room_name}' not found!")
                input("Press Enter to continue...")
                
            elif light_choice == 6:
                # toggle all lights
                if len(rooms) == 0:
                    print("\nNo rooms added yet!")
                else:
                    action = input("\nTurn all lights ON or OFF? (ON/OFF): ").upper()
                    
                    # handle action
                    if action == "ON":
                        for i in range(len(rooms)):
                            rooms[i][1] = True
                            if rooms[i][2] == 0:
                                rooms[i][2] = 100
                        print("All lights turned ON")
                    elif action == "OFF":
                        for i in range(len(rooms)):
                            rooms[i][1] = False
                        print("All lights turned OFF")
                    else:
                        print("Invalid option!")
                input("Press Enter to continue...")
            
            # back to main menu
            elif light_choice == 7:
                is_light_running = False
            else:
                print("Invalid option")
                input("Press Enter to continue...")

    # security system
    elif choice == 3:
        print("\nSecurity System - Coming soon!")
        input("Press Enter to continue...")

    elif choice == 4:
        # home status
        print("\n====== HOME STATUS ======")
        if current_temp:
            print(f"Temperatue: {current_temp}°C")
        else:
            print("Temperature: Not set")

        print("\n--- Lighnting ---")
        if len(rooms) > 0:
            lights_on_count = 0
            for i in range(len(rooms)):
                if rooms[i][1]:
                    lights_on_count += 1
                    print(f"  {rooms[i][0]}: ON ({rooms[i][2]}%)")
                else:
                    print(f"  {rooms[i][0]}: OFF")
            print(f"\nTotal: {lights_on_count}/{len(rooms)} lights ON")
        else:
            print("  No rooms configured")
        print("========================")
        input("\nPress Enter to continue...")

    # exit program
    elif choice == 5:
        print("Shutting down the Smart Home Controller...")
        is_running = False

    # invalid option handler
    else:
        print("This option is not in the list.")
        input("Press Enter to continue...")