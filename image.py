import cv2
import numpy as np

img = cv2.imread('1.jpeg',0)
print(img.shape, img.size, img.dtype)

#replace with black
img [100:200, 400:700] = 0
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#crop
crop = img[500:800, 700:1000]
cv2.imshow('img',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
