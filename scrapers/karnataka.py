import requests
from bs4 import BeautifulSoup

def fetch_karnataka_updates():
    url = "https://cetonline.karnataka.gov.in/kea"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    for tag in soup.find_all(['a', 'li']):
        text = tag.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["cet", "kcet", "admit card", "counselling", "result"]):
            updates.append(text)
    return updates[:10]
