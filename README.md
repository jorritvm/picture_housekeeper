# picture_housekeeper
## What is it
Ensemble of picture archive maintenance tools

## How to use flat2tree
Will reorganise a flat folder of files into per date subfolders based on date modified.
1. set up path
2. execute

## How to use heic2jpg
1. convert all heic in a folder into jpg & keep exif - this uses imagemagick and parallel computing
2. set up path
3. execute will:
    * create jpg from existing heic
    * set jpg modified date equal to heic's
    * remove heic
    * remove .mov with same name

## How to use archiver
Folders in current folder will be zipped if the zips don't exist yet.
1. Put this python file in the folder where it has to archive the subfolders one by one
2. run the script

## How to use walkresize
Pictures in current folder and subfolders will be resized.
1. Put this python file in the folder where it has to archive the subfolders one by one
2. run the script

## How to use pic mov separator
A small script to recursively go trough a bunch of folders and put all the pictures in a subfolder called pics.
1. Put this python file in the folder where it has to start crawling
2. run the script

## How to use cleanup
List and perform cleanup actions
1. configure options in settings.py 

2. run analyse_actions.py, this will:
    * skip folders from the skiplist
    * flag empty folders for removal
    * flag certain folders for zipping (configurable)
    * flag '.' files for removal (OSX previews?)
    * flag certain file types for removal (configurable)
    * flag small files for removal
    * flag digital negatives in 'trash folders' for development
    * flag digital negatives that have been developed in 'trash folders' for removal
    * probe video files and flag the correct ones for h264 transcoding and subsequent removal of the original
    * export all actions in an excel file and open this file

3. analyse the excel file and accept actions by putting an 'x' in the first non empty column
    * if the action is inspect a manual action is needed
    * if the action is develop, manual operation in lightroom will be needed

4. run perform_actions.py