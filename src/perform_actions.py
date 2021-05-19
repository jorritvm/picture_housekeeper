import pandas as pd
import settings as s
import os
from os.path import basename
import sys
import shutil
from helpers import ask_filepath, compress_folder_with_7z

# fpfn = ask_filepath(s.output_folder)
fpfn = "D:/dev/python/picture_housekeeper/output/2021-05-19-23-34-28 actionlist_output.xlsx"
df = pd.read_excel(fpfn, index_col=0)

for i in range(df.shape[0]):
    # for i in range(25):
    if df.iloc[i].loc["perform"] != "x":
        continue

    action = df.iloc[i].loc["action"]

    if action == "remove":
        fp = os.path.join(df.iloc[i].loc["folder"], df.iloc[i].loc["file"])
        if os.path.exists(fp):
            try:
                os.remove(fp)
            except:
                e = sys.exc_info()[0]
                print(e)
            df.at[i, 'perform'] = ""

    if action == "zip_folder":
        fp = df.iloc[i].loc["folder"]
        compression_switch = s.compression_levels[s.compression_level]
        compress_folder_with_7z(fp, compression_switch, s.zip7_path)
        df.at[i, 'perform'] = ""
        # action = "remove_folder" # this way we delete the folder when it is zipped

    if action == "remove_folder":
        fp = df.iloc[i].loc["folder"]
        try:
            shutil.rmtree(fp)
        except:
            e = sys.exc_info()[0]
            print(e)
        df.at[i, 'perform'] = ""


df.to_excel(fpfn)
os.startfile(fpfn)

print("finished!")
