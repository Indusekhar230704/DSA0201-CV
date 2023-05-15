#  Read Image and Display it in Gray scale,
import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="C:/Users/aspi/Downloads/spiderman.png"
img =  cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur IMG",imgBlur)
cv2.waitKey(0)
