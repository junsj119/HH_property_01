import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers) #사이트링크 넣어주기

soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number 순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis 제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis 가수

genies = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for genie in genies:
    rank = genie.select_one('td.number').text[0:2].strip()    #앞에 공통적인 부분은 다 빼고 이름부분만 뽑기
    title = genie.select_one('td.info > a.title.ellipsis').text.strip()
    if '19금' in title:
        title = title.strip('19금')
        title = title.strip()
    artist = genie.select_one('td.info > a.artist.ellipsis').text

    print(rank, title, artist)