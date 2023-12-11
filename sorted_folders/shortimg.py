import os
import shutil

# Define the source folder where the images are located
source_folder = '/home/aivid9/image99'

# Define the destination folder where you want to move the matching images
destination_folder = '/home/aivid9/image999'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
file_list = os.listdir(source_folder)

# Iterate through the files and move those with names starting with 'rawImg_'
for filename in file_list:
    if filename.startswith('rawImg_'):
        source_file_path = os.path.join(source_folder, filename)
        destination_file_path = os.path.join(destination_folder, filename)
        
        # Move the file to the destination folder
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved {filename} to {destination_folder}")

print("Done! All matching images have been moved.")
