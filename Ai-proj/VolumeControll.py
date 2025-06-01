# libraries used
# 1 opencv -- for camera controll
# 2 mediapipe -- ml framework (with Hand model)
# 3 pycaw -- for audio control
import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
# pycaw imports
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
#########################################
wCam, hCam = 640, 480
#########################################
# check if cam is working or not
cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # id 3 = width
cap.set(4, hCam)  # id 4 = height
pTime = 0

detector = htm.HandDetector(detectionCon=0.7)

# pycaw temp
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# get volume range of device
volumeRange = volume.GetVolumeRange()
minVolume = volumeRange[0]  # min volume val
maxVolume = volumeRange[1]  # max volume val
vol = 0
voluBar = 400
voluPer = 0

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.findPositions(img, draw=False,)
    if len(lmlist) != 0:  # make sure landmarks list is not empty
        # print(lmlist[4], lmlist[8])

        # get x and y positions
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        # center of drawn line
        cx, cy = int((x1+x2)/2), int((y1+y2)/2)

        # draw on returned landmarks
        cv2.circle(img, (x1, y1), 7, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (0, 0, 255), cv2.FILLED)
        # connect the two landmarks
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        # draw circle on the center of line
        cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)

        # get lenght of the line
        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # range of the length of "line" was from  around 240 to 50
        # (for my hands , maybe diffrent for smaller or larger hands)
        # conver to vloume range  (volume range is -65 to 0)

        # interp converts range of "line" to the range of "volume (of device)"
        vol = np.interp(length, [50, 240], [minVolume, maxVolume])
        voluBar = np.interp(vol, [minVolume, maxVolume], [400, 150])
        voluPer = np.interp(vol, [minVolume, maxVolume], [0, 100])

        print(int(length), vol)
        # chage volume of device
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            # change color of center circle on line
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    # make volume display
        # also NEED to CONVERT the Range of volume to RANGE of volume box (150-400)
        # means k jab volume min ho toh box ki range 400(min) pe ho : CHECK LINE 68
        # or jan volume max ho toh box ki range 150(max) pe ho : CHECK LINE 68
    cv2.rectangle(
        img,
        (50, 150),  # initial position
        (85, 400),  # ending position
        (0, 0, 255),  # color of rect
        3  # border width
    )

    # fill inside the rectacgle to show volume level
    cv2.rectangle(
        img,
        # the height of the filling bar is the level of current volume
        (50, int(voluBar)),
        (85, 400),  # ending position
        (0, 255, 255),  # color of rect
        cv2.FILLED  # border width
    )

    cv2.putText(
        img,  # on what to write
        f'{int(voluPer)}%',  # WHAT to write
        (40, 450),  # pixel position (x,y)
        cv2.FONT_HERSHEY_COMPLEX,  # font
        1,  # scale
        (0, 255, 0),  # color
        2  # thickness
    )

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(
        img,  # on what to write
        f'FPS: {int(fps)}',  # WHAT to write
        (50, 70),  # pixel position (x,y)
        cv2.FONT_HERSHEY_COMPLEX,  # font
        1,  # scale
        (255, 0, 0),  # color
        2  # thickness
    )

    cv2.imshow("Image", img)
    cv2.waitKey(1)
