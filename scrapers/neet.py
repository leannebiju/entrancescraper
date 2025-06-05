import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def normalize(text):
    return ' '.join(text.lower().split())

def is_similar(a, b, threshold=0.85):
    return SequenceMatcher(None, a, b).ratio() > threshold

def fetch_neet_updates():
    url = "https://neet.nta.nic.in"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    seen = []

    for tag in soup.find_all("li"):
        text = tag.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["neet", "admit card", "score","result", "counselling", "exam"]):
            norm_text = normalize(text)
            if not any(is_similar(norm_text, normalize(s)) for s in seen):
                seen.append(text)
                updates.append(text)

    return updates