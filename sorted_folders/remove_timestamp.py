from PIL import Image, ImageOps
import os

# Source folder path where the images with timestamps are located
source_folder = "/home/aivid9/image99"

# Destination folder path where modified images will be saved
destination_folder = "/home/aivid9/image999"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
file_list = os.listdir(source_folder)

# Loop through each file in the source folder
for file_name in file_list:
    # Check if the file is an image (you can add more image formats if needed)
    if file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Construct the full path of the source image
        source_path = os.path.join(source_folder, file_name)
        
        # Open the image using Pillow
        image = Image.open(source_path)
        
        # Remove EXIF timestamp information by cropping the image
        image_without_timestamp = ImageOps.exif_transpose(image)
        
        # Construct the full path of the destination image
        destination_path = os.path.join(destination_folder, file_name)
        
        # Save the modified image to the destination folder
        image_without_timestamp.save(destination_path)
        print(f"Processed: {file_name}")

print("Timestamps removed from all images.")
