import os
import json
import shutil
import datetime

folder_path = "D:/pictures/iphone_import_emmy"

def main():
    x = input("are you sure you wish to proceed? (y/n)")
    if x != "y":
        print("Aborting..")
    else:
        # look up all json files
        all_files = os.listdir(folder_path)
        json_files = list()
        for file_name in all_files:
            root, ext = os.path.splitext(file_name)
            file_name_full = os.path.join(folder_path, file_name)
            if ext.lower() == ".json":
                json_files.append(file_name_full)

        # read json files and make file-modified pairs
        info = dict()
        for json_file in json_files:
            f = open(json_file)
            js = json.load(f)
            f.close()

            key = js['title']
            val = js['photoTakenTime']['timestamp']
            info[key] = val

        # set file modified date according to date in json
        for key, val in info.items():
            fpfn = os.path.join(folder_path, key)

            if os.path.exists(fpfn):
                # update stats onto the file
                print("Set modified time as 'date taken' for file %s" % (key))
                os.utime(fpfn, (int(val), int(val)))

        print("Finished!")

if __name__ == "__main__":
    main()




