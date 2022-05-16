from flask import Blueprint, render_template, request, redirect, session, url_for

from ..controller import cat_controller
from ..models.models import Categoria, Users
from .exceptions import Errores
from ..helpers import auxx

categoria = Blueprint("categorias", __name__)

@categoria.route('/<user>', methods=['GET'])
def get_list(user):
    try:
        if (user not in session['user']): 
            return redirect(url_for('sesiones.login'))

        else:
            user = Users(user = user, id = auxx.selectUserID(user))
            categorias = cat_controller.lists(user)

            return render_template('listCategorias.html', categoria = categorias, user = user.user)

    except Exception as ex:
        print(ex)
        return redirect(url_for('sesiones.login'))
        
@categoria.route('/<user>/addCat', methods=['GET', 'POST'])
def create(user):
    try:    
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))
        
        else:
            user = Users(user = user, id = auxx.selectUserID(user))

            if request.method == 'POST':
                try:
                    nombre = request.form['nombre']
                    cat = Categoria(categoria = nombre)
                
                except Exception as ex:
                    print(ex)
                    return Errores.badrequest()
                else:
                    cat_controller.create(cat, user)
                    return redirect(url_for('categorias.get_list', user = user.user))
            else:
                return render_template('catEdAdd.html', user = user.user, accion = 'Añadir categoria')

    except Exception as ex:
        print(ex)
        return redirect(url_for('sesiones.login'))

@categoria.route('/<user>/eliminarCat/<id>')
def delete(user, id):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))
        else:
            cat = Categoria(id = id)
            user = Users(user = user, id = auxx.selectUserID(user))
            cat_controller.delete(cat)
            return redirect(url_for('categorias.get_list', user = user.user))

    except Exception as ex:
        print(ex)
        return redirect(url_for('sesiones.login'))

@categoria.route('/<user>/editarCat/<id>', methods = ['POST', 'GET'])
def editarCat(user, id):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))

        else:
            user = Users(user = user, id = auxx.selectUserID(user))

            if request.method == 'POST':
                try:
                    nombre = request.form
                    cat = Categoria(id = id, categoria = nombre['nombre'])
                except Exception as ex:
                    print(ex)
                    return Errores.badrequest()
                else:
                    cat_controller.update(cat, user)
                    return redirect(url_for('categorias.get_list', user = user.user))

            else:
                return render_template('catEdAdd.html', user = user.user, id = id, accion = 'Editar categoria')

    except Exception as ex:
        print(ex)
        return redirect(url_for('sesiones.login'))