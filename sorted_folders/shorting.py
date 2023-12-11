import os
import re
import shutil

# Input TXT file path
input_file_path = '/home/aivid9/Downloads/fileList.txt'

# Read folder paths from input file
with open(input_file_path, 'r') as file:
    folder_paths = file.read().splitlines()
def extract_numeric_part(folder_name):
    match = re.search(r'\d+', folder_name)
    if match:
        return int(match.group())
    else:
        return float('inf')  # Fallback for folders without numeric part

# Sort folder paths based on the numeric part of folder names
folder_paths = sorted(folder_paths, key=lambda x: extract_numeric_part(os.path.basename(x)))

# Output directory where sorted folders will be created
output_directory = 'sorted_folders'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Copy folders to the output directory with new names
for i, folder_path in enumerate(folder_paths, start=1):
    folder_name = os.path.basename(folder_path)
    folder_name = re.sub(r'^file\s+', '', folder_name)  # Remove "file " prefix if present
    folder_name = re.sub(r'[^0-9a-zA-Z_]', '_', folder_name)  # Replace non-alphanumeric characters with underscores
    new_folder_name = f'{i:04d}_{folder_name}'  # Sanitize folder name
    new_folder_path = os.path.join(output_directory, new_folder_name)
    
    # Copy the folder to the output directory
    # os.rename(folder_path, new_folder_path)


# Write the new folder paths to a new TXT file
output_file_path = '/home/aivid9/Downloads/output.txt'
with open(output_file_path, 'w') as file:
    file.write('\n'.join([os.path.basename(folder) for folder in folder_paths]))

print(f'Folders sorted and renamed. Renamed folders stored in {output_directory}')
print(f'New folder paths written to {output_file_path}')