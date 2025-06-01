import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:  # if hand landmarks are in frame
            # number of hands in frame (handlandmarks of multihands)
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPositions(self, img, handNo=0, draw=True):
        lmlist = []

        if self.results.multi_hand_landmarks:  # check if hand land marks are detected  on screen
            # select a specific hand from the ones detected
            myhand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myhand.landmark):
                # print(id, lm)
                h, w, c = img.shape  # height ,widhth and channel  , getting from  the img.shape
                cx, cy = int(lm.x * w), int(lm.y*h)  # center position
                # prints id , x position and y position of landmark on hand
                # print(id, cx, cy)
                lmlist.append([id, cx, cy])
                if draw:
                    # id zero is landmark on wrist
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
                    # img is where to draw
                    # cx,cy are x and y pixel positions on where to draw
                    # 7 id diameter
                    # (255,0,0) is rgb color of the draw
                    # cv2.FILLED = filled drwan obj

        return lmlist


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()  # object of custom class

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPositions(img)

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


if __name__ == "__main__":
    main()


# #what is enumeirate

# WITHOUT
# fruits = ['apple', 'banana', 'cherry']
# index = 0
# for fruit in fruits:
#     print(f"Index {index}: {fruit}")
#     index += 1
# # Output:
# # Index 0: apple
# # Index 1: banana
# # Index 2: cherry

# WITH
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(f"Index {index}: {fruit}")
# # Output:
# # Index 0: apple
# # Index 1: banana
# # Index 2: cherry
