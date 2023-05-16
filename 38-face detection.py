import cv2

# Load the input image
img = cv2.imread("C:/Users/aspi/Downloads/abcd.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("C:/Users/aspi/Desktop\cv/haarcascade_frontalface_default.xml")

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw bounding boxes around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output image
cv2.imshow('Faces Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
