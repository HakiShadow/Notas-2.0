from ..database import notasDB
from ..models.models import Notas, Categoria, Users
from ..helpers import auxx

def list(categoria):
    return notasDB.list_all(categoria)

def create(categoriaId: Categoria, nota: Notas, user: Users) -> Notas:
    return notasDB.create(categoriaId, nota, user)

def delete(nota: Notas):
    return notasDB.delete(nota)

def update(nota: Notas, notaID: Notas):
    return notasDB.update(nota, notaID)

def status(nota: Notas):

    status = auxx.tareaStatus(nota.id)

    try:
        if status == 0:
            status = 1
            nota = Notas(id = nota.id, estado = status)
            return notasDB.status(nota)
        else: 
            status = 0
            nota = Notas(id = nota.id, estado = status)
            return notasDB.status(nota)

    except Exception as ex:
        print(ex, 'Problema en control de sesion')
        return 406