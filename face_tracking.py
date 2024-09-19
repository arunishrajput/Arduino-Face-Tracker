import cv2
import serial
import time

# Initialize serial communication (change 'COMX' to your Arduino's serial port, or use '/dev/ttyUSB0' for Linux)
arduino = serial.Serial('COMX', 9600)
time.sleep(2)  # Allow time for the serial connection to initialize

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def map_range(value, in_min, in_max, out_min, out_max):
    # Map value from one range to another (useful for converting face position to servo angle)
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale (needed for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Get the frame's width to map face position to servo
    frame_width = frame.shape[1]

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Calculate the face's horizontal center position
        face_center_x = x + w // 2

        # Map the face position to a servo angle (0-180 degrees)
        servo_position = map_range(face_center_x, 0, frame_width, 0, 180)

        # Send the servo position to the Arduino via serial
        arduino.write(f"{servo_position}\n".encode())

        # Print position for debugging
        print(f"Servo Position: {servo_position}")

    # Display the resulting frame with detected faces
    cv2.imshow('Face Tracker', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
