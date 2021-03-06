from flask import Blueprint, redirect, render_template, request, session, url_for

from ..controller import session_controller
from ..models.models import Users
from ..helpers import auxx

sesion = Blueprint("sesiones", __name__)


@sesion.route('/', methods=['GET', 'POST'])
def login():
    if not (session.get('user') == None):
        return redirect(url_for('categorias.get_list', user = session['user']))

    else:
        if request.method == 'GET':
            return render_template('login.html')

        else:
            try:
                datos = request.form
                user = datos['user']
                password = datos['pass']

                user = Users(user = user, pas = password)

                recordar = datos.get('check')
                recordar = auxx.recordarme(recordar)

                if session_controller.login(user) == 200:
                    session.clear()
                    session["user"] = user.user
                    session["auth"] = 1
                    session.permanent = recordar
                    return redirect(url_for('categorias.get_list', user = user.user))
                else:
                    return redirect(url_for('sesiones.signup'))

            except Exception as ex:
                print(ex, 'here')
                return redirect(url_for('sesiones.signup'))

@sesion.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signUp.html')
    else:
        try:
            datos = request.form
            user = datos['user']
            password = datos['pass']

            user = Users(user = user, pas = password)

            if session_controller.register(user) == 200:
                return redirect(url_for('sesiones.login'))
            else:
                return redirect(url_for('sesiones.signup'))

        except Exception as ex:
            print(ex)
            return redirect(url_for('sesiones.signup'))

@sesion.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('sesiones.login'))

@sesion.route('/delete', methods=['GET', 'POST'])
def delete():
        if (session.get('user') == None):
            return redirect(url_for('sesiones.login'))

        else:
            if request.method == 'GET':
                return render_template('confirm.html')
            
            else:
                datos = request.form
                user = datos['user']
                password = datos['pass']

                user = Users(user = user, pas = password)

                session_controller.delete(user)
                return redirect(url_for('sesiones.login'))



# @session.route('/update')
# def update():
#     pass

