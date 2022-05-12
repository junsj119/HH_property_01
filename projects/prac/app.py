from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])      #get요청 api코드 #, request, jsonify 추가
def test_get():
   title_receive = request.args.get('title_give')  #title_give라는 이름으로 뭔가를 받아와서 변수로 넣고
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']                      #data: {title_give: '봄날은간다'} 값을 꺼낸다
   print(title_receive)
   return jsonify({'result':'success', 'msg': '요청을 잘 받았어요!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)