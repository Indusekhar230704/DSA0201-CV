import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/aspi/Downloads/FLOWER.jpg")
img = cv2.resize(img,(255, 255))
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply the Laplacian filter with a positive center coefficient
laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_img = cv2.filter2D(gray_img, -1, laplacian_kernel)

# Convert the image back to color
sharpened_img = cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)

# Display the original and sharpened images
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

