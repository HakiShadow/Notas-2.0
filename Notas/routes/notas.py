from flask import Blueprint, render_template, request, redirect, url_for
from ..helpers import auxx
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
    categoria = Categoria(id = id)
    if request.method == 'POST':
        datos = request.form
        nota = Notas(nota = datos['tarea'],
                    dia =  datos['dia'],
                    mes = datos['mes'],
                    estado = 0)
        notas_controller.create(categoria, nota)
        return redirect(url_for('notas.list', id = categoria))
    else:
        return render_template('tareaEdAdd.html', accion = 'Crear', id = categoria.id)

@notas.route('/eliminar/<id>/<notaid>')
def delete(id, notaid):
    categoria = Categoria(id = id)
    notaId = Notas(id = notaid)
    notas_controller.delete(categoria, notaId)
    return redirect(url_for('notas.list', id = categoria))

@notas.route('/editar/<id>/<idtarea>', methods = ['POST', 'GET'])
def editar(id, idtarea):
    categoria = Categoria(id = id)

    if request.method == 'POST':
        datos = request.form

        nota = Notas(nota = datos['tarea'],
                    dia =  datos['dia'],
                    mes = datos['mes'])

        notaID = Notas(id = idtarea)

        notas_controller.update(nota, notaID, categoria)
        return redirect(url_for('notas.list', id = categoria))
    else:
        return render_template('tareaEdAdd.html', accion = 'Editar', id = categoria.id)


@notas.route('/listo/<id>/<idtarea>')
def cambiar(id, idtarea):

    categoriaID = Categoria(id=id) # ID de la categoria
    
    categoria = auxx.select(categoriaID.id) # Nombre de la categoria

    nota = auxx.selectTarea(categoria, idtarea) # Contenido de la tabla categoria en ese id

    notas = Notas()

    if nota[3] == 0:
        estado = 1
        notas = Notas(id = idtarea, estado = estado)

        notas_controller.status(categoria, notas) # Se envia el nombre de la categoria, y el contenido de la tabla en ese id
    else: 
        estado = 0
        notas = Notas(id = idtarea, estado = estado)

        notas_controller.status(categoria, notas) # Se envia el nombre de la categoria, y el contenido de la tabla en ese id

    return redirect(url_for('notas.list', id = categoriaID))
