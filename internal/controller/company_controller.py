from flask_restplus import Resource
from flask import request
import logging
from internal.dto.dto import company_read
from internal.controller.api import api
from internal.services.company_service import CompanyService

logger = logging.getLogger(__name__)

ns = api.namespace('company', description='Operations related to company.')

parser = api.parser()
parser.add_argument('page', type=int, help='Page filter', location='query')
parser.add_argument('row_count', type=int, help='Row Count per page', location='query')
parser.add_argument('order_by', type=str, help='Column to order by', location='query')
parser.add_argument('is_descending', type=bool, help='Is descending order', location='query')

@ns.route('/<int:id>')
class Company(Resource):
    @api.marshal_with(company_read)
    def get(self, id):
        data = CompanyService.get_company_by_id(id)
        return data

@ns.route('')
class CompanyList(Resource):
    @api.expect(parser)
    @api.marshal_list_with(company_read)
    def get(self):
        page = request.args.get('page')
        row_count = request.args.get('row_count')
        order_by = request.args.get('order_by')
        is_descending = request.args.get('is_descending')
        data = CompanyService.get_companies(order_by, is_descending, page, row_count)
        return data