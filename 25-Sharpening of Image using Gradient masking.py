import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")
    
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filters to obtain the horizontal and vertical gradients
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradient
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Normalize the gradient magnitude to the range [0, 255]
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Apply a threshold to the normalized gradient magnitude to obtain a binary mask
threshold = 50
gradient_mask = cv2.threshold(gradient_magnitude_normalized, threshold, 255, cv2.THRESH_BINARY)[1]

# Apply the binary mask to the original image to obtain the sharpened image
sharpened = cv2.bitwise_and(image, image, mask=gradient_mask)

# Display the sharpened image
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened)
