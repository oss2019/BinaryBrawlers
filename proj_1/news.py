import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
print(response)
soup = BeautifulSoup(response.text, 'html.parser')

raw_data = soup.select(".titleline")
subtext_data = soup.select(".subtext")

collected_data = [] # We will apped dict with keys "title", "link" and "score"

for ind, item in enumerate(raw_data):
    title = item.get_text()
    link = item.find("a").get("href", None)
    score_data = subtext_data[ind].select(".score")
    if score_data:
        score = int((score_data[0].get_text()).split(" ")[0])
        collected_data.append({
            "title": title,
            "link": link,
            "score":score
        })

collected_data.sort(key=lambda x:x["score"], reverse=True)
