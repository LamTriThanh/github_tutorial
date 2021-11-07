import cv2 as cv

capture = cv.VideoCapture(r'C:\Users\user0\Desktop\computer_study\opencv_course\video\dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break   

capture.release()
cv.destroyAllWindows()