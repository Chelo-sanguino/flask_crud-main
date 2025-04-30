from flask import Flask
from config import config
from flask_cors import CORS
from pedidos.adapters.articulos_adapter import ArticulosAdapter
from pedidos.helpers.pg_command import PGCommand

app = Flask(__name__, template_folder='./presentation/templates', static_folder='./presentation/static')
app.config.from_object(config["dev"])

# Configurar CORS correctamente para todas las rutas de la API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

db = PGCommand()

from pedidos.presentation.controllers.site_controller import *
from pedidos.presentation.controllers.articulos_controller import *
from pedidos.presentation.controllers.articulos_api_controller import articulos_api

# Registrar el blueprint con la URL correcta
app.register_blueprint(articulos_api, url_prefix='/api/articulos')
