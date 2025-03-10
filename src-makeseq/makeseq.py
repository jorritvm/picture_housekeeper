# online photo albums dont sort by name but by date taken, and if that does not exist mtime
# if the naming is the correct sequence, this will overwrite the mtime and remove the exif date taken to respect that sequence
# warning: the original mtime will be lost

import os
import time
from PIL import Image
from PIL.ExifTags import TAGS


flat_folder = r"C:\pictures\2025\2025-03-08 verjaardag Giel\sel\jpeg_large"

# old method that did not work...
# def remove_exif_date_taken(file_path):
#     try:
#         with Image.open(file_path) as img:
#             # Get the EXIF data
#             exif_data = img.info.get('exif')
#             if exif_data:
#                 # Remove the date taken from the EXIF data
#                 img_without_exif = img.copy()
#                 img_without_exif.info.pop('exif', None)
#                 img_without_exif.save(file_path)
#                 print(f"Removed EXIF date taken from {file_path}")
#     except Exception as e:
#         print(f"Error processing EXIF data for {file_path}: {e}")

def remove_exif(file_path):
    try:
        with Image.open(file_path) as img:
            # Convert to RGB (to avoid issues with some JPEG modes)
            img_no_exif = Image.new(img.mode, img.size)
            img_no_exif.paste(img)

            # Save without EXIF
            img_no_exif.save(file_path, "jpeg")
            print(f"Removed EXIF from {file_path}")
    except Exception as e:
        print(f"Error processing EXIF data for {file_path}: {e}")

def update_file_mtimes(folder_path):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # List all files in the folder, sorted alphabetically
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    if not files:
        print(f"No files found in the directory '{folder_path}'.")
        return

    # Get the mtime of the first file
    first_file_path = os.path.join(folder_path, files[0])
    base_mtime = os.path.getmtime(first_file_path)

    # Update mtime for each file, incrementing by 1 second
    for index, file_name in enumerate(files):
        file_path = os.path.join(folder_path, file_name)
        remove_exif(file_path)
        new_mtime = base_mtime + index
        os.utime(file_path, (new_mtime, new_mtime))
        print(f"Updated mtime for {file_name} to {time.ctime(new_mtime)}")

if __name__ == "__main__":
    update_file_mtimes(flat_folder)
