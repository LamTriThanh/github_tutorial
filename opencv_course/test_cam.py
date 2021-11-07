import cv2 
import time 
##############################
wCam, hCam = 700, 600
##############################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 1
while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 38, 255), 2)

    cv2.imshow("Test camera", img)
    cv2.waitKey(1)