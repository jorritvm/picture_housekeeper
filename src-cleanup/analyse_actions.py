import os
import pandas as pd
import settings as s
from helpers import get_video_meta, stringlist_pmatch_string, string_pmatch_stringlist, get_folder_size_mb, get_file_size_mb, ts

actionlist = list()

for root, dirs, files in os.walk(s.folder_to_scan):

    # skip folders that match our skiplist patterns
    if stringlist_pmatch_string(s.skip_folders_partial_match, os.path.basename(root)):
        print("skipping folder: " + root)
        dirs[:] = []
        continue

    # remove empty folders
    if not dirs and not files:
        action = {"folder": root, "file": "", "size": get_folder_size_mb(
            root, 2), "action": "remove_folder", "reason": "empty folder"}
        actionlist.append(action)
        continue

    # zip folders that match our ziplist patterns
    if stringlist_pmatch_string(s.zip_folders_partial_match, os.path.basename(root)):
        action = {"folder": root, "file": "", "size": get_folder_size_mb(
            root, 2), "action": "zip_folder", "reason": "basename matches ziplist"}
        actionlist.append(action)
        dirs[:] = []
        continue

    # hande files in this directory
    for name in files:
        fpfn = os.path.join(root, name)
        fn, fext = os.path.splitext(fpfn)
        action = None

        # if the file starts with a dot flag it for removal
        if name[0] == '.':
            action = {"action": "remove",
                      "reason": "file starts with '.'"}

        # remove specific filetypes
        elif fext.lower() in s.remove_these_filetypes:
            action = {"action": "remove",
                      "reason": "extension is flagged for removal"}

        # remove small files that aren't text or gif
        elif os.stat(fpfn).st_size / 1024 < s.small_filesize_threshold:
            if fext.lower() not in s.permitted_small_files:
                action = {"action": "remove",
                          "reason": "file very small"}

        # remove digital negatives if they are in a trash folder
        elif fext.lower() in [".cr2", ".dng", ".nef"] and ("sel_t" in root or "trash" in root):
            all_files = [os.path.join(path, name) for path, subdirs, files in os.walk(
                root) for name in files]
            if string_pmatch_stringlist(os.path.basename(fn) + ".jpg", all_files):
                action = {"action": "remove",
                          "reason": "digital negative in a trash folder"}
            else:
                action = {"action": "develop_delete",
                          "reason": "digital negative was never developed, can only be deleted after jpg is created"}

        # videofiles
        elif fext.lower() in s.extensions_that_indicate_video_files:
            meta = get_video_meta(fpfn, s.fp_ffprobe)
            if meta is None:
                action = {"action": "inspect", "reason": "file unreadable"}
            else:
                # if meta["video_codec_name"] != "h264":
                if meta['video_codec_tag_string'] == 'avc1':
                    action = {"action": "convert_delete",
                              "reason": "probably iphone6 video " + meta.__str__()}
                elif 'hvc' in meta['video_codec_tag_string']:
                    # iphone 8 is already in h265 -> do not touch this
                    pass
                else:
                    action = {"action": "convert_delete",
                              "reason": "source unknown but h264 might downsize it " + meta.__str__()}

        # compose action
        if action is not None:
            fullaction = {"folder": root,
                          "file": name,
                          "size": get_file_size_mb(fpfn, 2)}
            fullaction.update(action)
            actionlist.append(fullaction)

# write action output
df = pd.DataFrame(actionlist)

fn = s.output_filename
if s.prefix_with_timestamp:
    fn = ts() + " " + fn
fpfn = os.path.join(s.output_folder, fn)
df.to_excel(fpfn)

os.startfile(fpfn)

print("finished.")
