'''
live_plot.py

Responsibilities
----------------
1. Continuously monitor logs/live_log.csv
2. Plot Distance vs Sample Number
3. Automatically refresh every 500 ms
4. Stop when the graph window is closed
'''

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
# Interactive Plot
# ----------------------------------------------------

plt.ion()

figure, axis = plt.subplots()

while plt.fignum_exists(figure.number):

    # Check if CSV exists
    if os.path.exists(LIVE_LOG):

        try:

            data = pd.read_csv(LIVE_LOG)

            axis.clear()

            if len(data) > 0:

                axis.plot(
                    range(1, len(data) + 1),
                    data["Distance(cm)"],
                    marker='o',
                    linewidth=2,
                    label="Distance"
                )

                axis.set_title("Live HC-SR04 Distance Monitoring")

                axis.set_xlabel("Sample Number")

                axis.set_ylabel("Distance (cm)")

                axis.grid(True)

                axis.legend()

        except Exception:
            pass

    # Refresh every 500 ms
    plt.pause(0.5)

plt.ioff()
plt.show()