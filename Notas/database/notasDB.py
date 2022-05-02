from ..models.models import Notas
from .connection import DataBase as DB
from ..helpers import auxx


def list_all(notas):
    id = notas.id
    tabla = auxx.select(id)
    tabla = (tabla.title()).replace(" ", "")
    query = f'''
        SELECT * FROM {tabla} ORDER BY fecha, estado asc
        '''
    tareasDict = []
    tareasDict = DB.EjecutarSQL(DB, query)
    return tareasDict

def create(categoriaId, nota):
    id = categoriaId.id
    tablaCat = auxx.select(id)
    tablaCat=(tablaCat.title()).replace(" ", "")

    nota = nota.nota
    estado = nota.estado

    mes = str(nota.mes)
    dia = str(nota.dia)
    fecha = (mes+'/'+dia)

    sql = f'''
    INSERT INTO {tablaCat} (tarea, fecha, estado)
    VALUES ('{nota.capitalize()}', STR_TO_DATE('{fecha}',"%m/%d"), '{estado}')
    '''
    DB.EjecutarSQL(DB, sql)