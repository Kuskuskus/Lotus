from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

