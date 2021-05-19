# define application wide configuration variables
folder_to_scan = "d:/pictures"

skip_folders_partial_match = ["LRCatalog", "wrapup", "iphone_import_"]
zip_folders_partial_match = ["web"]
small_filesize_threshold = 10  # in KB
permitted_small_files = [".txt", ".gif"]
remove_these_filetypes = [".py", ".thm"]

extensions_that_indicate_video_files = [
    ".avi", ".mov", ".ts", ".mp4", ".mkv", ".webv"]

fp_ffprobe = "C:/Program Files/ffmpeg/bin/ffprobe.exe"

output_folder = "../output"
output_filename = "actionlist_output.xlsx"
prefix_with_timestamp = True

zip7_path = "C:/Program Files/7-Zip/7z.exe"
# compression options are: "copy" "fastest" "fast" "normal" "maximum" "ultra"
compression_level = "maximum"
compression_levels = {"copy": "-mx0",
                      "fastest": "-mx1",
                      "fast": "-mx3",
                      "normal": "-mx5",
                      "maximum": "-mx7",
                      "ultra": "-mx9"}


fp_ffmpeg = "C:/Program Files/ffmpeg/bin/ffmpeg.exe"
