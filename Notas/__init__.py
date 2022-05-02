from flask import Flask
from config import Config

from .routes import categoria, notas

app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
app.config.from_object(Config)


app.register_blueprint(categoria, url_prefix="/")
app.register_blueprint(notas, url_prefix="/")

#AQUI AGREGARE CADA BLUEPRINT NUEVO QUE SE ENCUENTRE EN LA CARPETA ROUTES, DESCONOZCO LA UTILIDAD DEL URL_PREFIX, revisar: https://code-examples.net/es/q/1216b91


# reset_table()
