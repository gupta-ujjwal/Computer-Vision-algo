import cv2

#o for camera and file name for a saved video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Window', frame)
        if cv2.waitKey(1) & 0XFF == 27: #ASCII for exc
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
