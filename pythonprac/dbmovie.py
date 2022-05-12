from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.uhugw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

#movie = db.movies.find_one({'title':'가버나움'})
#print(movie['star']) 가버나움의 평점이 나온다

# star = movie['star']
# all_movies = list(db.movies.find({'star':star}, {'_id':False}))
# for m in all_movies:
#     print(m['title'])

#db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})

all_users = list(db.movies.find({}, {'_id':False}))

for user in all_users:
    print(user)