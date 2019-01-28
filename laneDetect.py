
# coding: utf-8

# In[1]:


import cv2
import numpy as np

img = cv2.imread('road-lane.jpg')



# In[2]:



img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernal_size=11
img_gray_blur = cv2.GaussianBlur(img_gray, (kernal_size,kernal_size), 0)
th1 = 50
th2 = 200


#edge_img = cv2.Canny(img, th1, th2)

cv2.imshow('edge image', img_gray_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:



img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernal_size
img_gray_blur = cv2.GaussianBlur(img_gray, (kernal_size,kernal_size), 0)


th1 = 50
th2 = 110

img_gray_blur_edge = cv2.Canny(img_gray_blur, th1, th2)

mask = np.zeros(img_gray.shape, dtype=np.uint8)
h,w = img_gray_blur_edge.shape

roi_corners = np.array([[(0.75*w, 0.55*h),(0.25*w,0.55*h), (0,0.9*h),(0,h), (w,h)]], dtype = np.int32)

ignore_mask_color = (255,)
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
cv2.imshow('mask',mask)

roi_img = cv2.bitwise_and(img_gray_blur_edge, mask)
cv2.imshow('roi_img', roi_img)

img_gray_blur_edge_bgr = cv2.cvtColor(img_gray_blur_edge, cv2.COLOR_GRAY2BGR)

linesP = cv2.HoughLinesP(roi_img, 5, np.pi/180,100, None, 50, 130)

if linesP is not None:
    for i in range(0, len(linesP)) :
        l = linesP[i][0]
        cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

cv2.imshow('final', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

