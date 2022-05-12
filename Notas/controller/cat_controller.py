from ..database import categoriasDB
from ..models.models import Categoria, Users

def lists(user: Users):
    userID = user.id
    return categoriasDB.list_all(userID)

def create(categoria: Categoria, user: Users) -> Categoria:
    # categoria es una instancia de la clase Categoria, por ende un objeto
    # En este caso, el controlador solo es un intermediario
    return categoriasDB.create(categoria, user)

def delete(categoria: Categoria, user: Users) -> Categoria:
    return categoriasDB.delete(categoria, user)

def update(categoria: Categoria, user: Users) -> Categoria:
    return categoriasDB.update(categoria, user)
