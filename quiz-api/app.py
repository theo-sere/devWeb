from flask import Flask, request
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def HandlePayload():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	hashed = hashlib.md5(tried_password).digest()
	if hashed == b'z~"\x8d\xf1\x9d\xf5\xda\xd2\xe2\x8a+\x1f7\xaf&':
		return {"size": 0, "scores": []}, 200

if __name__ == "__main__":
    app.run()