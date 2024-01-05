import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
URLs = ['https://interactive.aljazeera.com/aje/2018/live-results-pakistan-election-day-2018/index.html']

data = []
for url in URLs:

    results = requests.get(url,headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    data.append({
        'name': soup.find('h2', class_ = 'constituency-card__id'),
        'brand': soup.find('h3', class_ = 'constituency-card__name'),
        'ref':soup.find('div', class_ = 'constituency-card__reg-voters'),
        # 'price':soup.find('span', {'itemprop':'price'}).get('content'),
        'url':url
    })

print(data)