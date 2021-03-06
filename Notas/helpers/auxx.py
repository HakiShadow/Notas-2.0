from ..database.connection import DataBase as DB
from datetime import datetime

def tareaStatus(idtarea):

    query = f'''
    SELECT estado FROM tareas
    WHERE id_tareas = {idtarea};
    '''
    status = DB.EjecutarSQL(DB, query)
    status = status[0][0]
    return status

def existencia():
    query = '''
    SELECT count(*) 
    FROM information_schema.TABLES 
    WHERE (TABLE_SCHEMA = 'notas-remaster') 
    AND (TABLE_NAME = 'categorias')
    '''
    existe = DB.EjecutarSQL(DB, query)
    return existe[0][0]

def preparar(notas):

    nota = notas.nota
    estado = notas.estado

    notaSplit = nota.split() # Creamos una lista con lo que nos viene en la nota
    mayus = notaSplit[0].capitalize() # Primera palabra en mayusculas

    notaSplit.pop(0) # Quitamos la primer palabra porque estaba en minusculas
    notaSplit.insert(0, mayus)  # En el lugar anterior agregamos el elemento mayus
    nota = ' '.join(notaSplit)  # Reunimos todo y lo devolvemos
    nota = nota + '.'

    if (notas.dia is None and notas.mes is None):
        dia = datetime.today().strftime('%d')
        mes = datetime.today().strftime('%m')
    else:
        dia = str(notas.dia)
        mes = str(notas.mes)

    fecha = (mes+'/'+dia)

    nota = [nota, fecha, estado]

    return nota

def prepararCat(cat):
    nombre = cat.categoria
    catSplit = nombre.split() # Creamos una lista con el nombre de la categoria
    mayus = catSplit[0].capitalize() # Primera palabra en mayusculas

    catSplit.pop(0) # Quitamos la primer palabra porque estaba en minusculas
    catSplit.insert(0, mayus)  # En el lugar anterior agregamos el elemento mayus
    nombre = ' '.join(catSplit)  # Reunimos todo y lo devolvemos
    nombre = nombre + '.'
    return nombre

def recordarme(recordar):
    if recordar == 'on':
        check = True
    else:
        check = False
    return (check)

def selectUserID(user):
    query = f'''
    SELECT user_id FROM users WHERE user = '{user}'
    '''
    result = DB.EjecutarSQL(DB, query)
    result = result[0][0]
    return result

def selectCategoria(catId):
    query = f'''
    SELECT categoria FROM categorias WHERE idcategorias = '{catId}'
    '''
    result = DB.EjecutarSQL(DB, query)
    result = result[0][0]
    return result

