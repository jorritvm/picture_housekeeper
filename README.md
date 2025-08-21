> ⚠️ **Archived Repository**  
> This project is no longer maintained. See [ARCHIVED.md](ARCHIVED.md) for details.


# picture_housekeeper

An ensemble of picture archive maintenance tools

## Overview of all modules


| Name of Operation  | Description                                                                                                | Integrated in Imagetools |
|--------------------|------------------------------------------------------------------------------------------------------------|--------------------------|
| archiver           | Folders in current folder will be zipped if the zips don't exist yet.                                      | ✅                        |
| cleanup            | Lists and performs cleanup actions (removal, zipping, flagging, exporting actions to Excel).               | ✅                        |
| created2mod        | Converts the creation date of files to the modified date.                                                  | ✅                        |
| flat2tree          | Reorganizes a flat folder of files into per-date subfolders based on date modified.                        | ✅                        |
| heic2jpg           | Converts all HEIC files in a folder to JPG, keeps EXIF, removes original HEIC and matching live MOV files. | ✅                        |
| makeseq            | Force Google to see name-based sequential order.                                                           | ✅                        |
| metadata-harvester | Overwrites downloaded Google Photos with correct metadata using the google photos API.                     | ✅                        
| picmovseparator  | Recursively moves all pictures into a subfolder called `pics`.                                             | ✅                        |
| prefix names       | Adds the mtime as prefix to all filenames.                                                                 | ✅                        |
| takeout            | Parses Google Takeout JSON files to correct the 'file modified' time of pictures.                          | ✅                        |
| walkresize         | Resizes pictures in current folder and subfolders.                                                         | ✅                        |

## How to use
See the [HOWTO.md](HOWTO.md) file for detailed instructions on how to use each operation.

## Author
Jorrit Vander Mynsbrugge
