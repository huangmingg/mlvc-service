from pandas.core.base import PandasObject
from pandas.core.indexes.base import InvalidIndexError
from client.aws import run_prediction
import pandas as pd
import os

DATA_DIRECTORY = os.path.join(os.getcwd(), "data")

class CompanyService:
    @staticmethod
    def get_company_by_id(id):
        df = pd.read_csv(os.path.join(DATA_DIRECTORY, 'companies.csv'))
        if id not in df.index:
            raise Exception(InvalidIndexError)
        company = df.iloc[id].to_dict()
        return company

    @staticmethod
    def get_all_companies():
        df = pd.read_csv(os.path.join(DATA_DIRECTORY, 'companies.csv'))
        companies = df.to_dict('records')
        return companies

    @staticmethod
    def get_companies(order_by, is_descending, page, row_count):
        descending = True if is_descending == 'true' else False
        df = pd.read_csv(os.path.join(DATA_DIRECTORY, 'companies.csv'))
        if order_by not in df.columns:
            order_by = 'location'
        df.sort_values(order_by, ascending=descending, inplace=True)
        df.reset_index(inplace=True, drop=True)
        offset = (int(page) - 1) * int(row_count)
        companies = df.iloc[offset : offset + int(row_count)]
        return companies.to_dict('records')
