from flask import Blueprint, render_template, request, redirect

from ..controller import cat_controller
from ..models.models import Categoria

categoria = Blueprint("categorias", __name__)

@categoria.route('/', methods=['GET'])
def get_list():
    cat_list = cat_controller.lists()
    return render_template('listCategorias.html', categoria = cat_list)

@categoria.route('/addCat', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cat = Categoria(categoria=nombre)
        cat_controller.create(cat)
        return redirect('/')
    else:
        return render_template('catEdAdd.html', accion = 'Añadir')

@categoria.route('/eliminarCat/<id>')
def delete(id):
    cat = Categoria(id=id)
    cat_controller.delete(cat)
    return redirect('/')

@categoria.route('/editarCat/<id>', methods = ['POST', 'GET'])
def editarCat(id):
    if request.method == 'POST':
        nombre = request.form
        cat = Categoria(id = id, categoria = nombre['nombre'])
        cat_controller.update(cat)
        return redirect('/')
    else:
        return render_template('catEdAdd.html', id = id, accion = 'Editar')