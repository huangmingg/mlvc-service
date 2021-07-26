## Code retrieved from https://github.com/NUS-Fintech-Society/ML_VC-Library/tree/main/mlvc/train

import os
import logging
import pickle
import numpy as np
from xgboost import XGBClassifier

logger = logging.getLogger(__name__)

MODEL_DIRECTORY = os.path.join(os.getcwd(), "client")

def run_prediction(data):
    feature = _transform_data_to_feature(data)
    model = XGBClassifier()
    model.load_model(os.path.join(MODEL_DIRECTORY, "xgb.json"))
    scaler = pickle.load(open(os.path.join(MODEL_DIRECTORY, "scaler.pkl"), 'rb'))
    scaled_input = scaler.transform(np.asarray(feature).reshape(-1, 15))
    pred = model.predict(scaled_input)
    return pred[0]


def _transform_data_to_feature(data):
    # data = {'last_funding_type': 'Series A', 'hub_tags': 'Unicorn', 'employee': '1001-5000',
    #         'industries': "['Banking', 'Internet', 'Mobile', 'Telecommunications']",
    #         'total_products_active': 7, 'valuation_at_ipo': 600000,
    #         'money_raised_at_ipo': 500000, 'number_of_acquisitions': 14, 'number_of_investments': 44,
    #         'number_of_lead_investments': 30, 'number_of_lead_investors': 2,
    #         'number_of_employee_profiles': 91, 'company_type': 'For Profit'}

    emp = employees_to_le_single(data.get('employee'))
    fund_type_A, fund_type_B = grp_last_funding_type_single(data.get('last_funding_type'))
    hub_unicorn, hub_emerging_unicorn = hub_tag_cat_single(data.get('hub_tags'))
    comp_type = company_type_to_ohe_single(data.get('company_type'))
    kmeans_ind = pickle.load(open(os.path.join(MODEL_DIRECTORY, 'kmeans_industries.sav'), 'rb'))
    tfidf_ind = pickle.load(open(os.path.join(MODEL_DIRECTORY, 'tfidf_industries.pkl'), 'rb'))
    ind = " ".join(data.get('industries'))[0]
    ind_pred = kmeans_ind.predict(tfidf_ind.transform([ind]))[0]

    final_input_values = []
    final_input_values.append(emp)
    final_input_values.append(fund_type_A)
    final_input_values.append(fund_type_B)
    final_input_values.append(data.get('money_raised_at_ipo'))
    final_input_values.append(data.get('valuation_at_ipo'))
    final_input_values.append(hub_unicorn)
    final_input_values.append(comp_type)
    final_input_values.append(hub_emerging_unicorn)
    final_input_values.append(ind_pred)
    final_input_values.append(data.get('total_products_active'))
    final_input_values.append(data.get('number_of_acquisitions'))
    final_input_values.append(data.get('number_of_investments'))
    final_input_values.append(data.get('number_of_lead_investments'))
    final_input_values.append(data.get('number_of_lead_investors'))
    final_input_values.append(data.get('number_of_employee_profiles'))
    return final_input_values

def employees_to_le_single(employ):
    employees = {'1-10': 1, '11-50': 2, '51-100': 3, '101-250': 4, '251-500': 5,
                 '501-1000': 6, '1001-5000': 7, '5001-10000': 8, '10001+': 9}

    if employ in employees.keys():
        employ_new = employees.get(employ)

    return employ_new

def grp_last_funding_type_single(last_fund):
    grp = ''
    tags = {'Group A': ['Pre-Seed', 'Debt Financing', 'Private Equity', 'Angel', 'Seed', 'Initial Coin Offering',
                        'Venture - Series Unknown', 'Equity Crowdfunding'],
            'Group B': ['Secondary Market', 'Post-IPO Secondary', 'Post-IPO Equity', 'Series G', 'Series H', 'Series I',
                        'Series F', 'Post-IPO Debt'],
            'Group C': ['Product Crowdfunding', 'Corporate Round', 'Convertible Note', 'Undisclosed', 'Series A',
                        'Series B', 'Series C', 'Grant', 'Series D', 'Series E', 'Non-equity Assistance']}

    if last_fund is not np.nan:
        for k, v in tags.items():
            if last_fund in v:
                grp = grp + k
    if grp == 'Group A':
        return 1, 0
    elif grp == 'Group B':
        return 0, 1
    else:
        return 0, 0

def hub_tag_cat_single(hub_tag):
    tag = ''
    tags = {'Unicorn': ['Unicorn', 'Pledge 1%, Unicorn'],
            'Exited Unicorn': ['Exited Unicorn', 'Exited Unicorn, Pledge 1%',
                               'Crunchbase Venture Program, Exited Unicorn'],
            'Emerging Unicorn': ['Emerging Unicorn', 'Emerging Unicorn, Pledge 1%'],
            'Others': ['Crunchbase Venture Program', 'Crunchbase Venture Program, Pledge 1%', 'Pledge 1%']}

    if hub_tag is not np.nan:
        for k, v in tags.items():
            if hub_tag in v:
                tag = tag + k
    if tag == 'Unicorn':
        return 1, 0
    elif tag == 'Emerging Unicorn':
        return 0, 1
    else:
        return 0, 0        

def company_type_to_ohe_single(type):
    if type == "For Profit":
        return 1
    else:
        return 0