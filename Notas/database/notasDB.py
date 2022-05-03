from .connection import DataBase as DB
from ..helpers import auxx


def list_all(notas):
    id = notas.id
    tabla = auxx.select(id)
    tabla = tabla.replace(" ", "")

    query = f'''
        SELECT * FROM {tabla} ORDER BY fecha, estado asc
        '''
    tareasDict = []
    tareasDict = DB.EjecutarSQL(DB, query)
    return tareasDict

def create(categoriaId, notas):
    categoriaId = categoriaId.id
    tablaCat = auxx.select(categoriaId)
    tablaCat = tablaCat.replace(" ", "")

    nota = notas.nota
    estado = notas.estado

    mes = str(notas.mes)
    dia = str(notas.dia)
    fecha = (mes+'/'+dia)

    query = f'''
    INSERT INTO {tablaCat} (tarea, fecha, estado)
    VALUES ('{nota.capitalize()}', STR_TO_DATE('{fecha}',"%m/%d"), '{estado}')
    '''
    DB.EjecutarSQL(DB, query)

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

def update(nota, notaID, categoria):
    categoria = auxx.select(categoria.id) # Nombre de la categoria donde se ubica la nota que queremos cambiar
    categoria = categoria.replace(" ", "")

    mes = str(nota.mes)
    dia = str(nota.dia)

    fecha = (mes+'/'+dia)
    
    query = f"""
    UPDATE {categoria} 
    SET 
    tarea = '{(nota.nota).capitalize()}',
    fecha = STR_TO_DATE('{fecha}',"%m/%d")
    WHERE id = {notaID.id}
    """
    DB.EjecutarSQL(DB, query)
