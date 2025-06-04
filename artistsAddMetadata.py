import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Adjust this to your folder path
folder_path = r'D:/Music - HDD/Music Repository/2025 Club'

for filename in os.listdir(folder_path):
    if not filename.lower().endswith(".mp3"):
        continue

    filepath = os.path.join(folder_path, filename)
    parts = re.split(r" - ", filename.rsplit(".", 1)[0], maxsplit=1)

    if len(parts) < 2:
        print(f"Skipping: {filename} (doesn't match pattern)")
        continue

    artist = parts[0].strip()
    title = parts[1].strip()

    try:
        audio = MP3(filepath, ID3=EasyID3)
        audio['artist'] = artist
        audio['title'] = title
        audio.save()
        print(f"Updated: {filename} → Artist: {artist}, Title: {title}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")
