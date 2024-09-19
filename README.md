# Arduino Face Tracker

This project uses a USB webcam to detect human faces and sends positional data to an Arduino-controlled servo motor to track the face in real-time.

## Features

- Real-time face detection using `OpenCV`.
- Servo motor control based on face position using `pySerial`.
- Arduino integration for precise servo movement.
- Adjustable tracking parameters for face sensitivity.

## Prerequisites

- Python 3.6 or higher
- Arduino IDE
- Arduino board with connected servo motor
- USB Webcam (for face tracking)

## Installation

### Python

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arunishrajput/arduino-face-tracker.git
   cd arduino-face-tracker
   ```

2. **Create a virtual environment and activate it (optional but recommended):**

   - Create virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate virtual environment:
     - For Windows:
       ```bash
       venv\Scripts\activate
       ```
     - For Linux/Mac:
       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install the libraries manually:

   ```bash
   pip install opencv-python pyserial
   ```

### Arduino

1. **Set up Arduino hardware:**

   - Connect the servo motor to your Arduino board.
     - ***Servo Pin:*** Connect the signal pin of the servo to Pin 9 on the Arduino.
     - ***Power Pins:*** Connect the servo’s power and ground to the Arduino’s 5V and GND pins, respectively.

2. **Upload the Arduino code:**

   - Open the `arduino_code.ino` file in the Arduino IDE.
   - Select the correct board and port from Tools > Board and Tools > Port.
   - Upload the sketch to your Arduino by clicking the Upload button.

3. **Check serial communication:**

   - The Python script will communicate with the Arduino over serial (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux/Mac).
   - Ensure the correct port is selected in both the Arduino IDE and Python script.

## Usage

1. **Connect Arduino and Webcam:**

   - Ensure your Arduino is connected to your computer via USB.
   - Mount your webcam on the servo-controlled setup.

2. **Run the Python face tracking script:**

   ```bash
   python face_tracking.py
   ```

3. **Face Tracking:**

   - The webcam will detect faces, and the servo will adjust its position to track the face's movement.
   - Adjust the sensitivity and detection parameters in the script if needed.

## Configuration

- **Serial Port:** Update the serial port in the Python script (`face_tracking.py`) to match your Arduino connection.
- **Servo Sensitivity:** Tweak the `map_range` function in the Python script to adjust the servo's range of motion and smoothness.
- **Face Detection Parameters:** Modify the `detectMultiScale()` function to adjust face detection sensitivity.

## Contribution

- Feel free to fork this repository, create a feature branch, and submit a pull request. Contributions, issues, and feature requests are welcome!

## Acknowledgments

- [OpenCV](https://opencv.org/) for face detection functionality.
- [pySerial](https://pyserial.readthedocs.io/en/latest/) for serial communication with Arduino.
- [Arduino community](https://www.arduino.cc/) for providing helpful resources for servo control.
