import cv2 
import time
import numpy as np
import Hand_Tracking_Module as htm
import time

wCam ,hCam = 640,480
capture = cv2.VideoCapture(0)
capture.set(3,wCam)
capture.set(4,hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)

while True:
    success, img = capture.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Frame Rate
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    # Display
    cv2.imshow("Video", img)
    cv2.waitKey(1)