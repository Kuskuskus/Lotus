from lotus.model import db, User, Compability

def sync (user_id, json):
    bd_compabilities = Compability.query.filter_by(user_id=user_id)
    friends = json['response']['items']
    friends_id = list()

    for friend in friends:
        friends_id.append(friend['id'])

    for compability in bd_compabilities:
        if compability.friend.id not in friends_id:
            db.session.delete(compability)
            db.session.commit()
        else:
            friends_id.remove(compability.friend.id)



