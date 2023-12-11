# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:43:01 2023

@author: Sankalp Sahu
"""

import cv2
import os

# Define a function to convert center coordinates and dimensions to min-max coordinates
def center_to_min_max(cx, cy, w, h):
    xmin = int(cx - (w / 2))
    xmax = int(cx + (w / 2))
    ymin = int(cy - (h / 2))
    ymax = int(cy + (h / 2))
    return xmin, xmax, ymin, ymax

# Input and output directories
input_dir = r"/home/aivid9/Data-Data/ANPR_cut_frame/folder_17"
output_dir = r"/home/aivid9/Data-Data/ANPR_cut_frame/crop_plate"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all files in the input directory
files = os.listdir(input_dir)

# Counter for naming the processed images
processed_image_count = 0

for file in files:
    if file.endswith(".txt"): #.txt
        # Process text files
        with open(os.path.join(input_dir, file), "r") as txt_file:
            lines = txt_file.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id, center_x, center_y, width, height = map(float, line.split())
                    print(class_id, center_x, center_y, width, height)

                    # Read the corresponding image
                    img_filename = os.path.splitext(file)[0] + ".png"
                    img_path = os.path.join(input_dir, img_filename)

                    if os.path.exists(img_path):
                        image = cv2.imread(img_path)
                        image_height, image_width, _ = image.shape
                        print("image read")

                        if image is not None:
                            # Get the min-max coordinates
                            xmin = int((center_x - width / 2) * image_width)
                            ymin = int((center_y - height / 2) * image_height)
                            xmax = int((center_x + width / 2) * image_width)
                            ymax = int((center_y + height / 2) * image_height)

                            # Crop the image
                            cropped_image = image[ymin:ymax, xmin:xmax]
                            print(cropped_image.size)

                            # Generate the output filename
                            output_filename = f"processed_image{processed_image_count}.jpg"
                            processed_image_count += 1
                            output_path = os.path.join(output_dir, output_filename)

                            # Save the cropped image
                            cv2.imwrite(output_path, cropped_image)
                        else:
                            print(f"Failed to load imxminage: {img_path}")
                    else:
                        print(f"Image not found: {img_path}")

print("Cropping and saving complete.")
