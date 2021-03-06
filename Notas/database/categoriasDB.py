from ..models.models import Categoria
from .connection import DataBase as DB
from ..helpers import auxx


def list_all(user):
    try:
        ID = user.id

        query = f'''
            SELECT * FROM categorias WHERE user_id = '{ID}' ORDER BY idcategorias asc
            '''
        categorias = []

    except Exception as ex:
        print(ex)
        return ex

    else:
        for record in DB.EjecutarSQL(DB, query):
            categoria = Categoria(id=record[0], categoria=record[1]) #Se genera una lista que contiene objetos!
            categorias.append(categoria)
        return categorias

def create(categoria, user):
    try:

        nombre = auxx.prepararCat(categoria)

        userID = user.id
        query = f'''
            INSERT INTO categorias (categoria, user_id)
            VALUES ('{nombre}', {userID});
            '''
        DB.EjecutarSQL(DB, query)

    except Exception as ex:
        print(ex)
        return ex

def delete(categoria):

    print(categoria.id)
    query = f"""
    DELETE FROM categorias
    WHERE idcategorias = {categoria.id}
    """
    DB.EjecutarSQL(DB, query)

def update(categoria, user):

    try: 
        id = categoria.id
        newName = categoria.categoria # Nombre que reemplazara al viejo

    except Exception as ex:
        print(ex)
        return ex

    else:
        try:
            newName = auxx.prepararCat(categoria)
            query = f"""
            UPDATE categorias 
            SET categoria = '{newName}'
            WHERE (idcategorias = {id}) and (user_id = {user.id})
            """
            DB.EjecutarSQL(DB, query)

        except Exception as ex:
            print(ex)
            return ex
