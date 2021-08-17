from flask_restplus import Resource
from flask import request
import logging
from internal.dto.dto import company_read
from internal.controller.api import api
from internal.services.statistics_service import StatisticsService

logger = logging.getLogger(__name__)

ns = api.namespace('statistics', description='Operations related to any statistics retrieval.')

parser = api.parser()
parser.add_argument('location', type=str, help='Location', location='query')
parser.add_argument('industries', type=list, help='Industries', location='query')

@ns.route('')
class CompanyStatisticsList(Resource):
    @api.expect(parser)
    @api.marshal_list_with(company_read)
    def get(self):
        location = request.args.get('location')
        industries = request.args.get('industries')
        data = StatisticsService.get_company_statistics(location, industries)
        return data