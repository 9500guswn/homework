from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/candle', methods=['POST'])
def get_candle():
    n_receive = request.form['n_give']
    c_receive = request.form['c_give']
    a_receive = request.form['a_give']
    p_receive = request.form['p_give']

    db.real_homework.insert_one({
        'n': n_receive,
        'c': c_receive,
        'a': a_receive,
        'p': p_receive,
    })
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@app.route('/candle', methods=['GET'])
def post_candle():
    candlelist=list(db.real_homework.find({},{'_id':False}))
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!','candlelist':candlelist})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
