import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
temp = cv2.imread('temp.jpg')

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
temp_gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

w,h = temp_gray.shape[::-1]

result = cv2.matchTemplate(img1_gray, temp_gray, method = cv2.TM_CCORR_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img1, top_left, bottom_right, (0,255,0), 3)

cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
