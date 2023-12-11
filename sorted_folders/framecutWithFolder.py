import cv2
import os

# Directory path where video files are located
input_directory = '/home/aivid9/Data-Data/videoForTrim_23'
output_directory = '/home/aivid9/Data-Data/ANPR_cut_frame/folder_23'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get a list of all video files in the input directory
video_files = [f for f in os.listdir(input_directory) if f.endswith(".mp4")]

for video_filename in video_files:
    # Construct the full path to the video file
    video_path = os.path.join(input_directory, video_filename)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file {video_filename}")
        continue

    frame_count = 0
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = fps  # Extract one frame per second

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % interval == 0:
            # Save the frame as an image
            frame_filename = os.path.join(output_directory, f"ANPR_Images_{frame_count // fps}.png")
            cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    print(f"Images extracted from {video_filename} to {output_directory}")

print("All video files processed.")
