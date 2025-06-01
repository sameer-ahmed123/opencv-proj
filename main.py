# import cv2

# # Open the default camera (0). Use 1 or 2 for external cameras if needed.
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()

#     # If frame not read correctly
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     mirrored_frame = cv2.flip(frame, 1)

#     cv2.imshow('Mirrored Camera', mirrored_frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     # # Show the frame in a window named "Camera"
#     # cv2.imshow('Camera', frame)

#     # # Press 'q' to quit
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break

# # Release the camera and close window
# cap.release()
# cv2.destroyAllWindows()


# import torch
# import cv2

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     results = model(frame)
#     # results.print()  # prints all detections
#     annotated_frame = results.render()[0]

#     cv2.imshow("Object Detection", annotated_frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2
# from ultralytics import YOLO

# model = YOLO('yolov8n.pt')

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("could not open cam")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("failed to grab frames")
#         break

#     results = model(frame)

#     anotated_frames = results[0].plot()

#     cv2.imshow("yolov8n object detaction ", anotated_frames)

#     if cv2.waitKey(1) == ord("q"):
#         break


# cap.release()
# cv2.destroyAllWindows()



import cv2
from ultralytics import YOLO

model = YOLO('yolov8l.pt')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("could not open cam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frames")
        break

    results = model(frame)

    anotated_frames = results[0].plot()

    cv2.imshow("yolov8L object detaction ", anotated_frames)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
