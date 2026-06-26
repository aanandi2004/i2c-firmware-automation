'''test_i2c.py is your manual user interface. Unlike i2c_test.py (automatic testing), this lets you type commands interactively.

Python → ESP32 → Arduino → ESP32 → Python'''

from i2c_controller import send_command, close_connection

print("===================================")
print("      I2C Command Console")
print("===================================")
print("Available Commands")
print("START")
print("STOP")
print("EXIT")
print("===================================")

while True:

    command = input("\nEnter Command : ").strip()

    if command.upper() == "EXIT":
        break

    if command.upper() not in ["START", "STOP"]:
        print("Invalid Command")
        continue

    print("\nSending Command...")

    response = send_command(command)

    print("\n----------- RESPONSE -----------")

    for line in response:
        print(line)

    print("-------------------------------")

close_connection()

print("\nSerial Connection Closed")