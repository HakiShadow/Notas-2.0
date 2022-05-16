import bcrypt
from ..database.connection import DataBase as DB
from flask import redirect, session, url_for

def login(user):
    try: 
        hashAlmacenada = verify(user)
        if hashAlmacenada == '':
            return 404

        else:
            password = (user.pas).encode()
            hashAlmacenada = hashAlmacenada.encode()
            if bcrypt.checkpw(password, hashAlmacenada):
                return 200
            else:
                return 400

    except Exception as ex:
        print(ex, 'login')
        return 404

def verify(user):
    try:
        query = f'''
        SELECT pass FROM users WHERE user = '{user.user}'
        '''
        hashpass = DB.EjecutarSQL(DB, query) # Formato tupla
        hashpass = hashpass[0][0] # Formato string
        return hashpass
    
    except Exception as ex:
        print(ex, 'verify')
        hashpass = ''
        return hashpass
    
def create(user):
    try:
        # No verifico si el usuario ya existe, puesto que de existir el proceso fallaria
        hash = user.pas
        hash = hash.decode()

        query = f'''
        INSERT INTO users (user, pass) VALUES ('{user.user}', '{hash}')
        '''
        DB.EjecutarSQL(DB, query)
        return 200
        
    except Exception as ex:
            print (ex)
            return 400

def delete(user):

    try:
        query = f'''
        DELETE FROM users WHERE user = '{user.user}'
        '''
        DB.EjecutarSQL(DB, query)
        session.clear()
        return 200

    except Exception as ex:
        print (ex, 'delete ')
        return 400