import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.uhugw.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.ch1

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers) #사이트링크 넣어주기

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup) #- 전체 HTML 코드가 나온다

#select와 select_one 차이는 구글링  -> 1. 리스트형태로 나오냐 script? 형식으로 나오냐 차이
#그리고 하나만뽑냐 다뽑냐도 되는듯??
#즉 돌리고싶으면 select한 후 select_one으로 값 추출

##코딩 시작 #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')  #영화이름 -> 검사 -> 코드 -> 코드셀렉트
print(title)                #<a href="/movie/bi/mi/basic.naver?code=186114" title="밥정">밥정</a> 출력
#print(title.text)           #밥정 출력
#print(title['href'])        #/movie/bi/mi/basic.naver?code=186114 출력

#2, 3번째꺼의 검사코든데 공통점을 추출
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a


movies = soup.select('#old_content > table > tbody > tr')
#print(movies)           #영화제목에 관한?? HTML 전체코드 출력

for movie in movies:
    a = movie.select_one('td.title > div > a')      #앞에 공통적인 부분은 다 빼고 이름부분만 뽑기
    if a is not None:
        #print(a)        #<a href="/movie/bi/mi/basic.naver?code=147092" title="히든 피겨스">히든 피겨스</a> 이런식으로 출력

        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text

        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)


        #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img                 순위
        #old_content > table > tbody > tr:nth-child(2) > td.point                               별점
