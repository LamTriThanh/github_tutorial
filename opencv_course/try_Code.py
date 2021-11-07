#pylint:disable=no-member

import cv2 as cv

# img = cv.imread(r'C:\Users\user0\Desktop\computer_study\opencv_course\img\cats.jpg')
# cv.imshow('Cats', img)

capture = cv.VideoCapture(r"C:\Users\user0\Desktop\computer_study\opencv_course\video\dog.mp4")
cv.waitKey(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break   

capture.release()
cv.destroyAllWindows()