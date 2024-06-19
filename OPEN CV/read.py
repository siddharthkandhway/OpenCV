import cv2 as cv

# img=cv.imread('1275078.jpg')

# cv.imshow('car',img)

# cv.waitKey(0)

capture =cv.VideoCapture("wap.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows


