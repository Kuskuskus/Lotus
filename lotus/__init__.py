from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from lotus.model import db, User, Compability
from lotus.horoscope import get_horoscope

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    cors = CORS(app, 
                origins = app.config['CORS_ORIGINS'],
                methods = app.config['CORS_METHODS'])
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/user', methods=['POST'])
    def get_user():
        user_req = request.get_json()
        user = User.query.get(user_req['response'][0]['id'])
        if user:
            initial_bday = user.bdate
            if user_req['response'][0]['bdate'] != initial_bday:
                user.bdate = user_req['response'][0]['bdate']
                db.session.commit()
        else:
            user = User(id=user_req['response'][0]['id'], 
                        bdate=user_req['response'][0]['bdate'],
                        horoscope=get_horoscope(user_req['response'][0]['bdate'])
                        )
            db.session.add(user)
            db.session.commit()

        response = make_response(jsonify({'user authorized': user_req['response'][0]['id']}), 200)
        return response

    @app.route('/friends', methods=['POST'])
    def friends():
        req = request.get_json()
        response = make_response(jsonify(req), 200)
        return response
    
    return app



