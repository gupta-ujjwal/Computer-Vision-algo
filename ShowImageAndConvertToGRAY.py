import cv2

image = cv2.imread('1.jpeg')
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('window',greyImage)
cv2.waitKey(8000)
cv2.destroyAllWindows()
cv2.imwrite('1copy.jpeg',image)
