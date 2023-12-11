import os
import cv2
import shutil

# Source folder path where the images are located
source_folder = "/home/aivid9/image99"

# Destination folder path where modified images will be saved
destination_folder = "/home/aivid9/image999"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
file_list = os.listdir(source_folder)

# Initialize a dictionary to store image file names with their corresponding bounding box numbers
image_dict = {}

# Loop through each file in the folder
for file_name in file_list:
    # Check if the file is an image (you can add more image formats if needed)
    if file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Extract the bounding box number from the file name
        parts = file_name.split("_")
        if len(parts) >= 2:
            bounding_box_number = parts[-1].split(".")[0]
            image_dict[file_name] = bounding_box_number

# Loop through the dictionary to compare and rename images
for img_name, bounding_box_number in image_dict.items():
    if img_name.startswith("Img_"):
        raw_img_name = img_name.replace("Img_", "rawImg_")
        for other_img_name, other_bounding_box_number in image_dict.items():
            if other_img_name.startswith("rawImg_") and other_bounding_box_number == bounding_box_number:
                # Rename the raw image with bounding box number
                new_raw_img_name = raw_img_name
                os.rename(os.path.join(source_folder, other_img_name), os.path.join(destination_folder, new_raw_img_name))
                print(f"Renamed and moved: {other_img_name} to {new_raw_img_name}")
                break

print("Image comparison and renaming completed.")
