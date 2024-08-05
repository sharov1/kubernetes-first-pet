from flask import Flask
import os

app = Flask(__name__)

message = os.getenv('MESSAGE', 'Hello world!')

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return message

@app.route('/check', methods=['GET'])
def health_check():
    return "OK BOSS", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1024)
