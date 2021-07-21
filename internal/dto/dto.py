from flask_restplus import fields
from internal.controller.api import api

prediction_create = api.model('prediction_create', {
    'name': fields.String(required=True)
})

company_read = api.model('company_read', {
    'location': fields.String(),
    'employee': fields.String(),
    'industries': fields.String(),
    'operating_status': fields.String(),
    'last_funding_type': fields.String(),
    'related_hubs': fields.String(),
    'hub_tags': fields.String(),
    'investment_stage': fields.String(),
    'number_of_funding_rounds': fields.String(),
    'number_of_lead_investors': fields.String(),
    'number_of_investors': fields.String(),
    'number_of_funds': fields.String(),
    'total_funding_amount': fields.String(),
    'total_fund_raised': fields.String(),
    'number_of_investments': fields.String(),
    'number_of_lead_investments': fields.String(),
    'number_of_diversity_investments': fields.String(),
    'number_of_acquisitions': fields.String(),
    'number_of_exits': fields.String(),
    'number_of_board_member_and_advisor_profiles': fields.String(),
    'number_of_employee_profiles': fields.String(),
    'total_products_active': fields.String(),
    'monthly_visits': fields.String(),
    'monthly_visits_growth': fields.String(),
    'active_tech_count': fields.String(),
    'number_of_articles': fields.String(),
    'number_of_events': fields.String(),
    'valuation_at_ipo': fields.String(),
    'money_raised_at_ipo': fields.String(),
    'last_funding': fields.String(),
    'downloads_last_30_days': fields.String(),
    'price': fields.String(),
    'diversity_spotlight_(us_only)': fields.String()
})