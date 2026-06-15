import os
import requests
import json
import time

API_KEY = "YOUR_API_KEY"

base_url = "https://serpapi.com/search.json"

queries = ["cafe", "coffee"]

starts = [0, 20, 40, 60, 80, 100]

locations = [
    ("เมืองสระบุรี", 14.5289, 100.9101),
]

for district, lat, lon in locations:
    folder = f"data/{district}"
    os.makedirs(folder, exist_ok=True)

    for q in queries:
        for start in starts:
            print("fetch:", district, q, start)

            params = {
                "engine": "google_maps",
                "type": "search",
                "q": q,
                "ll": f"@{lat},{lon},11z",
                "nearby": "true",
                "google_domain": "google.co.th",
                "hl": "th",
                "gl": "th",
                "start": start,
                "api_key": API_KEY
            }

            response = requests.get(base_url, params=params, timeout=60)
            data = response.json()

            filename = f"{folder}/{q}_{start}_{district}.json"

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(
                    data,
                    f,
                    ensure_ascii=False,
                    indent=2
                )

            time.sleep(1)