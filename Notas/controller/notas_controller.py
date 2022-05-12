from ..database import notasDB
from ..models.models import Notas, Categoria

def list(categoria):
    return notasDB.list_all(categoria)

def create(categoriaId: Categoria, nota: Notas) -> Notas:
    return notasDB.create(categoriaId, nota)

def delete(categoriaId: Categoria, nota: Notas):
    return notasDB.delete(categoriaId, nota)

def update(nota: Notas, notaID: Notas, categoria: Categoria):
    return notasDB.update(nota, notaID, categoria)

def status(categoria: Categoria, nota: Notas):
    return notasDB.status(categoria, nota)