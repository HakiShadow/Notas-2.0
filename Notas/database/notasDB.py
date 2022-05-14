from flask import redirect, url_for
from .connection import DataBase as DB
from ..helpers import auxx
from ..routes.exceptions import Errores 


def list_all(categoria):
    try:
        query = f'''
        SELECT * FROM tareas 
        WHERE id_cat = {categoria.id} and id_user = {categoria.id_user}
        ORDER BY estado and id_tareas asc ;
        '''
        result = []
        result = DB.EjecutarSQL(DB, query)
        return result
    except Exception as ex:
        print(ex)
        return Errores.badrequest()
        
def create(categoria, notas, user):
    try:
        idCat = categoria.id
        idUser = user.id
        
        nota = auxx.preparar(notas)

        query = f'''
        INSERT INTO tareas (nota, fecha, estado, id_user, id_cat)
        VALUES ('{nota[0]}', STR_TO_DATE('{nota[1]}',"%m/%d"), '{nota[2]}', {idUser}, {idCat} )
        '''
        DB.EjecutarSQL(DB, query)

    except Exception as ex:
        print(ex)
        return ex

def delete(nota):
    try:
        query = f'''
        DELETE FROM tareas
        WHERE id_tareas = '{nota.id}'
        '''
        DB.EjecutarSQL(DB, query)
    except Exception as ex:
        print(ex)
        return ex

def status(notas):
    try:
        query = f"""
        UPDATE tareas SET estado = '{notas.estado}' WHERE id_tareas = '{notas.id}'
        """
        DB.EjecutarSQL(DB, query)
    except Exception as ex:
        print(ex)
        return ex

def update(notas, notaID):
    try:
        nota = auxx.preparar(notas)

        query = f"""
        UPDATE tareas
        SET
        nota = '{nota[0]}',
        fecha = STR_TO_DATE('{nota[1]}',"%m/%d")
        WHERE id_tareas = {notaID.id}
        """
        DB.EjecutarSQL(DB, query)
    
    except Exception as ex:
        print(ex)
        return ex
