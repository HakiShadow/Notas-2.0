from flask import Blueprint, redirect, render_template, request, session, url_for

from ..controller import session_controller
from ..models.models import Users
from .exceptions import exceptions
from ..helpers import auxx

sesion = Blueprint("sesiones", __name__)


@sesion.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        datos = request.form
        user = datos['user']
        password = datos['pass']

        user = Users(user = user, pas = password)

        recordar = datos.get('check')
        recordar = auxx.recordarme(recordar)

        if session_controller.verify(user):
            session.clear()
            session["user"] = user.user
            session["auth"] = 1
            session.permanent = recordar
            return redirect(url_for('categorias.get_list'))
        else:
            return redirect(url_for('sesiones.login'))
    else:
        return render_template('login.html')

@sesion.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'POST':

        datos = request.form
        user = datos['user']
        password = datos['pass']

        user = Users(user = user, pas = password)

        if session_controller.register(user) == 200:
            return redirect(url_for('sesiones.login'))
        else:
            return redirect(url_for('sesiones.signup'))
    else:
        return render_template('signUp.html')

# @sesion.route('/logout')
# def logout():
#     pass

# @session.route('/update')
# def update():
#     pass