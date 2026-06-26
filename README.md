# I2C Distance Measurement System

An Embedded Systems project demonstrating end-to-end communication between Python, ESP32, and Arduino Uno using UART and I2C protocols. The system measures distance using an HC-SR04 ultrasonic sensor, logs the readings, performs automated testing, and provides live visualization.

---

## Project Overview

This project consists of three devices/software layers:

Python
↓ UART
ESP32 (I2C Master)
↓ I2C
Arduino Uno (I2C Slave)
↓
HC-SR04 Ultrasonic Sensor

The Arduino measures distance only when measurement is enabled and the push button is pressed. The ESP32 communicates with the Arduino over I2C and acts as a bridge between Python and the Arduino. Python logs the received distance values into CSV files and plots them in real time.

---

## Features

- UART communication between Python and ESP32
- I2C communication between ESP32 and Arduino Uno
- HC-SR04 ultrasonic distance measurement
- Push button controlled measurement
- LED status indication
- START / STOP command handling
- Continuous live monitoring
- Automatic CSV logging
- Automated communication testing
- Real-time graph plotting

---

## Hardware Used

- ESP32 Dev Module
- Arduino Uno
- HC-SR04 Ultrasonic Sensor
- Push Button
- LED
- Breadboard
- Jumper Wires

---

## Software Used

- Arduino IDE
- Python 3
- PySerial
- Pandas
- Matplotlib
- VS Code

---

## Project Structure

```
i2c_project_phase-1
│
├── firmware
│   ├── arduino_slave
│   │   └── arduino_slave.ino
│   │
│   └── esp32_master
│       └── esp32_master.ino
│
├── python
│   ├── i2c_controller.py
│   ├── i2c_listener.py
│   ├── i2c_test.py
│   ├── test_i2c.py
│   ├── plot_results.py
│   └── live_plot.py
│
├── logs
│   ├── live_log.csv
│   ├── results.csv
│   └── i2c_test_results.csv
│
├── screenshots
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Python Files

### i2c_controller.py

Responsible for serial communication with the ESP32.

Functions:
- Open UART connection
- Send commands
- Receive responses
- Close serial connection

---

### i2c_listener.py

Performs live monitoring.

Functions:
- Receives distance values
- Adds timestamps
- Stores data in CSV
- Runs continuously until interrupted

---

### live_plot.py

Displays live distance measurements from the CSV file.

---

### plot_results.py

Displays statistical graphs after data collection.

---

### i2c_test.py

Runs automated communication tests.

---

### test_i2c.py

Contains test cases used by the automation script.

---

## Communication Flow

Python
↓

UART

↓

ESP32

↓

I2C

↓

Arduino Uno

↓

Ultrasonic Sensor

↓

Arduino

↓

ESP32

↓

Python

↓

CSV Logging

↓

Live Plot

---

## Running the Project

### 1. Upload Arduino Firmware

Upload:

firmware/arduino_slave/arduino_slave.ino

---

### 2. Upload ESP32 Firmware

Upload:

firmware/esp32_master/esp32_master.ino

---

### 3. Install Python Packages

```
pip install -r requirements.txt
```

---

### 4. Live Monitoring

```
python i2c_listener.py
```

---

### 5. Live Plot

```
python live_plot.py
```

---

### 6. Run Automated Tests

```
python i2c_test.py
```

---

### 7. Plot Stored Results

```
python plot_results.py
```

---

## Sample Output

- Distance measurement
- Live CSV logging
- Real-time graph
- Automated PASS/FAIL report

---

## Future Improvements

- OLED Display
- Wi-Fi Dashboard
- MQTT Communication
- Cloud Database
- Multiple Sensors
- FreeRTOS Tasks

---

## Author

Aanandi Arya

Electronics and Communication Engineering
Embedded Systems | IoT | VLSI