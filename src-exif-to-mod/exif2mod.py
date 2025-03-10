# stores date created as date modified

import os

flat_folder = r"U:\family\pictures\2023\2023-07-16 Denemarken\sealsafari"


def main():
    x = input("are you sure you wish to proceed? (y/n)")
    if x != "y":
        print("Aborting..")
    else:
        print("-----------------------")
        print("Overwriting date modified with date created.")
        # first do all required conversions
        all_files = os.listdir(flat_folder)

        for file_name in all_files:
            file_name_full = os.path.join(flat_folder, file_name)
            root, ext = os.path.splitext(file_name_full)

            if ext.lower() == ".jpg":
                ctime = os.path.getctime(file_name_full)
                os.utime(file_name_full, (int(ctime), int(ctime)))

        print("Finished!")


if __name__ == "__main__":
    main()
