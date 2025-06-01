import cv2


def main():
    """
    Detects human faces in the video stream using a pre-trained Haar cascade classifier.
    """
    # 1. Open the camera.
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    # 2. Load the pre-trained Haar cascade classifier for face detection.
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        raise IOError('Unable to load the face cascade classifier')

    # 3. Create a window to display the video.
    cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)

    while True:
        # 4. Capture a frame from the camera.
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break

        # 5. Convert the frame to grayscale (face detection works on grayscale images).
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 6. Detect faces in the grayscale frame.
        faces = face_cascade.detectMultiScale(
            gray_frame, 1.3, 5)  # Parameters can be adjusted

        # 7. Draw rectangles around the detected faces.
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (255, 0, 0), 2)  # Blue rectangle

        # 8. Display the original frame with the face detections.
        # cv2.imshow("Face Detection", frame)
        mirrored_frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        cv2.imshow("Face Detection", mirrored_frame)

        # 9. Exit if the user presses 'q'.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 10. Release resources.
    cap.release()
    cv2.destroyAllWindows()


main()
