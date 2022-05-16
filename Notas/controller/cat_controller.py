from ..database import categoriasDB
from ..models.models import Categoria, Users

def lists(user: Users):
    return categoriasDB.list_all(user)

def create(categoria: Categoria, user: Users) -> Categoria:
    return categoriasDB.create(categoria, user)

def delete(categoria: Categoria) -> Categoria:
    return categoriasDB.delete(categoria)

def update(categoria: Categoria, user: Users) -> Categoria:
    return categoriasDB.update(categoria, user)
