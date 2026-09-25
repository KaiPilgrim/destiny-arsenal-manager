import json
from pathlib import Path

import requests


manifest_path = Path("data/raw/manifest.json")
output_path = Path("data/raw/item_definitions.json")

with manifest_path.open("r", encoding="utf-8") as file:
    manifest = json.load(file)

relative_path = (
    manifest["Response"]
    ["jsonWorldComponentContentPaths"]
    ["en"]
    ["DestinyInventoryItemDefinition"]
)

url = f"https://www.bungie.net{relative_path}"

print("Downloading Destiny inventory item definitions...")

with requests.get(url, stream=True, timeout=60) as response:
    response.raise_for_status()

    with output_path.open("wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)

size_mb = output_path.stat().st_size / (1024 * 1024)

print("Download complete")
print(f"Saved to: {output_path}")
print(f"File size: {size_mb:.2f} MB")