'''plot_results.py → Graph generation'''
import os
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")

LIVE_LOG = os.path.join(LOG_DIR, "live_log.csv")

# ----------------------------------------------------
# Check if CSV Exists
# ----------------------------------------------------
if not os.path.exists(LIVE_LOG):

    print("Error : live_log.csv not found.")
    print("Run i2c_listener.py first.")

    exit()

# ----------------------------------------------------
# Read CSV File
# ----------------------------------------------------
data = pd.read_csv(LIVE_LOG)

# ----------------------------------------------------
# Display Statistics
# ----------------------------------------------------
print("\n====================================")
print("        DISTANCE STATISTICS")
print("====================================")

print(f"Total Samples      : {len(data)}")
print(f"Minimum Distance   : {data['Distance(cm)'].min():.2f} cm")
print(f"Maximum Distance   : {data['Distance(cm)'].max():.2f} cm")
print(f"Average Distance   : {data['Distance(cm)'].mean():.2f} cm")

print("====================================")

# ----------------------------------------------------
# Plot Distance vs Sample Number
# ----------------------------------------------------
plt.figure(figsize=(10,5))

plt.plot(
    data["Distance(cm)"],
    marker='o',
    linewidth=2,
    label="Distance"
)

plt.title("HC-SR04 Distance Measurement")

plt.xlabel("Sample Number")

plt.ylabel("Distance (cm)")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.show()