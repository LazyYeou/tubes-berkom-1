import time

# define base variables 
current_temp = None
is_running = True
is_alarm_active = False
rooms = []
security_sensors = []

# init default rooms
rooms.append(["Living Room", False, 0])
rooms.append(["Bedroom", False, 0])
rooms.append(["Kitchen", False, 0])

# init default sensors
security_sensors.append(["Front Door","door", False])
security_sensors.append(["Back Door","door", False])
security_sensors.append(["Living Room Window","window", False])

# code main loop 
while is_running:
    print("==============================")
    print("   SMART HOME CONTROLLER CLI  ")
    print("==============================")
    print("1. Temperature Control")
    print("2. Light Control")
    print("3. Security System")
    print("4. Home Status")
    print("5. Exit")
    print("6. Sensor Inputs")
    print("==============================")

    # error handling
    try:
        choice = int(input("Select an option (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
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
            target_temp = float(input("Enter the target temperature (10 - 40) (°C): "))

            # validate target temperature
            if target_temp < 10 or target_temp > 40:
                print("Target temperature is out of range and must be between 10°C and 40°C.")
            else:
                if current_temp == target_temp:
                    print(f"Target and current temperature is already the same. System now idle.")
                else:
                    mode = "HEATING" if current_temp < target_temp else "COOLING"
                    print(f"\nSystem mode: {mode}")
                    print("Adjusting temperature...")

                    # adjust temperature loop
                    while abs(current_temp - target_temp) > 0:
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
            # check all rooms
            if light_choice == 1:
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
                
            # add room
            elif light_choice == 2:
                room_name = input("\nEnter room name: ").strip()
                
                if room_name == "":
                    print("Room name cannot be empty!")
                else:
                    # check if room name already exist and handle it
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
                
            # remove room
            elif light_choice == 3:
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
                
            # toogle rooms light
            elif light_choice == 4:
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
                        if light_on: 
                            status = f"ON ({brightness} %)"
                        else:
                            status = "OFF"
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
                
            # adjust room brightness
            elif light_choice == 5:
                if len(rooms) == 0:
                    print("\nno rooms added yet!")
                else:
                    print("\n ==== ROOMS ==== ")
                    
                    # display rooms
                    for i in range(len(rooms)):
                        room_name = rooms[i][0]
                        light_on = rooms[i][1]
                        brightness = rooms[i][2]
                        status = f"ON ({brightness}%)" if light_on else "OFF"
                        print(f"{i + 1}. {room_name}: {status}")
                    print("-" * 26)
                    
                    room_name = input("\nenter room name: ").strip()
                    
                    # find room and adjust brightnes
                    is_room_found = False
                    for i in range(len(rooms)):
                        if rooms[i][0] == room_name:
                            is_room_found = True
                            
                            if not rooms[i][1]:
                                print(f"Light in '{room_name}' is OFF Turn it on first")
                            else:
                                try:
                                    brightness = int(input("Enter brightness level (0- 100): "))

                                    # validate brightness value
                                    if 0 <= brightness and brightness <= 100:
                                        rooms[i][2] = brightness
                                        if brightness == 0:
                                            rooms[i][1] = False
                                            print(f"Light in '{room_name}' turned OFF")
                                        else:
                                            print(f"Brightness in '{room_name}' set to {brightness}%")
                                    else:
                                        print("Brightness input is out of range and must be between 0 and 100!")
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
        # security system 
        is_security_running = True
        while is_security_running:
            print("==== SECURITY SYSTEM ====")
            print("1. View sensors status")
            print("2. Add sensor")
            print("3. Remove sensor")
            print("4. Toggle door/window")
            print("5. Activate/deactivate alarm")
            print("6. Back to main menu")
            print("=========================")

            # error handling
            try:
                security_choice = int(input("Select option (1-6): "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            # check user choice
            if security_choice == 1:
                # view sensors status
                if len(security_sensors) == 0:
                    print("\nNo sensors aded yet!")
                else:
                    print("\n--- SECURITY SENSORS ---")

                    # iterate through sensors and display status
                    for i in range(len(security_sensors)):
                        location = security_sensors[i][0]
                        sensor_type = security_sensors[i][1]
                        status = security_sensors[i][2]
                        
                        if sensor_type == "door":
                            if status:
                                status_text = "LOCKED"
                            else:
                                status_text = "UNLOCKED"
                        elif sensor_type == "window":
                            if status:
                                status_text = "CLOSED"
                            else:
                                status_text = "OPEN"
                        else:
                            status_text = str(status)
                        
                        print(f"{i + 1}. {location} ({sensor_type}): {status_text}")
                    print("-" * 24)
                input("\nPress Enter to continue...")

            # add sensor
            elif security_choice == 2:
                location = input("\nEnter sensor location: ").strip()
                
                # validate location
                if location == "":
                    print("Location cannot be empty!")
                else:
                    print("\nSensor types:")
                    print("1. Door")
                    print("2. Window")
                    
                    sensor_type_choice = input("Select sensor type (1-2): ").strip()
                    
                    # check sensor type
                    if sensor_type_choice == "1":
                        sensor_type = "door"
                        default_status = True
                    elif sensor_type_choice == "2":
                        sensor_type = "window"
                        default_status = True
                    else:
                        print("Invalid sensor type!")
                        input("Press Enter to continue...")
                        continue
                    
                    # add sensor to list
                    security_sensors.append([location, sensor_type, default_status])
                    print(f"Sensor '{location}' ({sensor_type}) added successfully!")
                input("Press Enter to continue...")
            
            # remove sensor
            elif security_choice == 3:

                #display sensors
                if len(security_sensors) == 0:
                    print("\nNo sensors added yet!")
                else:
                    print("\n==== SECURITY SENSORS ====")
                    for i in range(len(security_sensors)):
                        location = security_sensors[i][0]
                        sensor_type = security_sensors[i][1]
                        print(f"{i + 1}. {location} ({sensor_type})")
                    print("-" * 24)
                    
                    location = input("\nEnter sensor location to remove: ").strip()
                    
                    sensor_found = False

                    # find and remove sensor
                    for i in range(len(security_sensors)):
                        if security_sensors[i][0] == location:
                            security_sensors.pop(i)
                            sensor_found = True
                            print(f"Sensor '{location}' removed successfully!")
                            break
                   
                    if not sensor_found:
                        print(f"Sensor '{location}' not found!")
                input("Press Enter to continue...")

                # toggle door or window lock
            elif security_choice == 4:


                if len(security_sensors) == 0:
                    print("\nNo sensors added yet!")
                else:
                    door_window_list = []
                    print("\n--- DOORS & WINDOWS ---")
                    counter = 1

                    # display doors and windows
                    for i in range(len(security_sensors)):
                        if security_sensors[i][1] == "door" or security_sensors[i][1] == "window":
                            door_window_list.append(i)
                            location = security_sensors[i][0]
                            sensor_type = security_sensors[i][1]
                            status = security_sensors[i][2]
                            if status and sensor_type == "door":
                                status_text = "LOCKED"
                            elif not status and sensor_type == "door":
                                status_text = "UNLOCKED"
                            elif status:
                                status_text = "CLOSED"
                            else:
                                status_text = "OPEN"
                            
                            print(f"{counter}. {location} ({sensor_type}): {status_text}")
                            counter += 1
                    print("-" * 23)
                    
                    if len(door_window_list) == 0:
                        print("No doors or windows founda!")
                    else:
                        location = input("\nEnter location to toggle: ").strip()
                        
                        sensor_found = False

                        # find and toggle door/window status
                        for i in door_window_list:
                            if security_sensors[i][0] == location:
                                sensor_found = True
                                security_sensors[i][2] = not security_sensors[i][2]
                                
                                if security_sensors[i][1] == "door":
                                    if security_sensors[i][2]:
                                        status_text = "LOCKED"
                                    else:
                                        status_text = "UNLOCKED"
                                else:
                                    if security_sensors[i][2]:
                                        status_text = "CLOSED"
                                    else:
                                        status_text = "OPEN"
                                
                                print(f"{location} is now {status_text}")
                                break
                        
                        if not sensor_found:
                            print(f"Door/window '{location}'not found!")
                input("Press enter to continue...")

            # activate/deactivate alarm
            elif security_choice == 5:
                if is_alarm_active:

                    # deactivate alarm
                    confirm = input("\n Deactivate alarm? (Y/N): ").upper()
                    if confirm == "Y":
                        is_alarm_active = False
                        print("Alarm deactivate")
                    else:
                        print("Alarm remains active")
                else:
                    # check if all doors and windows are locked/closed
                    all_secure = True
                    unsecure_list = []
                    
                    # find unsecure doors/windows
                    for i in range(len(security_sensors)):
                        if security_sensors[i][1] == "door" or security_sensors[i][1] == "window":
                            if not security_sensors[i][2]:
                                all_secure = False
                                unsecure_list.append(security_sensors[i][0])
                    
                    # handle unsecure doors/windows
                    if not all_secure:
                        print("\nCannot activate alarm! The following are not secure:")
                        for location in unsecure_list:
                            print(f"  - {location}")
                        print("Please lock/closed all doors and windows first.")
                    else:
                        confirm = input("\Activate alarm? (Y/N): ").upper()
                        if confirm == "Y":
                            is_alarm_active = True
                            print("Alarm activated")
                        else:
                            print("Alarm remains deactivateED")
                input("Press Enter to continue...")

            # back to main menu
            elif security_choice == 6:
                is_security_running = False
            else:
                print("Invalid option!")
                input("Press Enter to continue...")
            

        input("Press Enter to continue...")

    elif choice == 6:
        print("\n====== SENSOR INPUTS ======")
        try:
            temp_input = input("Enter current room temperature (°C) (leave blank to keep current): ").strip()
            if temp_input != "":
                current_temp = float(temp_input)
        except ValueError:
            print("Invalid temperature input! Keeping previous temperature value.")
        if len(rooms) > 0:
            for i in range(len(rooms)):
                room_name = rooms[i][0]
                try:
                    ambient_input = input(f"Ambient sensor (0-100) for {room_name}: ").strip()
                    ambient = int(ambient_input)
                    if ambient < 0:
                        ambient = 0
                    if ambient > 100:
                        ambient = 100
                except ValueError:
                    ambient = 100
                person = input(f"Sensor detect person in {room_name}? (Y/N): ").upper().strip()
                if person == "Y":
                    rooms[i][1] = True
                    brightness = 100 - ambient
                    if brightness < 0:
                        brightness = 0
                    if brightness > 100:
                        brightness = 100
                    if brightness == 0:
                        brightness = 30
                    rooms[i][2] = brightness
                else:
                    rooms[i][1] = False
                    rooms[i][2] = 0
        else:
            print("\nNo rooms added yet!")
        if len(security_sensors) > 0:
            danger_flag = False
            for i in range(len(security_sensors)):
                location = security_sensors[i][0]
                cam = input(f"Camera detect danger at {location}? (Y/N): ").upper().strip()
                if cam == "Y":
                    is_alarm_active = True
                    danger_flag = True
                    print(f"Danger detected at {location}!")
            if not danger_flag:
                print("No danger detected by cameras.")
        else:
            print("\nNo sensors added yet!")

        print("\n====== HOME STATUS ======")
        if current_temp:
            print(f"Temperatue: {current_temp}°C")
        else:
            print("Temperature: Not set")

        print("\n--- Lighting ---")
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

        print("\n--- Security ---")
        if is_alarm_active:
            print("Warning: Alarm is currently active!")
        else:
            print("Alarm is not active.")
        
        # count secure vs unsecure sensors
        secure_count = 0
        total_sensors = 0
        for i in range(len(security_sensors)):
            if security_sensors[i][1] == "door" or security_sensors[i][1] == "window":
                total_sensors += 1
                if security_sensors[i][2]:
                    secure_count += 1
        
        if total_sensors > 0:
            print(f"sensors: {secure_count}/{total_sensors} secured")
        print("========================")
        input("\nPress Enter to continue...")

    elif choice == 4:
        # home status
        print("\n====== HOME STATUS ======")
        if current_temp:
            print(f"Temperatue: {current_temp}°C")
        else:
            print("Temperature: Not set")

        print("\n--- Lighting ---")
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

        print("\n--- Security ---")
        if is_alarm_active:
            print("Warning: Alarm is currently active!")
        else:
            print("Alarm is not active.")
        
        # count secure vs unsecure sensors
        secure_count = 0
        total_sensors = 0
        for i in range(len(security_sensors)):
            if security_sensors[i][1] == "door" or security_sensors[i][1] == "window":
                total_sensors += 1
                if security_sensors[i][2]:
                    secure_count += 1
        
        if total_sensors > 0:
            print(f"sensors: {secure_count}/{total_sensors} secured")
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
