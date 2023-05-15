import cv2

def capture_video(display_slow_motion=False, display_fast_motion=False):
    # Open the video capture device (web camera)
    cap = cv2.VideoCapture(0)

    # Check if the capture device is successfully opened
    if not cap.isOpened():
        print("Failed to open the camera.")
        return

    # Variables for controlling the speed of video playback
    slow_motion_factor = 0.5  # Set this value to adjust the slow motion speed
    fast_motion_factor = 2.0  # Set this value to adjust the fast motion speed

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Check if the frame is successfully read
        if not ret:
            print("Failed to read frame from the camera.")
            break

        # Display the frame
        cv2.imshow("Video", frame)

        # Check if slow motion display is enabled
        if display_slow_motion:
            # Delay the display to achieve slow motion
            delay = int(1000 / (cap.get(cv2.CAP_PROP_FPS) * slow_motion_factor))
        elif display_fast_motion:
            # Delay the display to achieve fast motion
            delay = int(1000 / (cap.get(cv2.CAP_PROP_FPS) * fast_motion_factor))
        else:
            # Normal display
            delay = int(1000 / cap.get(cv2.CAP_PROP_FPS))

        # Wait for the specified delay and check if the user pressed the 'q' key to quit
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    # Release the video capture device and close the display window
    cap.release()
    cv2.destroyAllWindows()

# Example usage
capture_video(display_slow_motion=True)
