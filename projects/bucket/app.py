from flask import Flask, render_template, request, jsonify
import certifi

ca = certifi.where()


app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.uhugw.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({}, {'_id':False}))
    count = len(bucket_list) + 1    #len()함수 ->list의 개수

    doc = {
        'num':count,
        'bucket':bucket_receive,
        'done':0,
    }
    db.bucket.insert_one(doc)

    return jsonify({'msg': '연결 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give'] # 서버로 와서 receive에 들어오게 되면 숫자도 문자열로 바뀜

    db.bucket.update_one({'num':int(num_receive)},{'$set':{'done':1}})   #num에 넘겨받은 값에 해당하는 애의 done을 1로 업데이트

    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket/done/cancel", methods=["POST"])
def bucket_done_cancel():
    num_receive = request.form['num_give'] # 서버로 와서 receive에 들어오게 되면 숫자도 문자열로 바뀜

    db.bucket.update_one({'num':int(num_receive)},{'$set':{'done':0}})   #num에 넘겨받은 값에 해당하는 애의 done을 1로 업데이트

    return jsonify({'msg': '버킷 취소완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id':False}))
    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)