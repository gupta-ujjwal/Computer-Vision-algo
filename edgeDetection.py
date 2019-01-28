import cv2
import numpy as np

img = cv2.imread('gslogo.png',0)

th1 = 50
th2 = 200

edge_img = cv2.Canny(img, th1, th2)

cv2.imshow('edge image', edge_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
