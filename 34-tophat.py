import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/aspi/Downloads/spiderman.png", cv2.IMREAD_GRAYSCALE)

# Create a structuring element
kernel = np.ones((5,5), np.uint8)

# Apply top hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the result
cv2.imshow("Original", img)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
