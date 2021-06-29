# 1. convert all heic in a folder into jpg & keep exif
# ---> requires https://imagemagick.org/script/download.php
# --> use imazing heic converter
# 2. set jpg modified date equal to heic's
# 3. remove heic
# 4. remove .mov with same name

import os
import shutil

flat_folder = "D:/pictures/iphone_import_jorrit"

x = input("are you sure you wish to proceed? (y/n)")
if x == "y":
    all_files = os.listdir(flat_folder)
    for file_name in all_files:

        file_name_full = os.path.join(flat_folder, file_name)
        root, ext = os.path.splitext(file_name_full)

        if ext == ".heic":
            print('-----------------------')

            jpg_file = root + ".jpg"
            if os.path.exists(jpg_file):

                # copy stats onto the jpg
                print("Statcopy onto %s" % (jpg_file))
                shutil.copystat(file_name_full, jpg_file)

                # remove the heic
                print("Removing %s" % (file_name))
                os.remove(file_name_full)

            mov_file = root + ".mov"
            if os.path.exists(mov_file):

                # remove the mov
                print("Removing %s" % (mov_file))
                os.remove(os.path.join(flat_folder, mov_file))

    print("Finished!")
else:
    print("Aborting..")
