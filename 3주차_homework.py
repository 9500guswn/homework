<달달한 맛>
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
song=soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for list in song:
    rank=list.select_one('td.number').text[0:2].strip()
    title=list.select_one('td.info > a.title.ellipsis').text.strip()
    singer=list.select_one('a.artist.ellipsis').text

    print(rank,title,singer)