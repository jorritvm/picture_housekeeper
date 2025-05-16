import os
import csv
import argparse
from datetime import datetime
import time

image_folder = r"C:\pictures\2025\2025-05-11 Lentefeest Manon\phone"
csv_file = r"_metadata for 2025 Lentefeest Manon.csv"

def apply_mtimes(folder_path, csv_path):
    # Read filename-to-timestamp mapping from CSV
    metadata = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row['filename']
            creation_time = row['creation_time']
            try:
                # Convert ISO timestamp to epoch
                dt = datetime.fromisoformat(creation_time.replace("Z", "+00:00"))
                epoch_time = dt.timestamp()
                metadata[filename] = epoch_time
            except Exception as e:
                print(f"Could not parse date for {filename}: {e}")

    # Walk through the folder and apply mtimes
    changed = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file in metadata:
                full_path = os.path.join(root, file)
                epoch_time = metadata[file]
                try:
                    os.utime(full_path, (epoch_time, epoch_time))  # atime, mtime
                    print(f"Updated {file} to {datetime.fromtimestamp(epoch_time)}")
                    changed += 1
                except Exception as e:
                    print(f"Failed to update {file}: {e}")

    print(f"\n✅ Done. Updated {changed} file(s).")

if __name__ == '__main__':
    apply_mtimes(image_folder, csv_file)
