'''
i2c_controller.py

Responsibilities
----------------
1. Open UART connection to ESP32
2. Send START / STOP commands
3. Receive responses
4. Return received data
5. Close connection safely
'''

import serial
import time

# ----------------------------------------------------
# UART Configuration
# ----------------------------------------------------

PORT = "/dev/cu.usbserial-588F0214971"
BAUD_RATE = 115200
TIMEOUT = 1

ser = None

# ----------------------------------------------------
# Open Serial Connection
# ----------------------------------------------------

def open_connection():

    global ser

    if ser is None or not ser.is_open:

        ser = serial.Serial(
            PORT,
            BAUD_RATE,
            timeout=TIMEOUT
        )

        time.sleep(2)

        print("--------------------------------")
        print("Connected to ESP32")
        print("--------------------------------")


# ----------------------------------------------------
# Send Command
# ----------------------------------------------------

def send_command(command):

    global ser

    ser.reset_input_buffer()

    ser.write((command + "\n").encode())

    print(f"Python -> ESP32 : {command}")


# ----------------------------------------------------
# Read One Line
# ----------------------------------------------------
# ----------------------------------------------------
# Read One Complete Line
# ----------------------------------------------------

def receive_data():

    global ser

    if ser is None:
        return ""

    if ser.in_waiting > 0:

        line = ser.readline().decode(
            errors="ignore"
        ).strip()

        return line

    return ""


# ----------------------------------------------------
# Close Connection
# ----------------------------------------------------

def close_connection():

    global ser

    if ser and ser.is_open:

        ser.close()

        print("\nSerial Connection Closed")