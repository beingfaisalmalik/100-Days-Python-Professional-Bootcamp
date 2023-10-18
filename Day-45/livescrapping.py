from bs4 import BeautifulSoup

import requests

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text,'html.parser')
article_tag = soup.find_all(name='span', class_='titleline')
print(article_tag.getText())





