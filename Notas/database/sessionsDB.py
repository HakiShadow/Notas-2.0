import imp
from ..database.connection import DataBase as DB
from ..models.models import Users
from ..helpers import auxx

def verify(user):

# el siguiente proceso podria ser simplificado con un try/except, pero lo dejare por ahora

    query = f'''
    SELECT user FROM users WHERE user = '{user.user}'
    '''
    result = DB.EjecutarSQL(DB, query)

    if result != ():
        query = f'''
        SELECT pass FROM users WHERE user = '{user.user}'
        '''
        hashpass = DB.EjecutarSQL(DB, query) # Formato tupla
        hashpass = hashpass[0][0] # Formato string
        return hashpass
    
    else:
        hashpass = ''
        return hashpass
    
def create(user):
    query = f'''
    SELECT user FROM users WHERE user = '{user.user}'
    '''
    result = DB.EjecutarSQL(DB, query)

    if result == ():
        hash = user.pas
        hash = hash.decode()

        query = f'''
        INSERT INTO users (user, pass) VALUES ('{user.user}', '{hash}')
        '''
        DB.EjecutarSQL(DB, query)

        return 200
    else:
        return 406