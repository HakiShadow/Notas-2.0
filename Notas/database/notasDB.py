from flask import redirect, url_for
from .connection import DataBase as DB
from ..helpers import auxx
from ..routes.exceptions import Errores 


def list_all(categoria):

    try:
        query = f'''
        SELECT * FROM tareas WHERE id_cat = {categoria.id} and id_user = {categoria.id_user} ;
        '''
        result = []
        result = DB.EjecutarSQL(DB, query)
        return result
    except Exception as ex:
        print(ex)
        return Errores.badrequest()
        
def create(categoriaId, notas):

    try:
        categoriaId = categoriaId.id
        tablaCat = auxx.select(categoriaId)
        tablaCat = tablaCat.replace(" ", "")

        nota = auxx.preparar(notas)

        query = f'''
        INSERT INTO {tablaCat} (tarea, fecha, estado)
        VALUES ('{nota[0]}', STR_TO_DATE('{nota[1]}',"%m/%d"), '{nota[2]}')
        '''
        DB.EjecutarSQL(DB, query)

    except Exception as ex:
        print(ex)
        return ex

def delete(categoriaId, notaId):
    categoriaId = categoriaId.id
    notaId = notaId.id

    categoriaName = auxx.select(categoriaId)
    categoriaName = categoriaName.replace(" ", "")

    query = f'''
    DELETE FROM {categoriaName}
    WHERE id = '{notaId}'
    '''
    DB.EjecutarSQL(DB, query)

def status(categoria, notas):
    
    categoria = categoria.replace(" ", "")

    query = f"""
    UPDATE {categoria} SET estado = '{notas.estado}' WHERE id = '{notas.id}'
    """
    DB.EjecutarSQL(DB, query)

def update(notas, notaID, categoria):

    try:
        categoria = auxx.select(categoria.id) # Nombre de la categoria donde se ubica la nota que queremos cambiar
        categoria = categoria.replace(" ", "")

        nota = auxx.preparar(notas)

        query = f"""
        UPDATE {categoria} 
        SET
        tarea = '{nota[0]}',
        fecha = STR_TO_DATE('{nota[1]}',"%m/%d")
        WHERE id = {notaID.id}
        """
        DB.EjecutarSQL(DB, query)
    
    except Exception as ex:
        print(ex)
        return ex


