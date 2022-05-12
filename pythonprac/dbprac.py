#3-11
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.uhugw.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

#데이터 삽입 3가지방법

doc = {
    'name': 'qqqq',
    'age': 27
}

##users 는 컬렉션
#db.users.insert_one({'name':'john','age':20})

#doc = {'name':'bobby','age':27}
db.users.insert_one(doc)


##DB에서 전체출력
# ##all_users = list(db.users.find({})) --> 이렇게하면 데이터 앞에 아이디값?이 같이온다 그걸 없애는게 밑에코드
# all_users = list(db.users.find({}, {'_id':False}))
#
# for user in all_users:
#     print(user)

##하나만 출력
#user = db.users.find_one({'name':'bobby'})
#print(user)
#print(user['age'])

#수정
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

#삭제
#db.users.delete_one({'name':'bobby'})