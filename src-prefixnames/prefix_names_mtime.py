# prefix all filenames with a iso8601 mtime

import os
from datetime import datetime


base_folder = r"U:\family\pictures\2024\_2024-05 Gevelwerken Mabrick uitvoering"


def main(base_folder):
    x = input("are you sure you wish to proceed? (y/n)")
    if x.lower() != "y":
        print("Aborting..")
        return  # early exit!

    print("-----------------------")
    print("Renaming all files with mtime prefix.")
    # first do all required conversions
    all_files = os.listdir(base_folder)

    for old_file_name in all_files:
        old_file_path = os.path.join(base_folder, old_file_name)
        _, ext = os.path.splitext(old_file_name)

        if ext.lower() in [".jpg", ".mov", ".png"]:
            mtime = os.path.getmtime(old_file_path)

            # Convert the timestamp to a datetime object
            modified_datetime = datetime.fromtimestamp(mtime)

            # Format the datetime object as an ISO 8601 string
            iso8601_string = modified_datetime.isoformat().replace(":", "-")

            # rename
            new_file_name = f"{iso8601_string}_{old_file_name}"
            new_file_path = os.path.join(base_folder, new_file_name)
            # print(f"OLD: {old_file_name}\nNEW: {new_file_name}\n--------------")
            os.rename(old_file_path, new_file_path)

    print("Finished!")


if __name__ == "__main__":
    main(base_folder)
