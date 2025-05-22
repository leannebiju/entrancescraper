import requests
from bs4 import BeautifulSoup

def fetch_neet_updates():
    url = "https://neet.nta.nic.in"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    for tag in soup.find_all(['marquee', 'li']):
        text = tag.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["admit card", "result", "exam", "registration", "counselling"]):
            updates.append(text)
    return updates[:10]
