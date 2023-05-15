import cv2
import numpy as np

img = cv2.imread("C:/Users/aspi/Downloads/FLOWER.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0,1,0], [1,-8,1], [0,1,0]])
sharpened = cv2.filter2D(gray, -1, kernel)

cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
