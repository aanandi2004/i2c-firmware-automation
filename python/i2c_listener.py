''' i2c_listener.py → Live monitoring
Start the measurement (START)
Receive distance values
Timestamp them
Save them to logs/live_log.csv
Stop when the user presses Ctrl + C
Send STOP
Close the serial connection
'''

import os
import csv
from datetime import datetime

from i2c_controller import (
    open_connection,
    close_connection,
    receive_data,
)

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LIVE_LOG = os.path.join(LOG_DIR, "live_log.csv")

# ----------------------------------------------------
# Create CSV if it doesn't exist
# ----------------------------------------------------

if not os.path.exists(LIVE_LOG):

    with open(LIVE_LOG, "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Distance(cm)"])

# ----------------------------------------------------
# Main Listener
# ----------------------------------------------------

def main():

    open_connection()

    print("\n==============================")
    print("I2C LISTENER STARTED")
    print("==============================\n")

    print("Waiting for Distance...\n")

    try:

        while True:

            data = receive_data().strip()

            if data == "":
                continue

            print("ESP32 -> Python :", data)

            # Process only distance messages
            if "Distance Received" in data:

                try:

                    # Extract numeric value after ':'
                    distance = float(data.split(":")[1].strip())

                    timestamp = datetime.now().strftime("%H:%M:%S")

                    with open(LIVE_LOG, "a", newline="") as file:

                        writer = csv.writer(file)
                        writer.writerow([timestamp, distance])

                    print(f"Saved : {timestamp} | {distance:.2f} cm")

                except (ValueError, IndexError):

                    continue

    except KeyboardInterrupt:

        print("\nStopping Listener...")

    finally:

        close_connection()

        print("Serial Connection Closed")


if __name__ == "__main__":

    main()