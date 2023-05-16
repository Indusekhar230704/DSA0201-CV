import cv2

# Load the pre-trained classifier
car_cascade = cv2.CascadeClassifier("C:/Users/aspi/Desktop/cv/cars.xml")

# Open the video capture
cap = cv2.VideoCapture("C:/Users/aspi/Downloads/istockphoto-1392540611-640_adpp_is.mp4")

while True:
    # Read the frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw bounding boxes around the detected cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
