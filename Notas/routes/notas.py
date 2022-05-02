from flask import Blueprint, render_template, request, redirect, url_for

from ..controller import notas_controller
from ..models.models import Notas, Categoria

notas = Blueprint("notas", __name__)

@notas.route('/tareas/<id>', methods=['GET'])
def list(id):
    # Este ID es el de la categoria
    notas = Notas(id=id)
    list = notas_controller.list(notas) or []
    return render_template('listTareas.html', tarea = list, id = id)

@notas.route('/add/<id>', methods=['GET', 'POST'])
def addNote(id):
    categoriaId = Categoria(id = id).id
    if request.method == ['POST']:
        datos = request.form()
        nota = Notas(nota = datos['tarea'],
                    dia =  datos['dia'],
                    mes = datos['mes'],
                    estado = datos['status'])

        notas_controller.create(categoriaId, nota)
        return redirect(url_for('list', id = categoriaId))
    else:
        return render_template('tareaEdAdd.html', accion = 'Crear', id = categoriaId)

@notas.route('/eliminar/<id>/<idtarea>')
def delete(id, idtarea):
    pass

@notas.route('/editar/<id>/<idtarea>', methods = ['POST', 'GET'])
def editar(id, idtarea):
    pass

@notas.route('/listo/<id>/<idtarea>')
def cambiar(id, idtarea):
    pass