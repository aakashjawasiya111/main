import cv2
import pytesseract

# Input and output file paths
input_file = "/home/aivid9/Data-Data/final_images_final"  # Replace with the path to your input file
print("Input File:", input_file)
output_file = "/home/aivid9/Data-Data/change_name_final_images"  # Replace with the path to your output file

# Read the input image using OpenCV
image = cv2.imread(input_file)

# Convert the image to grayscale (required for OCR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use pytesseract to extract text (license plate) from the image
license_plate_text = pytesseract.image_to_string(gray_image)

# Replace non-alphanumeric characters with capital letters
license_plate_text = ''.join(char.upper() if char.isalnum() else '' for char in license_plate_text)

# If there is any text, save it to the output file
if license_plate_text:
    # Append '.jpg' to the license plate text as you mentioned
    license_plate_text += ".jpg"

    # Write the modified license plate text to the output file
    with open(output_file, 'w') as f:
        f.write(license_plate_text)
else:
    print("No license plate text found in the image")
