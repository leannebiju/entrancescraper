import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def normalize(text):
    return ' '.join(text.lower().split())

def is_similar(a, b, threshold=0.85):
    return SequenceMatcher(None, a, b).ratio() > threshold

def fetch_keam_updates():
    url = "https://cee.kerala.gov.in"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    seen = []

    for li in soup.select("marquee li, ul li"):
        text = li.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["keam", "admit card", "score","result", "exam", "counselling"]):
            norm_text = normalize(text)
            if not any(is_similar(norm_text, normalize(existing)) for existing in seen):
                seen.append(text)
                updates.append(text)

    return updates