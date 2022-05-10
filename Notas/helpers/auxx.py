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

def existencia():
    query = '''
    select count(*) 
    FROM information_schema.TABLES 
    WHERE (TABLE_SCHEMA = 'tareas') 
    AND (TABLE_NAME = 'categorias')
    '''
    existe = DB.EjecutarSQL(DB, query)
    return existe[0][0]

def preparar(notas):

    nota = notas.nota
    dia = notas.dia
    mes = notas.mes
    estado = notas.estado

    notaSplit = nota.split() # Creamos una lista con lo que nos viene en la nota
    mayus = notaSplit[0].capitalize() # Primera palabra en mayusculas

    notaSplit.pop(0) # Quitamos el primer elemento porque estaba en minusculas
    notaSplit.insert(0, mayus)  # En el lugar anterior agregamos el elemento mayus
    nota = ' '.join(notaSplit)  # Reunimos todo y lo devolvemos
    nota = nota + '.'


    mes = str(notas.mes)
    dia = str(notas.dia)
    fecha = (mes+'/'+dia)

    nota = [nota, fecha, estado]

    return nota

def recordarme(recordar):
    if recordar == 'on':
        check = True
    else:
        check = False
    return (check)