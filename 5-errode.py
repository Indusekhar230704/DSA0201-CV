import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/aspi/Downloads/abcd.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    print("Failed to load the image.")
    exit()

# Create a kernel for erosion
kernel = np.ones((5, 5), np.uint8)  # You can adjust the kernel size as needed

# Apply erosion to the image
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
