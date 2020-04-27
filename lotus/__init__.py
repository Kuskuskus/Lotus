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
        correct = True
        user_req = request.get_json()
        user = User.query.get(user_req['response'][0]['id'])
        if user:
            if user_req['response'][0]['bdate'] != user.bdate:
                user.bdate = user_req['response'][0].get('bdate')
                user.horoscope = get_horoscope(user_req['response'][0].get('bdate'))
            if user_req['response'][0]['photo_50'] != user.photo:
                user.photo = user_req['response'][0]['photo_50']
            if user_req['response'][0]['first_name']+' '+user_req['response'][0]['last_name'] != user.name:
                user.name = user_req['response'][0]['first_name']+' '+user_req['response'][0]['last_name']
            db.session.commit()
            response = make_response(jsonify({'user authorized': user.id}), 200)
        else:
            try:
                    datetime.strptime(user_req['response'][0].get('bdate'), '%d.%m.%Y') 
               
            except(ValueError, TypeError):
                    correct = False
            
            if correct:
                user = User(id=user_req['response'][0]['id'], 
                            name=user_req['response'][0]['first_name']+' '+user_req['response'][0]['last_name'],
                            bdate=user_req['response'][0]['bdate'],
                            horoscope=get_horoscope(user_req['response'][0]['bdate']),
                            photo=user_req['response'][0]['photo_50']
                            )
                db.session.add(user)
                db.session.commit()
                response = make_response(jsonify({'user authorized': user_req['response'][0]['id']}), 200)
            else:
                response = make_response(jsonify({'missing bdate': user_req['response'][0]['id']}), 400)
        
        return response


    @app.route('/friends', methods=['POST', 'GET'])
    def friends():
        friends_req = request.get_json()
        user = User.query.get(friends_req['response']['items'][-1])
        del friends_req['response']['items'][-1]

        for friend in friends_req['response']['items']:
            correct = True
            friend_in_db = User.query.get(friend['id'])
        
            try:
                datetime.strptime(friend.get('bdate'), '%d.%m.%Y') 
               
            except(ValueError, TypeError):
                correct = False

            if correct:

                if friend_in_db:
                    if friend.get('bdate') != friend_in_db.bdate:
                        friend_in_db.bdate = friend.get('bdate')
                        friend_in_db.horoscope = get_horoscope(friend.get('bdate')) 
                        #добавить обновление совместимости
                    if friend['photo_50'] != friend_in_db.photo:
                        friend_in_db.photo = friend['photo_50']  
                    if friend['first_name']+' '+friend['last_name'] != friend_in_db.name:
                        friend_in_db.name = friend['first_name']+' '+friend['last_name']                      
                    db.session.commit()
                else:
                    new_friend = User(id=friend['id'], 
                                      name=friend['first_name']+' '+friend['last_name'],   
                                      bdate=friend['bdate'],
                                      horoscope=get_horoscope(friend['bdate']),
                                      photo=friend['photo_50']
                                     ) 
                    db.session.add(new_friend)

                    chakras = chakras_compability(user.bdate, friend['bdate'])
                    compability = Compability(user_id=user.id,
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
        response = make_response(jsonify(friends_req), 200)
        return response


    @app.route('/rating/<int:user_id>')
    def rating(user_id):
        compabilities = Compability.query.filter_by(user_id=user_id).order_by(Compability.average.desc()).all()
        return render_template('rating.html', compabilities=compabilities)    
    return app



