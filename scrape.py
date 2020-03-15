#this is from a youtube video Build a Python App That Tracks Amazon Prices!
#Dev Ed

import requests
from bs4 import BeautifulSoup

URL = 'https://veronamercato.it/it/references-list/'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

title = soup.find()
#then you need to specify exactly the tags you want

#you define a mail SMTP server and logins

#and finally while true you let it run forever??
