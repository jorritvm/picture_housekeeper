import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import csv

album_title = "2025 Lentefeest Manon"


# Scope needed to read photos and albums
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

def authenticate():
    print("-----starting auth-----")
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    return build('photoslibrary', 'v1', credentials=creds,static_discovery=False)


def get_album_id(service, album_title):
    albums = []
    next_page_token = None

    while True:
        results = service.albums().list(
            pageSize=50, pageToken=next_page_token
        ).execute()
        albums.extend(results.get('albums', []))
        next_page_token = results.get('nextPageToken')
        if not next_page_token:
            break

    for album in albums:
        if album['title'] == album_title:
            return album['id']
    
    return None


def list_media_items_in_album(service, album_id):
    media_items = []
    next_page_token = None

    while True:
        response = service.mediaItems().search(
            body={
                "albumId": album_id,
                "pageSize": 100,
                "pageToken": next_page_token
            }
        ).execute()

        items = response.get('mediaItems', [])
        media_items.extend(items)
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return media_items


if __name__ == '__main__':
    service = authenticate()
    print("-----auth done----")

    album_id = get_album_id(service, album_title)
    if not album_id:
        print(f"Album '{album_title}' not found.")
        exit(1)

    media_items = list_media_items_in_album(service, album_id)
    print(f"Found {len(media_items)} items.")

    # write to console and to csv
    output_file = f"_metadata for {album_title}.csv"

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "creation_time"])  # header

        for item in media_items:
            filename = item.get('filename')
            creation_time = item.get('mediaMetadata', {}).get('creationTime')
            print(f"{filename} - {creation_time}")
            writer.writerow([filename, creation_time])

