from flask import Blueprint, render_template, request, redirect

from ..controller import cat_controller
from ..models.models import Categoria
from .exceptions import Errores
categoria = Blueprint("categorias", __name__)


@categoria.route('/', methods=['GET'])
def get_list():
    cat_list = cat_controller.lists()
    if cat_list == 'Recien creada':
        return redirect('/')
    else:
        return render_template('listCategorias.html', categoria = cat_list)

@categoria.route('/addCat', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':

        try:
            nombre = request.form['nombre']
            cat = Categoria(categoria = nombre)
        
        except Exception as ex:
            print(ex)
            return Errores.badrequest()
        else:
            cat_controller.create(cat)

        return redirect('/')
    else:
        return render_template('catEdAdd.html', accion = 'Añadir')

@categoria.route('/eliminarCat/<id>')
def delete(id):
    cat = Categoria(id = id)
    cat_controller.delete(cat)
    return redirect('/')

@categoria.route('/editarCat/<id>', methods = ['POST', 'GET'])
def editarCat(id):
    if request.method == 'POST':

        try:
            nombre = request.form
            cat = Categoria(id = id, categoria = nombre['nombre'])
        except Exception as ex:
            print(ex)
            return Errores.badrequest()
        else:
            cat_controller.update(cat)

        return redirect('/')
    else:
        return render_template('catEdAdd.html', id = id, accion = 'Editar')