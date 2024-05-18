import cv2
import os
import hashlib


def extract_frames(video_path, output_folder, interval=1):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables
    frame_count = 0
    saved_count = 0
    hash_set = set()

    # Loop through video frames
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        frame_count += 1

        # Save frame if interval is reached
        if frame_count % interval == 0:
            # Calculate hash of the frame
            frame_hash = hashlib.md5(frame).hexdigest()

            # Check for duplicate frames
            if frame_hash not in hash_set:
                # Save the frame as an image
                image_path = os.path.join(output_folder, f"frame_{saved_count}.jpg")
                cv2.imwrite(image_path, frame)

                # Add frame hash to the set
                hash_set.add(frame_hash)
                saved_count += 1

    video_capture.release()


# input_path = "C:\\Users\\sivas\\OneDrive\\Desktop\\Day_videos"
# output_path = "D:\\Output_frames"
# input_files = os.listdir(input_path)
# output_files = os.listdir(output_path)
input_files = ["40", "41","42"]
output_files = ["40_Video_night","41_Video_night","42_Video_night"]

for input_video, output_video_folder in zip(input_files, output_files):
    # Example usage
    video_path = "E:\\Night Videos\\" + input_video + ".mp4"
    output_folder = "D:\\NIGHT_DATA\\" + output_video_folder
    interval = 15  # Save every 15th frame
    extract_frames(video_path, output_folder, interval)
