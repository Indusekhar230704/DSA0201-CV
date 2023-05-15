import cv2

# Open the video file
video = cv2.VideoCapture("C:/Users/aspi/Downloads/The.Vampire.Diaries.[S01E06].@Netflixonline.mkv")

# Check if the video was successfully opened
if not video.isOpened():
    print("Failed to open the video file.")
    exit()

# Get the frames per second (fps) of the video
fps = video.get(cv2.CAP_PROP_FPS)

# Create two video writers for slow motion and fast motion
slow_motion_writer = cv2.VideoWriter('slow_motion.avi', cv2.VideoWriter_fourcc(*'XVID'), fps/2, (int(video.get(3)), int(video.get(4))))
fast_motion_writer = cv2.VideoWriter('fast_motion.avi', cv2.VideoWriter_fourcc(*'XVID'), fps*2, (int(video.get(3)), int(video.get(4))))

# Read and process each frame
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Display the original frame
    cv2.imshow('Original', frame)

    # Slow motion
    slow_motion_writer.write(frame)  # Write the frame to the slow motion video writer
    cv2.imshow('Slow Motion', frame)
    cv2.waitKey(int(1000 / (fps/2)))  # Delay between frames for slow motion

    # Fast motion
    fast_motion_writer.write(frame)  # Write the frame to the fast motion video writer
    cv2.imshow('Fast Motion', frame)
    cv2.waitKey(int(1000 / (fps*2)))  # Delay between frames for fast motion

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writers
video.release()
slow_motion_writer.release()
fast_motion_writer.release()

# Close all windows
cv2.destroyAllWindows()
