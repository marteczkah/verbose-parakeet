import requests
from bs4 import BeautifulSoup

def user_article():
    print('')

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