from flask_restplus import Resource
import logging
from internal.controller.api import api

logger = logging.getLogger(__name__)

ns = api.namespace('heartbeat', description='Heart Beat.')

@ns.route('/')
class Heartbeat(Resource):
    def get(self):
        return "OK"
    