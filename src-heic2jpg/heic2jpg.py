# 1. convert all heic in a folder into jpg & keep exif - this uses imagemagick #
# 2. set jpg modified date equal to heic's
# 3. remove heic
# 4. remove .mov/.mp4 with same name and nearly same modified time

import os
import shutil
import subprocess
import multiprocessing as mp
import datetime

flat_folder = r"D:\pictures\iphone_import_emmy"


def convert_heic_to_jpg(src):
    # check for 'imagemagick'
    # try:
    #     cmd = ["which", "magick"]
    #     subprocess.check_output(cmd)
    # except Exception:
    #     print("Program 'imagemagick' not found!")
    #     return

    if src.lower().endswith(".heic"):
        pwd = os.getcwd()
        src_folder = os.path.abspath(os.path.dirname(src))
        os.chdir(src_folder)
        command = [
            "magick",
            src,
            "-set",
            "filename:base",
            "%[basename]",
            "%[filename:base].jpg",
        ]
        subprocess.call(command)
        os.chdir(pwd)


def delete_if_within_same_period(jpg_file, mov_file):
    """jpg_file, mov_file must be absolute file path"""
    jpg_modified_time = os.path.getmtime(jpg_file)
    mov_modified_time = os.path.getmtime(mov_file)

    jpg_modified_datetime = datetime.datetime.fromtimestamp(jpg_modified_time)
    mov_modified_datetime = datetime.datetime.fromtimestamp(mov_modified_time)

    time_difference = abs(jpg_modified_datetime - mov_modified_datetime)

    if time_difference.total_seconds() <= 300:  # 300 seconds = 5 minutes
        basename = os.path.basename(mov_file)
        print(f"Removing {basename}")
        os.remove(mov_file)


def delete_if_without_json(mov_file):
    """mov_file must be absolute file path"""
    json_file = mov_file + ".json"
    if not os.path.exists(json_file):
        os.remove(mov_file)


def main():
    x = input("are you sure you wish to proceed? (y/n)")
    if x != "y":
        print("Aborting..")
    else:
        print("-----------------------")
        print("Converting HEIC to JPG using parallel application of imagemagick..")
        # first do all required conversions
        all_files = os.listdir(flat_folder)
        heic_files_to_convert = list()
        for file_name in all_files:
            root, ext = os.path.splitext(file_name)
            file_name_full = os.path.join(flat_folder, file_name)
            jpg_file = root + ".jpg"
            if ext.lower() == ".heic" and not os.path.exists(jpg_file):
                heic_files_to_convert.append(file_name_full)

        # one by one
        # for heic_file in heic_files_to_convert:
        #         convert_heic_to_jpg(heic_file)

        # in parallel
        pool = mp.Pool()
        pool.map(convert_heic_to_jpg, heic_files_to_convert)

        # then do cleanup
        all_files = os.listdir(flat_folder)
        for file_name in all_files:
            file_name_full = os.path.join(flat_folder, file_name)
            root, ext = os.path.splitext(file_name_full)

            if ext.lower() == ".heic":
                print("-----------------------")

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
                    # delete_if_within_same_period(os.path.join(flat_folder, jpg_file),
                    #                              os.path.join(flat_folder, mov_file))
                    delete_if_without_json(mov_file)

                mp4_file = root + ".mp4"
                if os.path.exists(mp4_file):
                    # remove the mp4
                    # delete_if_within_same_period(os.path.join(flat_folder, jpg_file),
                    #                              os.path.join(flat_folder, mp4_file))
                    delete_if_without_json(mp4_file)

            if (
                ext.lower() == ".jpg"
                or ext.lower() == ".mov"
                or ext.lower() == ".heic"
                or ext.lower() == ".png"
            ):
                json_file = file_name_full + ".json"
                if os.path.exists(json_file):
                    # remove the json
                    print("Removing %s" % (json_file))
                    os.remove(os.path.join(json_file))

        print("Finished!")


if __name__ == "__main__":
    main()
