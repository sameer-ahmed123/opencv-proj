import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

hands = mpHands.Hands(False)
while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # print(results.multi_hand_landmarks)
    # for hands in results:
    if results.multi_hand_landmarks:  # if hand landmarks are in frame
        # number of hands in frame (handlandmarks of multihands)
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape  # height ,widhth and channel  , getting from  the img.shape
                cx, cy = int(lm.x * w), int(lm.y*h)  # center position
                # prints id , x position and y position of landmark on hand
                print(id, cx, cy)

                if id == 4:  # id zero is landmark on wrist
                    cv2.circle(img, (cx, cy), 15, (255, 255, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

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





# media pipe 
