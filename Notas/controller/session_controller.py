import bcrypt
from ..database import sessionsDB
from ..models.models import Users

def login(user: Users):
    return sessionsDB.login(user)

def register(user: Users):
    username = user.user

    sal = bcrypt.gensalt()
    hash = (user.pas).encode()

    hash = bcrypt.hashpw(hash, sal)

    user = Users(user = username, pas = hash)
    return sessionsDB.create(user)

def delete(user: Users):
    coincide = sessionsDB.login(user)
    if coincide == 200:
        return sessionsDB.delete(user)
    else:
        return 400

def update(user: Users):
    pass
    return sessionsDB.update(user)