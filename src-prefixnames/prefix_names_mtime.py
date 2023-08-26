# prefix all filenames with a iso8601 mtime


import os
from datetime import datetime

flat_folder = r"U:\family\pictures\2023\2023-07-16 Denemarken\denemarken-emmy"


def main():
    x = input("are you sure you wish to proceed? (y/n)")
    if x != "y":
        print("Aborting..")
    else:
        print("-----------------------")
        print("Renaming all files with mtime prefix.")
        # first do all required conversions
        all_files = os.listdir(flat_folder)

        for file_name in all_files:
            file_name_full = os.path.join(flat_folder, file_name)
            base, ext1 = os.path.splitext(file_name)
            root, ext = os.path.splitext(file_name_full)

            if ext.lower() in [".jpg", ".mov", ".png"]:
                mtime = os.path.getmtime(file_name_full)

                # Convert the timestamp to a datetime object
                modified_datetime = datetime.fromtimestamp(mtime)

                # Format the datetime object as an ISO 8601 string
                iso8601_string = modified_datetime.isoformat().replace(":", "-")

                # rename
                new_filename = f"{iso8601_string}_{file_name}"
                new_file_path = os.path.join(flat_folder, new_filename)
                os.rename(file_name_full, new_file_path)

        print("Finished!")


if __name__ == "__main__":
    main()
