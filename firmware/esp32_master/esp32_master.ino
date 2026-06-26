#include <Wire.h>

#define SLAVE_ADDRESS 8

String command = "";

bool measurementEnabled = false;

unsigned long previousMillis = 0;
const unsigned long interval = 100;

void setup()
{
    Serial.begin(115200);

    Wire.begin(21, 22);

    Serial.println("--------------------------------");
    Serial.println("ESP32 Master Ready");
    Serial.println("Waiting for Python...");
    Serial.println("--------------------------------");
}

void loop()
{
    //--------------------------------------------------
    // Receive Commands From Python
    //--------------------------------------------------
    if (Serial.available())
    {
        command = Serial.readStringUntil('\n');
        command.trim();

        if (command.length() == 0)
            return;

        Serial.print("Received from Python : ");
        Serial.println(command);

        //--------------------------------------------------
        // START
        //--------------------------------------------------
        if (command.equalsIgnoreCase("START"))
        {
            measurementEnabled = true;

            sendCommandToArduino("START");

            Serial.println("Measurement ENABLED");
        }

        //--------------------------------------------------
        // STOP
        //--------------------------------------------------
        else if (command.equalsIgnoreCase("STOP"))
        {
            measurementEnabled = false;

            sendCommandToArduino("STOP");

            Serial.println("Measurement DISABLED");
        }

        //--------------------------------------------------
        // Invalid Command
        //--------------------------------------------------
        else
        {
            Serial.println("Unknown Command");
        }
    }

    //--------------------------------------------------
    // Keep Requesting Distance Every 100 ms
    //--------------------------------------------------
    if (measurementEnabled)
    {
        unsigned long currentMillis = millis();

        if (currentMillis - previousMillis >= interval)
        {
            previousMillis = currentMillis;

            requestDistance();
        }
    }
}

//==================================================
// Send START / STOP to Arduino
//==================================================
void sendCommandToArduino(String cmd)
{
    Wire.beginTransmission(SLAVE_ADDRESS);

    Wire.print(cmd);

    int error = Wire.endTransmission();

    if (error == 0)
    {
        Serial.print("ESP32 -> Arduino : ");

        Serial.println(cmd);
    }
    else
    {
        Serial.print("I2C Error : ");

        Serial.println(error);
    }
}

//==================================================
// Request Distance
//==================================================
//--------------------------------------------------
// Request latest distance from Arduino
//--------------------------------------------------
void requestDistance()
{
    Wire.requestFrom(SLAVE_ADDRESS, 16);

    String response = "";

    while (Wire.available())
    {
        response += (char)Wire.read();
    }

    response.trim();

    if (response == "")
        return;

    if (response == "STOPPED")
        return;

    Serial.print("Distance Received : ");
    Serial.println(response);
}