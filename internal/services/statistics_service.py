import pandas as pd
import os

DATA_DIRECTORY = os.path.join(os.getcwd(), "data")

class StatisticsService:
    
    @staticmethod
    def get_statistics(location, industries):
        df = pd.read_csv(os.path.join(DATA_DIRECTORY, 'companies.csv'))
        df = df.loc[df['location_country'] == location]
        detail = _get_company_statistics(df)
        investment = _get_investment_statistics(df)
        return { 'detail': detail, 'investment': investment }
    
def _get_company_statistics(df):
    df = df[[
        'total_products_active', 
        'number_of_employee_profiles', 
        'number_of_board_member_and_advisor_profiles', 
        'active_tech_count', 
        'number_of_articles', 
        'number_of_events',
        ]]
    quantile = df.quantile([.25, .5, .75])
    resp = {
        'lower': quantile.iloc[0].to_dict(), 
        'median': quantile.iloc[1].to_dict(), 
        'upper': quantile.iloc[2].to_dict(),
    }
    return resp

def _get_investment_statistics(df):
    df = df[[
        'number_of_lead_investors', 
        'number_of_investors', 
        'number_of_investments', 
        'number_of_lead_investments', 
        'number_of_acquisitions',
        ]]
    quantile = df.quantile([.25, .5, .75])
    resp = {
        'lower': quantile.iloc[0].to_dict(), 
        'median': quantile.iloc[1].to_dict(), 
        'upper': quantile.iloc[2].to_dict(),
    }
    return resp

    