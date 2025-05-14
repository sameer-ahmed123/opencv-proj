import cv2

# Open default laptop camera (0 is default webcam index)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

# Set optional properties (optional, can be skipped)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Height

# Loop to continuously get frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame read failed, break loop
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Display the resulting frame
    cv2.imshow('Laptop Camera Feed', frame)

    # Press 'q' to exit the camera feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
