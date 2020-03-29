from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bdate = db.Column(db.String, nullable=True)
    horoscope = db.Column(db.String, nullable=True)
    compabilities = db.relationship('Compability', backref = 'user')

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Compability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    muladhara = db.Column(db.Integer, nullable = False)
    swadihshthana = db.Column(db.Integer, nullable = False)
    manipura = db.Column(db.Integer, nullable = False)
    anahatha = db.Column(db.Integer, nullable = False)
    vishuddha = db.Column(db.Integer, nullable = False)
    ajna = db.Column(db.Integer, nullable = False)
    sahasrara = db.Column(db.Integer, nullable = False)
    average = db.Column(db.Integer, nullable = False)
