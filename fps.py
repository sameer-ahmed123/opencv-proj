import cv2 as cv
import time

def main():
    # Try to open the default camera (index 0)
    # You might need to change the index if you have multiple cameras
    # e.g., cv.VideoCapture(1) or cv.VideoCapture(cv.CAP_DSHOW) on some Windows systems
    cap = cv.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video device.")
        exit()
    else:
        print("Camera opened successfully. Press 'q' to quit.")

    # Variables for FPS calculation
    prev_frame_time = 0
    new_frame_time = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Time when we finish processing for this frame
        new_frame_time = time.time() # Using time.time() for simplicity

        # Calculate FPS
        # The time for one frame is the difference between the current and previous new_frame_time
        # Avoid division by zero at the very first frame
        if prev_frame_time != 0:
            fps = 1 / (new_frame_time - prev_frame_time)
        else:
            fps = 0 # Or any placeholder for the first frame

        prev_frame_time = new_frame_time

        # Convert FPS to string to display
        fps_text = f"FPS: {fps:.2f}" # Format to two decimal places

        # --- Display the FPS on the frame ---
        # Font type
        font = cv.FONT_HERSHEY_SIMPLEX
        # Position of the text (bottom-left corner of text)
        position = (10, 30) # (x, y) coordinates from top-left
        # Font scale (size)
        font_scale = 1
        # Font color (BGR format - Blue, Green, Red)
        font_color = (0, 255, 0) # Green
        # Line thickness
        line_type = 2
        # Put the text on the frame
        cv.putText(frame, fps_text, position, font, font_scale, font_color, line_type)

        # Display the resulting frame
        cv.imshow('Camera Feed - Press Q to Quit', frame)

        # Check for 'q' key press to exit
        # cv.waitKey(1) returns the ASCII value of the key pressed or -1 if no key is pressed
        # 0xFF is a bitmask to get the last 8 bits (for compatibility)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and destroy all windows
    cap.release()
    cv.destroyAllWindows()
    print("Camera feed stopped and resources released.")

main()