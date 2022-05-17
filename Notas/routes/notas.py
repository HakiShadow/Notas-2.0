from flask import Blueprint, render_template, request, redirect, url_for, session
from ..helpers import auxx
from ..controller import notas_controller
from ..models.models import Notas, Categoria, Users
from .exceptions import Errores

notas = Blueprint("notas", __name__)

@notas.route('/<user>/categoria/<id>', methods=['GET'])
def list(user, id):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))
   
        else:
            catNombre = auxx.selectCategoria(id) # Devuelve el nombre de la categoria
            idUser = auxx.selectUserID(user) # Utilizando el nombre de usuario, buscamos el id del user
            categoria = Categoria(id = id, categoria = catNombre, id_user = idUser)
            notas = notas_controller.list(categoria) or []

            return render_template('listTareas.html', 
                                    tarea = notas, 
                                    id = id, 
                                    user = user, 
                                    categoria = categoria.categoria)

    except Exception as ex:
        print(ex)
        return redirect(url_for('categorias.get_list', user = user))

@notas.route('/<user>/add/<id>', methods=['GET', 'POST'])
def addNote(user, id):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))

        else:
            categoria = Categoria(id = id)
            user = Users(user = user, id = auxx.selectUserID(user))

            if request.method == 'GET':
                return render_template('tareaEdAdd.html', user = user.user, accion = 'Crear nota', id = categoria.id)
    
            else:
                try:
                    datos = request.form
                    nota = Notas(nota = datos['tarea'],
                                dia = datos.get('dia'),
                                mes = datos.get('mes'),
                                estado = 0)
                except Exception as ex:
                    print(ex)
                    return Errores.badrequest()
                else:   
                    notas_controller.create(categoria, nota, user)
                    return redirect(url_for('notas.list', user = user.user, id = categoria.id))

    except Exception as ex:
        print(ex)
        return redirect(url_for('notas.list', user = user.user, id = id))

@notas.route('/<user>/eliminar/<id>/<notaid>')
def delete(user, id, notaid):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))

        else:
            nota_id = Notas(id = notaid)
            notas_controller.delete(nota_id)
            return redirect(url_for('notas.list', user = user, id = id))

    except Exception as ex:
        print(ex)
        return redirect(url_for('notas.list', user = user, id = id))

@notas.route('/<user>/editar/<id>/<idtarea>', methods = ['POST', 'GET'])
def editar(user, id, idtarea):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))

        else:
            if request.method == 'GET':
                return render_template('tareaEdAdd.html', user = user, accion = 'Editar nota', id = id)
            else:
                try:
                    datos = request.form
                    newNota = Notas(nota = datos['tarea'],
                                dia = datos.get('dia'),
                                mes = datos.get('mes'))
                    notaID = Notas(id = idtarea)

                except Exception as ex:
                    print(ex)
                    return  Errores.badrequest()
                
                else:
                    notas_controller.update(newNota, notaID)
                    return redirect(url_for('notas.list', user = user, id = id))

    except Exception as ex:
        print(ex)
        return redirect(url_for('notas.list', user = user, id = id))

@notas.route('/<user>/listo/<id>/<idtarea>')
def cambiar(user, id, idtarea):
    try:
        if user not in session['user']:
            return redirect(url_for('sesiones.login'))

        else:
            nota = Notas(id = idtarea)
            notas_controller.status(nota)

            return redirect(url_for('notas.list', user = user, id = id))

    except Exception as ex:
        print(ex)
        return redirect(url_for('notas.list', user = user, id = id))