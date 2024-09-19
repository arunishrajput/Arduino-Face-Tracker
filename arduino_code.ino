#include <Servo.h>

Servo myServo;
int servoPin = 9;  // Set the pin where the servo is connected
int position = 90; // Default position (midpoint)

void setup()
{
    myServo.attach(servoPin);
    myServo.write(position); // Move servo to the default position
    Serial.begin(9600);      // Start serial communication
}

void loop()
{
    if (Serial.available() > 0)
    {
        position = Serial.parseInt(); // Read the incoming value
        if (position >= 0 && position <= 180)
        {
            myServo.write(position); // Rotate servo to the desired position
        }
    }
}
