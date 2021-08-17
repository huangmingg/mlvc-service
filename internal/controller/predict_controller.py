from flask_restplus import Resource
from flask import request
import logging
from internal.dto.dto import prediction_return, prediction_create
from internal.controller.api import api
from internal.services.predict_service import PredictService
from internal.services.statistics_service import StatisticsService

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
            stats = StatisticsService().get_statistics(body.get('country'), body.get('industries'))
            pred = ps.get_prediction() 
            resp = construct_response(body, pred, stats)
            return resp
        else:
            return "error"
        
def sanitize_body(body):
    return body            

def validate_body(body):
    for key in body.keys():
        pass
    return True

def construct_response(body, pred, stats):    
    return {
        'id': 'empty for now', 
        'company': body,
        'success': True if pred == 1 else False, 
        'company_stats': stats.get('detail'),
        'investment_stats': stats.get('investment'),
    }