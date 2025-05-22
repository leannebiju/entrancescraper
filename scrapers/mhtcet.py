import requests
from bs4 import BeautifulSoup

def fetch_mhtcet_updates():
    url = "https://cetcell.mahacet.org"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    for tag in soup.find_all("li"):
        text = tag.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["mht", "cet", "admit card", "result", "counselling", "exam"]):
            updates.append(text)
    return updates[:10]
