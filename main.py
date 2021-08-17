import requests
from bs4 import BeautifulSoup

def user_article():
    wiki_title = input('What do you want to find on Wikipedia?\n')
    wiki_title = wiki_title.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/' + wiki_title
    ans = requests.get(url)
    if ans.status_code == 404 or ans.status_code == 403:
        print('Page not found')
    else:
        soup = BeautifulSoup(ans.text, 'html.parser')
        about_article = soup.find('div', role='note').text
        print(about_article)

def top_report():
    url = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report'
    ans = requests.get(url)
    soup = BeautifulSoup(ans.text, 'html.parser')
    top_table = soup.find('dl').table.tbody
    rows = top_table.find_all('tr')
    for i, row in enumerate(rows):
        data = row.find_all('td')
        for index, info in enumerate(data):
            if index==1:
                print(i, ': ', info.text)
                break

user_purpose = input('What do you want to find on Wikipedia? top report/my article\n')
if user_purpose=='my article':
    user_article()
else:
    top_report()