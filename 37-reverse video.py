import cv2

# Read the video file
cap = cv2.VideoCapture("C:/Users/aspi/Downloads/Slow Motion Water Droplet Falling Breaks Surface Tension and Makes Ripples in HD YouTube Video View.mp4")

# Get the total number of frames
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Start from the last frame and move backwards
current_frame = total_frames - 1

# Loop through all frames in reverse order
while current_frame >= 0:

    # Set the current frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    # Read the current frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Display the current frame
    cv2.imshow('Video in Reverse', frame)

    # Wait for a key press
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Move to the previous frame
    current_frame -= 1

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()
