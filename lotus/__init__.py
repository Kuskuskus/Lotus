from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
from datetime import datetime, date
from flask_cors import CORS
from lotus.model import db, User, Compability
from lotus.horoscope import get_horoscope
from lotus.biorhythms import chakras_compability

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
        global user_req
        correct = True
        user_req = request.get_json()
        user = User.query.get(user_req['response'][0]['id'])
        if user:
            initial_bday = user.bdate
            if user_req['response'][0]['bdate'] != initial_bday:
                user.bdate = user_req['response'][0].get('bday')
                user.horoscope = get_horoscope(user_req['response'][0].get('bday'))
                db.session.commit()
            response = make_response(jsonify({'user authorized': user.id}), 200)
        else:
            try:
                    datetime.strptime(user_req['response'][0].get('bdate'), '%d.%m.%Y') 
               
            except(ValueError, TypeError):
                    correct = False
            
            if correct:
                user = User(id=user_req['response'][0]['id'], 
                            bdate=user_req['response'][0]['bdate'],
                            horoscope=get_horoscope(user_req['response'][0]['bdate'])
                            )
                db.session.add(user)
                db.session.commit()
                response = make_response(jsonify({'user authorized': user_req['response'][0]['id']}), 200)
            else:
                user = User(id=user_req['response'][0]['id'], 
                            bdate=None,
                            horoscope=None
                            )
                db.session.add(user)
                db.session.commit()
                response = make_response(jsonify({'missing bdate': user_req['response'][0]['id']}), 400)
        
        return response


    @app.route('/friends', methods=['POST'])
    def friends():
        global friends_req
        friends_req = request.get_json()
        for friend in friends_req['response']['items']:
            correct = True
            friend_in_db = User.query.get(friend['id'])
            if friend_in_db:
                if friend.get('bdate') != friend_in_db.bdate:
                    friend_in_db.bdate = friend.get('bdate')
                    friend_in_db.horoscope = get_horoscope(friend.get('bdate'))
            else:
                try:
                    datetime.strptime(friend.get('bdate'), '%d.%m.%Y') 
               
                except(ValueError, TypeError):
                    correct = False

                if correct:
                    new_friend = User(id=friend['id'], 
                                     bdate=friend['bdate'],
                                     horoscope=get_horoscope(friend['bdate'])
                                     ) 
                    db.session.add(new_friend)

                    chakras = chakras_compability(user_req['response'][0]['bdate'], friend['bdate'])
                    compability = Compability(user_id=user_req['response'][0]['id'],
                                              friend_id=friend['id'],
                                              muladhara=chakras['muladhara'],
                                              swadihshthana=chakras['swadihshthana'],
                                              manipura=chakras['manipura'],
                                              anahatha=chakras['anahatha'],
                                              vishuddha=chakras['vishuddha'],
                                              ajna=chakras['ajna'],
                                              sahasrara=chakras['sahasrara'],
                                              average=chakras['average']
                                              )
                    db.session.add(compability)
                    db.session.commit()
                else:
                     new_friend = User(id=friend['id'], 
                                     bdate=None,
                                     horoscope=None
                                     ) 
                     db.session.add(new_friend)
                     db.session.commit() 

    return redirect(url_for('rating'))

    @app.route('/rating')
    def rating():
        return render_template('rating.html')
    
    return app



