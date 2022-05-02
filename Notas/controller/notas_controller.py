from ..database import notasDB
from ..models.models import Notas, Categoria

def list(notas):
    return notasDB.list_all(notas)

def create(categoriaId: Categoria, nota: Notas) -> Notas:
    print('notas')
    return notasDB.create(categoriaId, nota)

# def delete(categoria: Categoria) -> Categoria:
#     return categorias.delete(categoria)

# def update(categoria: Categoria) -> Categoria:
#     return categorias.update(categoria)

# def details(categoria: Categoria) -> Categoria:
#     return categorias.detail(categoria)

