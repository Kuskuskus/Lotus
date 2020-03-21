from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, 
            origins = ['http://127.0.0.1:5000', 'http://82.148.17.124/', 'http://applotus.ru'],
            methods = ['GET', 'POST'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/friends', methods=['POST'])
def friends():
    req = request.get_json()
    response = make_response(jsonify(req), 200)
    return response


if __name__ == '__main__':
    app.run()

