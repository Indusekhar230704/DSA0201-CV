import cv2

# Load the image
img = cv2.imread("C:/Users/aspi/Downloads/spiderman.png")

# Define the ROI parameters
x, y = 100, 100
width, height = 200, 150

# Extract the ROI
roi = img[y:y+height, x:x+width]

# Display the ROI
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
