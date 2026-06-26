'''i2c_test.py → Automated functional testing
i2c_test.py should automatically test the complete communication chain:

Python → ESP32 → Arduino → ESP32 → Python'''

import os
import csv
from datetime import datetime

from i2c_controller import send_command, close_connection

# ----------------------------------------------------
# File Paths
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")

RESULT_FILE = os.path.join(LOG_DIR, "i2c_test_results.csv")

os.makedirs(LOG_DIR, exist_ok=True)

# ----------------------------------------------------
# Test Cases
# ----------------------------------------------------
test_cases = [

    {
        "TC_ID": "TC001",
        "Command": "START",
        "Expected": "START"
    },

    {
        "TC_ID": "TC002",
        "Command": "STOP",
        "Expected": "STOPPED"
    }
]

results = []

pass_count = 0
fail_count = 0

print("\n==============================")
print(" I2C AUTOMATION TEST STARTED ")
print("==============================")

# ----------------------------------------------------
# Execute Test Cases
# ----------------------------------------------------
for test in test_cases:

    print(f"\nRunning {test['TC_ID']}")

    response = send_command(test["Command"])

    actual = " ".join(response)

    if test["Expected"] in actual:

        status = "PASS"

        pass_count += 1

    else:

        status = "FAIL"

        fail_count += 1

    print("Command  :", test["Command"])
    print("Expected :", test["Expected"])
    print("Actual   :", actual)
    print("Result   :", status)

    results.append([

        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        test["TC_ID"],

        test["Command"],

        test["Expected"],

        actual,

        status
    ])

# ----------------------------------------------------
# Save CSV Report
# ----------------------------------------------------
with open(RESULT_FILE, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([

        "Timestamp",

        "Test Case",

        "Command",

        "Expected",

        "Actual",

        "Result"

    ])

    writer.writerows(results)

# ----------------------------------------------------
# Summary
# ----------------------------------------------------
total = pass_count + fail_count

print("\n==============================")
print("TEST SUMMARY")
print("==============================")

print(f"PASS : {pass_count}")

print(f"FAIL : {fail_count}")

print(f"TOTAL: {total}")

if total > 0:

    print(f"PASS %: {(pass_count/total)*100:.2f}")

print("==============================")

print(f"\nReport Saved : {RESULT_FILE}")

close_connection()

print("\nSerial Connection Closed")