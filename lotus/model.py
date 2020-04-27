from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bdate = db.Column(db.String, nullable=True)
    horoscope = db.Column(db.String, nullable=True)
    photo = db.Column(db.String, nullable=False)
    compability_of = db.relationship('Compability', backref = 'user', foreign_keys='[Compability.user_id]')
    compability_with = db.relationship('Compability', backref='friend', foreign_keys='[Compability.friend_id]')

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Compability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    friend_id = db.Column(db.Integer, db.ForeignKey(User.id))
    muladhara = db.Column(db.Integer, nullable = False)
    swadihshthana = db.Column(db.Integer, nullable = False)
    manipura = db.Column(db.Integer, nullable = False)
    anahatha = db.Column(db.Integer, nullable = False)
    vishuddha = db.Column(db.Integer, nullable = False)
    ajna = db.Column(db.Integer, nullable = False)
    sahasrara = db.Column(db.Integer, nullable = False)
    average = db.Column(db.Integer, nullable = False)
