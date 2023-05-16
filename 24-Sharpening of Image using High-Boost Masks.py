import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")

# Apply a Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Subtract the blurred image from the original image to get the high-frequency components
high_freq = cv2.subtract(image, blurred)

# Scale the high-frequency components
scaled_high_freq = cv2.multiply(high_freq, 2)

# Add the scaled high-frequency components to the original image to produce the sharpened image
sharpened = cv2.add(image, scaled_high_freq)

# Display the sharpened image
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened)
