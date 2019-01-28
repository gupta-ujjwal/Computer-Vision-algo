

import cv2
import numpy as np
#o for camera and file name for a saved video

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('frontface_alt.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imshow('window',frame)
    if cv2.waitKey(1) & 0xFF == 27: #ASCII for exc
        break
cap.release()
cv2.destroyAllWindows()
