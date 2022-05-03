from ..models.models import Categoria
from .connection import DataBase as DB
from ..helpers import auxx

def list_all():
    if auxx.existencia() == 0: # En caso que sea la primera vez usando la app, se creara por unica vez la tabla principal
        query = '''
        CREATE TABLE categorias (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        categoria VARCHAR(50) NOT NULL UNIQUE
        )
        '''
        DB.EjecutarSQL(DB, query)
        listo = 'Recien creada'
        return listo
    else:
        query = '''
            SELECT * FROM categorias
            '''
        categorias = []
        for record in DB.EjecutarSQL(DB, query):
            categoria = Categoria(id=record[0], categoria=record[1]) #Se genera una lista que contiene objetos!
            categorias.append(categoria)
        return categorias

def create(categoria):
    nombre = (categoria.categoria).capitalize()
    
    query = f'''
        INSERT INTO categorias (categoria)
        VALUES ('{nombre}');
        '''
    DB.EjecutarSQL(DB, query)

    nombre = nombre.replace(" ", "") # Retiramos los espacios para que pueda almacenarse en la BD

    query = f''' 
        CREATE TABLE {nombre} (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        tarea VARCHAR(500) NOT NULL,
        fecha DATE NOT NULL,
        estado BOOLEAN NOT NULL
        )'''
    DB.EjecutarSQL(DB, query)

def delete(categoria):
    id = categoria.id
    nombre = auxx.select(id)

    query = f"""
    DELETE FROM categorias
    WHERE categoria = '{nombre.capitalize()}'
    """
    DB.EjecutarSQL(DB, query)

    nombre = nombre.replace(" ", "") # Retiramos los espacios para que pueda almacenarse en la BD

    query = f"""
    DROP TABLE {nombre}
    """
    DB.EjecutarSQL(DB, query)
    
def update(categoria):
 
    id = categoria.id
    oldName = auxx.select(id)  # Nombre actual de la categoria y que se debe cambiar
    newName = categoria.categoria # Nombre que reemplazara al viejo

#-------------------
 
    query = f"""
    UPDATE categorias 
    SET categoria = '{newName.capitalize()}'
    WHERE categoria = '{oldName.capitalize()}'
    """
    DB.EjecutarSQL(DB, query)

    newName = newName.replace(" ", "")
    oldName = oldName.replace(" ", "")
     
    query = f"""
    ALTER TABLE {oldName} 
    RENAME TO {newName};
    """
    DB.EjecutarSQL(DB, query)