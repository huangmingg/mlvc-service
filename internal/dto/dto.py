from flask_restplus import fields
from internal.controller.api import api

company_read = api.model('company_read', {
    'id': fields.String(required=True),
    'name': fields.String(),
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


prediction_create = api.model('prediction_create', {
    'name': fields.String(required=True),
    'country': fields.String(), 
    'company_type': fields.String(), 
    'employee': fields.String(), 
    'description': fields.String(), 
    'founded_at': fields.String(), 
    'last_funding_type': fields.String(), 
    'valuation_at_ipo': fields.Float(), 
    'money_raised_at_ipo': fields.Float(), 
    'number_of_acquisitions': fields.Float(), 
    'number_of_investments': fields.Float(), 
    'number_of_lead_investments': fields.Float(), 
    'number_of_lead_investors': fields.Float(), 
    'total_product_active': fields.Float(), 
    'active_tech_count': fields.Float(), 
    'number_of_employee_profile': fields.Float(), 
    'industries': fields.List(fields.String()),
})

detail_stat = api.model('detail_stat', {
    'total_products_active': fields.Float(), 
    'number_of_employee_profiles': fields.Float(), 
    'number_of_board_member_and_advisor_profiles': fields.Float(), 
    'active_tech_count': fields.Float(), 
    'number_of_articles': fields.Float(), 
    'number_of_events': fields.Float(),
})

investment_stat = api.model('investment_stat', {
    'number_of_lead_investors': fields.Float(), 
    'number_of_investors': fields.Float(), 
    'number_of_investments': fields.Float(), 
    'number_of_lead_investments': fields.Float(), 
    'number_of_acquisitions': fields.Float(), 
    'valuation_at_ipo': fields.Float(), 
    'money_raised_at_ipo': fields.Float(),
})

comp_detail_stat = api.model('comp_detail_stat', {
    'upper': fields.Nested(detail_stat),
    'median': fields.Nested(detail_stat),
    'lower': fields.Nested(detail_stat),
})

comp_investment_stat = api.model('comp_investment_stat', {
    'upper': fields.Nested(investment_stat),
    'median': fields.Nested(investment_stat),
    'lower': fields.Nested(investment_stat),
})

prediction_return = api.model('prediction_return', {
    'company_id': fields.String(required=True),
    'company': fields.Nested(company_read),
    'success': fields.Boolean(required=True),
    'company_stats': fields.Nested(comp_detail_stat),
    'investment_stats': fields.Nested(comp_investment_stat),
})

company_statistics_read = api.model('company_statistics_read', {
    'id': fields.String(required=True),
    'name': fields.String(),
    'employee': fields.String(),
    'industries': fields.String(),
    'operating_status': fields.String(),
    'last_funding_type': fields.String(),
    'related_hubs': fields.String(),
    'hub_tags': fields.String(),
    'investment_stage': fields.String(),
    'number_of_funding_rounds': fields.Float(),
    'number_of_lead_investors': fields.Float(),
    'number_of_investors': fields.Float(),
    'number_of_funds': fields.Float(),
    'total_funding_amount': fields.Float(),
    'total_fund_raised': fields.Float(),
    'number_of_investments': fields.Float(),
    'number_of_lead_investments': fields.Float(),
    'number_of_diversity_investments': fields.Float(),
    'number_of_acquisitions': fields.Float(),
    'number_of_exits': fields.Float(),
    'number_of_board_member_and_advisor_profiles': fields.Float(),
    'number_of_employee_profiles': fields.Float(),
    'total_products_active': fields.Float(),
    'monthly_visits': fields.Float(),
    'monthly_visits_growth': fields.Float(),
    'active_tech_count': fields.Float(),
    'number_of_articles': fields.Float(),
    'number_of_events': fields.Float(),
    'valuation_at_ipo': fields.Float(),
    'money_raised_at_ipo': fields.Float(),
    'last_funding': fields.Float(),
    'downloads_last_30_days': fields.Float(),
    'price': fields.Float(),
    'diversity_spotlight_(us_only)': fields.String()
})