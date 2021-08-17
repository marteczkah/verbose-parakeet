import requests
from bs4 import BeautifulSoup

wiki_title = input('What do you want to find on Wikipedia?\n')
wiki_title = wiki_title.replace(' ', '_')
url = 'https://en.wikipedia.org/wiki/' + wiki_title
print(url)

ans = requests.get(url)

if ans.status_code == 404 or ans.status_code == 403:
    print('Page not found')
else:
    soup = BeautifulSoup(ans.text, 'html.parser')
    about_article = soup.find('div', role='note').text
    print(about_article)