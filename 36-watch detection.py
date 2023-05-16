import cv2

# Load the cascade classifier
watch_cascade = cv2.CascadeClassifier("C:/Users/aspi/Desktop/cv/watch-cascade.xml")

# Load the input image
img = cv2.imread("C:/Users/aspi/Downloads/watch.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect watches in the image
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

# Draw bounding boxes around the detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output image
cv2.imshow('Watches Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



