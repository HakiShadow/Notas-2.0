from ..database.connection import DataBase as DB

def select(id):
    query = f'''
    SELECT categoria FROM categorias
    WHERE id = {id};
    '''
    nombre = DB.EjecutarSQL(DB, query)
    nombre = nombre[0][0]
    return nombre

def selectTarea(categoria, idtarea):
    categoria = categoria.replace(" ", "")
    query = f'''
    SELECT * FROM {categoria}
    WHERE id = {idtarea};
    '''
    tarea = DB.EjecutarSQL(DB, query)
    tarea = tarea[0]
    return tarea