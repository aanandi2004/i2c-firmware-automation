#include <Wire.h>                  // I2C Communication Library

#define SLAVE_ADDRESS 8            // Arduino Slave Address

// ---------------- Hardware Connections ----------------
const int trigPin = 13;            // HC-SR04 Trigger Pin
const int echoPin = 11;            // HC-SR04 Echo Pin
const int ledPin = 5;              // Status LED
const int buttonPin = 6;   
bool lastButtonState = HIGH;        // Push Button (Active LOW)

// ---------------- Global Variables ----------------
String command = "";               // Command received from ESP32

bool measurementEnabled = false;   // START = true, STOP = false

float latestDistance = 0.0;        // Stores latest measured distance

// ------------------------------------------------------
// Function : Measure Distance using Ultrasonic Sensor
// ------------------------------------------------------
float readDistance()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);

    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);

    return (duration * 0.0343) / 2.0;
}

// ------------------------------------------------------
// I2C Receive Callback
// Executes whenever ESP32 sends a command
// ------------------------------------------------------
void receiveEvent(int howMany)
{
    command = "";

    // Read complete command from ESP32
    while (Wire.available())
    {
        command += (char)Wire.read();
    }

    command.trim();

    Serial.print("Received from ESP32 : ");
    Serial.println(command);

    // ---------------- START Command ----------------
    if (command == "START" || command == "start")
    {
        measurementEnabled = true;

        Serial.println("Measurement ENABLED");
        Serial.println("Waiting for Button Press...");
    }

    // ---------------- STOP Command ----------------
    else if (command == "STOP" || command == "stop")
    {
        measurementEnabled = false;

        digitalWrite(ledPin, LOW);

        Serial.println("Measurement DISABLED");
        Serial.println("LED : OFF");
    }

    // ---------------- Invalid Command ----------------
    else
    {
        Serial.println("Unknown Command");
    }
}

// ------------------------------------------------------
// I2C Request Callback
// Executes whenever ESP32 requests data
// ------------------------------------------------------
//------------------------------------------------------
// I2C Request Callback
// Sends the latest distance to ESP32
//------------------------------------------------------
void requestEvent()
{
    if (measurementEnabled)
    {
        // Convert float to string with 2 decimal places
        char distanceBuffer[10];
        dtostrf(latestDistance, 5, 2, distanceBuffer);

        Wire.write(distanceBuffer);
    }
    else
    {
        Wire.write("STOPPED");
    }
}

void setup()
{
    // UART Debug Communication
    Serial.begin(9600);

    // Ultrasonic Sensor Configuration
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);

    // LED Configuration
    pinMode(ledPin, OUTPUT);

    // Button Configuration
    pinMode(buttonPin, INPUT_PULLUP);

    // Initialize Arduino as I2C Slave
    Wire.begin(SLAVE_ADDRESS);

    // Register I2C Callbacks
    Wire.onReceive(receiveEvent);
    Wire.onRequest(requestEvent);

    Serial.println("--------------------------------");
    Serial.println("Arduino Slave Ready");
    Serial.println("Waiting for START Command...");
    Serial.println("--------------------------------");
}

void loop()
{
    if (measurementEnabled)
    {
        bool currentButtonState = digitalRead(buttonPin);

        if (currentButtonState != lastButtonState)
        {
            lastButtonState = currentButtonState;

            if (currentButtonState == LOW)
            {
                digitalWrite(ledPin, HIGH);

                latestDistance = readDistance();

                Serial.print("Button : PRESSED");
                Serial.print(" | LED : ON");
                Serial.print(" | Distance : ");
                Serial.print(latestDistance);
                Serial.println(" cm");
            }
            else
            {
                digitalWrite(ledPin, LOW);

                Serial.println("Button : RELEASED | LED : OFF");
            }
        }
    }
    else
    {
        digitalWrite(ledPin, LOW);
    }

    delay(100);
}