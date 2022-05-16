from flask import Blueprint, render_template

exceptions = Blueprint("excep", __name__)

class Errores:

    @exceptions.errorhandler(404)
    def notfound():
        error = 'Pagina no encontrada'
        return render_template('error.html', error = error), 404

    @exceptions.errorhandler(400)
    def badrequest():
        error = 'Al menos una entrrada es incorrecta, verifique los datos ingresados'
        return render_template('error.html', error = error), 404