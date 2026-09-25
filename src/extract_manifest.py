import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("BUNGIE_API_KEY")

url = "https://www.bungie.net/Platform/Destiny2/Manifest/"

headers = {
    "X-API-Key": api_key
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

raw_path = Path("data/raw/manifest.json")
raw_path.write_bytes(response.content)

data = response.json()

print("Status code:", response.status_code)
print("Bungie status:", data["ErrorStatus"])
print("Message:", data["Message"])
print("Raw response saved to:", raw_path)