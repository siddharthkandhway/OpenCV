import cv2
cap=cv2.VideoCapture(0)
# cap=cv2.VideoCapture('video name') for accessing the video
while True:
    ret,frame=cap.read() #cap.read() will save the frame from video or camera and save it to frame and ret is a boolean which will be false if it fails
    cv2.imshow('frame',frame)

    if cv2.waitKey(0)==ord('d'):
        break

cap.release()
cv2.destroyAllWindows()