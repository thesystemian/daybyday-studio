import os
from pathlib import Path
import yaml

episode_number = input("Episode number (e.g. 01): ")
title = input("Episode title: ")
description = input("Short description: ")
date = input("Date (YYYY-MM-DD): ")

folder = Path(f"episodes/episode-{episode_number}")
folder.mkdir(parents=True, exist_ok=True)

metadata = {
    "title": title,
    "description": description,
    "date": date,
    "author": "Dax",
    "cover": "cover.png",
    "audio": "audio.mp3"
}

with open(folder / "metadata.yaml", "w") as f:
    yaml.dump(metadata, f)

print(f"✅ Episode folder created: {folder}")
