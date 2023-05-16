import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path ="C:/Users/aspi/Downloads/spiderman.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel, iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

cv2.imshow("Lena",img)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("img Blur",imgBlur)
cv2.imshow("img Canny",imgCanny)
cv2.imshow("imgDilation",imgDilation)
cv2.imshow("imgErosion",imgEroded)
cv2.waitkey(0)
