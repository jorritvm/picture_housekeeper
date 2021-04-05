# picture_housekeeper
## What is it
This tool takes care of my picture archive (> 250GB) cleanup.

## How to
1. configure options in settings.py 

2. run analyse_actions.py, this will:
    * skip folders from the skiplist
    * flag empty folders for removal
    * flag certain folders for zipping (configurable)
    * flag . files for removal
    * flag certain file types for removal (configurable)
    * flag small files for removal
    * flag digital negatives in 'trash folders' for development
    * flag digital negatives that have been developed in 'trash folders' for removal
    * probe video files and flag the correct ones for h264 transcoding and subsequent removal of the original
    * export all actions in an excel file and open this file

3. analyse the excel file and accept actions by putting an 'x' in the first non empty column

4. run perform_actions.py