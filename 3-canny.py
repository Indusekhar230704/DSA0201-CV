#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/aspi/Downloads/abcd.jpg"
img =  cv2.imread(path)
imgCanny = cv2.Canny(img,100,200)
cv2.imshow("Img Canny",imgCanny)
