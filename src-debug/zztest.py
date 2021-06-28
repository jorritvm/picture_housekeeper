# test to see if continue skips subdirectories
# it does in my testcase but does not seem to work in my real program :-)

import os

fpfn = "c:/users/jorrit/downloads"
for root, dirs, files in os.walk(fpfn, topdown=False):

    if os.path.basename(root) in ["skip"]:
        continue
    
    print("root:") 
    print(root)
    print("dirs:")
    print(dirs)
    print("files:")
    print(files)
