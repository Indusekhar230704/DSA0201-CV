import cv2
import numpy as np

img = cv2.imread("C:/Users/aspi/Downloads/spiderman.png", cv2.IMREAD_GRAYSCALE)
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
boundary = cv2.filter2D(img, -1, kernel)
cv2.imshow('Original Image', img)
cv2.imshow('Boundary Image', boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()

