import sys
import shutil
import os
from os.path import join, getsize
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def main():

    # set root folders
    fromfolder = os.getcwd()
    tofolder = fromfolder+"_small"

    # set width and heigth
    w = int(input("Choose size (1600, 1280, 1024, 800, 640)"))
    if w == 1600:
        h = 1200
    if w == 1280:
        h = 1024
    elif w == 1024:
        h = 786
    elif w == 800:
        h = 600
    elif w == 640:
        h = 480

    # walk!
    for root, dirs, files in os.walk(os.getcwd()):

        for name in files:
            ext = os.path.splitext(name)[-1]

            # paths
            origfullpath = join(root, name)
            newPath = root.replace(fromfolder, tofolder)
            newFullPath = join(newPath, name)

            # create directory
            if not os.path.exists(newPath):
                os.makedirs(newPath)

            # debug print
            print("OUD - NIEUW")
            print(origfullpath)
            print(newPath)

            # IMAGE
            if ext in (".JPG", ".jpg", ".bmp", ".BMP"):
                # create existing image object
                image = QImage(origfullpath)

                # resize
                newImage = image.scaled(w, h, Qt.KeepAspectRatio, 1)

                if newImage.save(newFullPath):
                    print("success")
                else:
                    print("failed")

              # NO IMAGE
            else:
                try:
                    shutil.copy(origfullpath, newFullPath)
                except:
                    pass

            print("---------------------------")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # print QImageReader.supportedImageFormats()
    main()
    # sys.exit(app.exec_())
