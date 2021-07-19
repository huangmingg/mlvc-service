from flask_restplus import Resource
from flask import request, jsonify
import logging
from internal.dto.dto import *
from internal.controller.api import api

logger = logging.getLogger(__name__)

ns = api.namespace('predict', description='Operations related to prediction.')

@ns.route('/')
class Predict(Resource):
    @ns.expect(company_create)
    @api.marshal_with(company_create)
    def post(self):
        body = request.get_json()
        if (not body['name']) or (not body['number_of_employees']):
            logger.info("Missing parameters from request")
        else:
            return {'name': f"Group {body['name']} successfully created"}

    def get(self):
            response = jsonify({'some': 'data'})
            return response