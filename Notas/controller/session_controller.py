import bcrypt
from ..database import sessionsDB
from ..models.models import Users

def verify(user: Users):
    hash = sessionsDB.verify(user)

    if hash != '':
        return hash
    else:
        return 404


def register(user: Users):

    username = user.user

    hash = (user.pas).encode()
    sal = bcrypt.gensalt()

    hash = bcrypt.hashpw(hash, sal)

    user = Users(user = username, pas = hash)

    return sessionsDB.create(user)

def delete(user: Users):
    pass
    return sessionsDB.delete(user)

def update(user: Users):
    pass
    return sessionsDB.update(user)