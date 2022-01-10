import datetime
from datetime import timedelta

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import jwt

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.prac1

admin_id = "Yang"
admin_pw = "123"
SECRET_KEY = 'apple'

@app.route("/login", methods=['POST'])
def login_proc():
    user_id = request.form['id']
    user_pw = request.form['pw']

    if (user_id == admin_id and user_pw == admin_pw):
        payload = {
            'id': user_id,
            'exp': datetime.utcnow() + timedelta(seconds=60)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
