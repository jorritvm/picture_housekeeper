import datetime
import os
flat_folder = "D:/pictures/iphone_import_emmy"
tree_folder = flat_folder

x = input("are you sure you wish to proceed? (y/n)")
if x == "y":
    for file_name in os.listdir(flat_folder):
        file_name_full = os.path.join(flat_folder, file_name)
        if not os.path.isfile(file_name_full):
            continue
        timestamp = os.path.getmtime(file_name_full)
        dt = datetime.datetime.fromtimestamp(timestamp)

        subfolder_name = str(dt.year) + "-" + \
            str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)
        subfolder_full = os.path.join(tree_folder, subfolder_name)
        if not os.path.exists(subfolder_full):
            os.makedirs(subfolder_full)

        subfolder_name_full = os.path.join(subfolder_full, file_name)

        print("Moving %s -> %s" % (file_name_full, subfolder_name_full))
        os.rename(file_name_full, subfolder_name_full)

    print("Finished!")
else:
    print("Aborting..")
