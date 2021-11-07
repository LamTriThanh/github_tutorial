import cv2 as cv

capture = cv.VideoCapture(r'C:\Users\user0\Desktop\computer_study\opencv_course\video\dog.mp4')
img = cv.imread(r'C:\Users\user0\Desktop\computer_study\opencv_course\img\cat.jpg')


def rescaleFrame(frame, scale=0.67):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    demenstions = (w,h)

    return cv.resize(frame, demenstions, interpolation=cv.INTER_AREA)


resized_img = rescaleFrame(img)
cv.imshow("img", resized_img)

while True:
    isTrue, frame = capture.read()
    frameResized = rescaleFrame(frame, scale=.2)
    cv.imshow("video", frame)
    cv.imshow("video resized", frameResized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break       

capture.release()
cv.destroyAllWindows()