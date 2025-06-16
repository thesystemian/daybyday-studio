from pathlib import Path
import yaml
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

PODCAST_TITLE = "Day By Day English"
PODCAST_LINK = "https://your-website.com"
PODCAST_DESCRIPTION = "Your daily English podcast to grow slowly, day by day."
PODCAST_AUTHOR = "Dax Ricaud"

rss = Element("rss", version="2.0")
channel = SubElement(rss, "channel")
SubElement(channel, "title").text = PODCAST_TITLE
SubElement(channel, "link").text = PODCAST_LINK
SubElement(channel, "description").text = PODCAST_DESCRIPTION
SubElement(channel, "language").text = "en-us"
SubElement(channel, "managingEditor").text = f"{PODCAST_AUTHOR} (contact@your-website.com)"

episodes_path = Path("episodes")
for episode_folder in sorted(episodes_path.iterdir()):
    metadata_file = episode_folder / "metadata.yaml"
    if metadata_file.exists():
        with open(metadata_file, "r") as f:
            data = yaml.safe_load(f)

        item = SubElement(channel, "item")
        SubElement(item, "title").text = data["title"]
        SubElement(item, "description").text = data["description"]
        SubElement(item, "guid").text = episode_folder.name

        pub_date = datetime.strptime(data["date"], "%Y-%m-%d")
        SubElement(item, "pubDate").text = pub_date.strftime("%a, %d %b %Y 10:00:00 +0000")

        audio_url = f"{PODCAST_LINK}/episodes/{episode_folder.name}/{data['audio']}"
        SubElement(item, "enclosure", url=audio_url, type="audio/mpeg")

output = Path("feed.xml")
ElementTree(rss).write(output, encoding="utf-8", xml_declaration=True)
print(f"✅ RSS feed created: {output}")
