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
            SELECT * FROM categorias ORDER BY id asc
            '''
        categorias = []
        for record in DB.EjecutarSQL(DB, query):
            categoria = Categoria(id=record[0], categoria=record[1]) #Se genera una lista que contiene objetos!
            categorias.append(categoria)
        return categorias

def create(categoria):
    try:
        nombre = (categoria.categoria).capitalize()
        query = f'''
            INSERT INTO categorias (categoria)
            VALUES ('{nombre}');
            '''
        DB.EjecutarSQL(DB, query)

    except Exception as ex:
        print(ex)
        return ex
    
    else:
        try:
            nombreTabla = nombre.replace(" ", "") # Retiramos los espacios para que pueda almacenarse en la BD

            query = f''' 
                CREATE TABLE {nombreTabla} (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                tarea VARCHAR(500) NOT NULL,
                fecha DATE NOT NULL,
                estado BOOLEAN NOT NULL
                )'''
            DB.EjecutarSQL(DB, query)

        except Exception as ex: # En caso que la creación de la tabla falle, 
                                # borramos la categoria, de modo que no quede uno sin otro
            print(ex)
            query = f"""
                DELETE FROM categorias
                WHERE categoria = '{nombre.capitalize()}'
                """
            DB.EjecutarSQL(DB, query)
            return ex

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

    try: 
        id = categoria.id
        oldName = auxx.select(id)  # Nombre actual de la categoria y que se debe cambiar
        newName = categoria.categoria # Nombre que reemplazara al viejo

    except Exception as ex:
        print(ex)
        return ex

    else:
        try:
            query = f"""
            UPDATE categorias 
            SET categoria = '{newName.capitalize()}'
            WHERE categoria = '{oldName.capitalize()}'
            """
            DB.EjecutarSQL(DB, query)

        except Exception as ex:
            print(ex)
            return ex
        
        else:
            try:
                newName2 = newName.replace(" ", "")
                oldName2 = oldName.replace(" ", "")
        
                query = f"""
                ALTER TABLE {oldName2} 
                RENAME TO {newName2};
                """
                DB.EjecutarSQL(DB, query)

            except Exception as ex:
                print(ex)

                query = f"""
                UPDATE categorias 
                SET categoria = '{oldName.capitalize()}'
                WHERE categoria = '{newName.capitalize()}'
                """
                DB.EjecutarSQL(DB, query)
                
                # En caso de un problema, restauramos lo que ya se habia creado
                return ex
