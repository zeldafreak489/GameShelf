import requests
from django.conf import settings

BASE = getattr(settings, "RAWG_APT_BASE", "https://api.rawg.io/api")
KEY = getattr(settings, "RAWG_API_KEY", "")

def rawg_search(query, page=1, page_size=20):
    url = f"{BASE}/games"
    params = {"search": query, "page": page, "page_size": page_size}
    if KEY:
        params["key"] = KEY
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # Only return the list of games
    return data.get("results", [])

def rawg_game_detail(rawg_id):
    url = f"{BASE}/games/{rawg_id}"
    params = {}
    if KEY:
        params["key"] = KEY
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()