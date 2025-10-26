import time
import random

current_temp = None
is_running = True

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

    try:
        choice = int(input("Select an option (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        # temp system

        # check if current_temp is set
        if current_temp is None:
            current_temp = float(input("Enter the current temperature (°C): "))
        else:
            print(f'Current temperature: {current_temp}°C')

        change_temp = input("Do you want to change the temperature? (Y/N): ").upper()
        if change_temp == "Y":
            target_temp = float(input("Enter the target temperature (°C): "))

            if current_temp == target_temp:
                print(f"Target and current temperature is already the same. System now idle.")
            else:
                mode = "HEATING" if current_temp < target_temp else "COOLING"
                print(f"\nSystem mode: {mode}")
                print("Adjusting temperature...")

                while abs(current_temp - target_temp) > 1:
                    if current_temp < target_temp:
                        current_temp += 1
                    elif current_temp > target_temp:
                        current_temp -= 1

                    current_temp = round(current_temp, 1)
                    print(f"Current temperature: {current_temp}°C")
                    time.sleep(0.5)

                print(f"\n Target temperature of {target_temp}°C reached. System is now stable.")
        else:
            print("No changes made to the temperature.")
        
        input("Press Enter to continue...")

    elif choice == 5:
        print("Shutting down the Smart Home Controller...")
        is_running = False

    else:
        print("This option is not in the lust.")
        input("Press Enter to continue...")
