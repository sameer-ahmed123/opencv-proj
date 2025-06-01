import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm




pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()  # object of custom class

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPositions(img,draw=False)

    if len(lmlist) != 0:
        print(lmlist[4])
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(
        img,
        str(int(fps)),
        (10, 70),
        cv2.FONT_HERSHEY_COMPLEX,
        3,
        (255, 245, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
