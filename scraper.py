import requests
from bs4 import BeautifulSoup
import json

sujood = "https://www.sujood.co"
content = requests.get(sujood).content
soup = BeautifulSoup(content, 'lxml')

prayers = soup.find_all('div', class_="prayer")

prayers_json = []

for prayer in prayers:
    data_id = prayer.get('data-id')
    category = prayer.get('category')
    title = prayer.find('h1', class_="prayer-title").text.replace("&quot;",
                                                                  '').replace('\n            \"', '').replace('\"\n        ', '')
    arabic = prayer.find('p', class_="arabic").text.strip()
    transliteration = prayer.find('p', class_="transliteration").text.strip()
    translation = prayer.find('p', class_="translation").text.strip()

    prayers_json.append({
        'data_id': int(data_id),
        'category': category,
        'title': title,
        'arabic': arabic,
        'transliteration': transliteration,
        'translation': translation
    })

sorted_prayers = sorted(prayers_json, key=lambda x: x['data_id'])

with open('sujood.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_prayers, f)
