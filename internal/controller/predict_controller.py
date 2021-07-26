from flask_restplus import Resource
from flask import request
import logging
from internal.dto.dto import prediction_return, prediction_create
from internal.controller.api import api
from internal.services.predict_service import PredictService

logger = logging.getLogger(__name__)

ns = api.namespace('predict', description='Operations related to prediction.')

@ns.route('/')
class Predict(Resource):
    @ns.expect(prediction_create)
    @api.marshal_with(prediction_return)
    def post(self):
        body = sanitize_body(request.get_json())
        if validate_body(body):
            ps = PredictService(body)
            res = ps.get_prediction() 
            return construct_response(body, res)
        else:
            return "error"
        
def sanitize_body(body):
    return body            

def validate_body(body):
    for key in body.keys():
        print(key)
    return True

def construct_response(body, res):    
    return { 'success': True if res == 1 else False, 'name': body.get('name') }    