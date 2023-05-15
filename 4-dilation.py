#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/aspi/Downloads/abcd.jpg"
img =  cv2.imread(path)
imgDilation = cv2.dilate(img,kernel , iterations = 10)
cv2.imshow("Img Dialation",imgDilation)
cv2.waitKey(0)
