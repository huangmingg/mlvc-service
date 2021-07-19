from flask_restplus import fields
from internal.controller.api import api

company_create = api.model('company_create', {
    'name': fields.String(required=True),
    'number_of_employees': fields.String(required=True)
})