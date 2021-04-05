# define application wide configuration variables
folder_to_scan = "U:/family/pictures"

skip_folders_partial_match = ["LRCatalog", "wrapup", "web", "iphone_import_"]
zip_folders_partial_match = ["web"]
small_filesize_threshold = 10 # in KB
permitted_small_files = [".txt", ".gif"]
remove_these_filetypes = [".py", ".thm"]

extensions_that_indicate_video_files = [".avi", ".mov", ".ts", ".mp4", ".mkv", ".webv"]

zip7_path = "C:/Program Files/7-Zip/7z.exe"
compression = "maximum" # options are: "copy" "fastest" "fast" "normal" "maximum" "ultra"

fp_ffprobe = "C:/Program Files/ffmpeg/bin/ffprobe.exe"

output_folder = "output"
output_filename = "actionlist_output.xlsx"
prefix_with_timestamp = True
