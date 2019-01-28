import cv2
import numpy as np

img = cv2.imread('1.jpeg')

kernal = np.ones((9,9),np.float32)/81

dst = cv2.filter2D(img, -1, kernal)

cv2.imshow('img', img)
cv2.imshow('blurred',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
