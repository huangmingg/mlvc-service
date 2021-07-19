from flask import Flask, Blueprint
from flask_cors import CORS
from internal.controller.api import api
from internal.controller.blueprint import blueprint
import logging
from internal.controller.predict_controller import ns as predict_ns

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

CORS(app)

api.init_app(blueprint)
api.add_namespace(predict_ns)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(threaded=True)

