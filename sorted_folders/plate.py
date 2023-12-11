import os
import cv2

# Input and output folder paths
input_folder = "/home/aivid9/Data-Data/Final_images"  # Replace with the path to your input folder
output_folder = "/home/aivid9/Data-Data/final_images_final"  # Replace with the path to your output folder

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to process images
def process_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            # Add code to detect license plate and crop it (You may need to use OCR for plate detection)
            # For example, you can use OpenALPR or EasyOCR for plate detection and cropping
            
            # Once you have the cropped license plate image
            # Save it to the output folder
            plate_x = 100  # X-coordinate of the top-left corner of the plate
            plate_y = 200  # Y-coordinate of the top-left corner of the plate
            plate_width = 300  # Width of the plate
            plate_height = 100  # Height of the plate
            cropped_plate_image = image[plate_y:plate_y+plate_height, plate_x:plate_x+plate_width]

            plate_output_path = os.path.join(output_folder, f"cropped_{filename}")
            cv2.imwrite(plate_output_path,cropped_plate_image)
            
            print(f"Processed {filename}")

# Call the function to process images
process_images(input_folder, output_folder)
