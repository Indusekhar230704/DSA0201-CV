#cropping
import cv2
import numpy as np
 
image = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")
print(image.shape) # Print image shape
cv2.imshow("original", image)
imageCopy = image.copy()

cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)
 
cv2.imshow('image', image)
cv2.imshow('image copy', imageCopy)
 
# Cropping an image
cropped_image = image[80:280, 150:330]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()






#coping&pasting
import cv2

# Load images
img1 = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")
img2 = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")

# Crop a region of interest (ROI) from img1
roi = img1[100:300, 200:400]

# Copy the ROI into img2 at a specified location
x_offset = 50
y_offset = 100
img2[y_offset:y_offset+roi.shape[0], x_offset:x_offset+roi.shape[1]] = roi

# Display the resulting image
cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


