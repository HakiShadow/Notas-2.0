from typing import NamedTuple, Optional



class Categoria(NamedTuple):
    id: Optional[int] = None
    categoria: Optional[str] = None

class Notas(NamedTuple):
    id: Optional[int] = None
    nota: Optional[str] = None
    dia: Optional[str] = None
    mes: Optional[str] = None
    estado: Optional[bool] = None

class Users(NamedTuple):
    id: Optional[int] = None
    user: Optional[str] = None
    pas: Optional[str] = None
