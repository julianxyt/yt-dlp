import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, ID3NoHeaderError
FOLDER = 'D:/Music - HDD/Music Repository/2025 Club'
def clean_title(title):
    # Remove "[abcdefghijk]" pattern (Letters inside square brackets)
    title = re.sub(r"\[.*\]", "", title)

    # Remove "(official video)" (case-insensitive)
    title = re.sub(r"\(official .*\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(free .*\)", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\(lyric .*\)", "", title, flags=re.IGNORECASE)

    # Clean up any extra spaces, dashes
    title = re.sub(r"[-–—]\s*$", "", title).strip()
    return title.strip()

def rename_file(title, folder_path, filepath, filename):
    # Rename file to cleaned title
    new_filename = f"{title}.mp3"
    new_filepath = os.path.join(folder_path, new_filename)

    # Avoid overwriting files
    if os.path.exists(new_filepath):
        print(f"Cannot rename {filename} to {new_filename}: target exists.")
        return

    try:
        os.rename(filepath, new_filepath)
        print(f"Renamed '{filename}' → '{new_filename}'")
    except Exception as e:
        print(f"Error renaming file {filename}: {e}")

def main():
    folder_path = FOLDER  # Change this

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".mp3"):
            continue

        filepath = os.path.join(folder_path, filename)
        base_name = filename.rsplit(".", 1)[0]

        parts = re.split(r" - ", base_name, maxsplit=1)
        if len(parts) < 2:
            print(f"Skipping: {filename} (no ' - ' to split)")
            title = clean_title(base_name)
            rename_file(title, folder_path, filepath, filename)
            continue

        artist = parts[0].strip()
        title = parts[1].strip()
        title = clean_title(title)

        try:
            # Load or create ID3 tags
            try:
                audio = ID3(filepath)
            except ID3NoHeaderError:
                print(f"Problem with no ID3 tags - adding...")
                audio = ID3()
                audio.save(filepath)
                audio = EasyID3(filepath)

            audio.add(TPE1(encoding=3, text=artist))  # Artist
            audio.add(TIT2(encoding=3, text=title))   # Title

            audio.save(filepath)
            print(f"✅ Updated: {filename} → Artist: '{artist}', Title: '{title}'")
        except Exception as e:
            print(f"❌ Error updating {filename}: {e}")
        rename_file(title, folder_path, filepath, filename)

if __name__ == "__main__":
    main()