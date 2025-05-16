# google photo metadata harvester
you can get metadata for your own pictures using google takeout  
you cannot get this for shared albums in which friends have added their pictures  
if you download the files in a shared album you get a zip file of pictures where every picture has a mtime = time of download  
this little tool scrapes the mtimes from google using the api, and overwrites the mtimes of the donwloaded files

## how to get a token
- Go to: Google Cloud Console
- Create or select a project.
- Navigate to APIs & Services > Library.
- Search for Google Photos Library API and enable it.
- Go to Credentials > Create Credentials > OAuth client ID:
- Application type: Desktop App
- Name: Photos API Client
- Download the credentials.json file.
- Make sure you have set yourself up as a test user.

## how to install this app
```
python -m venv venv
venv\scripts\activate.bat
pip install -r requirements.txt
```

## how to get the metadata to a csv file
- set up album title in `get_metadata.py` 
- `python get_metadata.py`

## how to write the metadata mtime to the downloaded pictures
- set `image_folder` to the folder containing the downloaded images
- set `csv_file` to the csv file to use (can be relative path)
- `python write_metadata.py`

## author
JVM

