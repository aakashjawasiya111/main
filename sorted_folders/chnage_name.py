import cv2
import pytesseract
import os
import re

# Function to extract and process license plate numbers from an image
def extract_and_rename_license_plate(input_image_path, output_directory):
    # Read the input image using OpenCV
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the image
    license_plate_text = pytesseract.image_to_string(gray_image)

    # Remove non-alphanumeric characters and convert to uppercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', license_plate_text).upper()

    if cleaned_text:
        # Add '.jpg' extension to the cleaned text
        new_image_name = cleaned_text + '.jpg'

        # Construct the output file path
        output_image_path = os.path.join(output_directory, new_image_name)

        # Save the image to the output directory with the new name
        cv2.imwrite(output_image_path, image)
    else:
        print("No license plate text found in the image")

# Input directory path containing multiple image files
input_directory = "/home/aivid9/Data-Data/final_images_final"  # Replace with the path to your input directory

# Output directory path
output_directory = "/home/aivid9/Data-Data/change_name_final_images"  # Replace with the path to your output directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
file_list = os.listdir(input_directory)

for file_name in file_list:
    # Combine the directory path and file name to get the full file path
    file_path = os.path.join(input_directory, file_name)

    # Check if the file is an image (you can add more image extensions if needed)
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
        # Call the function to process each image
        extract_and_rename_license_plate(file_path, output_directory)
