import requests
from bs4 import BeautifulSoup

def fetch_tnmedical_updates():
    url = "http://www.tnmedicalselection.net"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    for tag in soup.find_all(['a', 'li']):
        text = tag.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["neet", "mbbs", "result", "counselling", "application"]):
            updates.append(text)
    return updates[:10]
