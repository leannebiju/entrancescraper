import requests
from bs4 import BeautifulSoup

def fetch_keam_updates():
    url = "https://cee.kerala.gov.in"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    updates = []
    for li in soup.select("marquee li, ul li"):
        text = li.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["keam", "admit card", "result", "exam", "counselling"]):
            updates.append(text)
    return updates[:10]