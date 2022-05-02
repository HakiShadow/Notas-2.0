from ..database import categoriasDB
from ..models.models import Categoria

def lists():
    return categoriasDB.list_all()

def create(categoria: Categoria) -> Categoria:
    # categoria es una instancia de la clase Categoria, por ende un objeto
    # En este caso, el controlador solo es un intermediario
    return categoriasDB.create(categoria)

def delete(categoria: Categoria) -> Categoria:
    return categoriasDB.delete(categoria)

def update(categoria: Categoria) -> Categoria:
    return categoriasDB.update(categoria)

def details(categoria: Categoria) -> Categoria:
    return categoriasDB.detail(categoria)

