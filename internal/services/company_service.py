from pandas.core.base import PandasObject
from pandas.core.indexes.base import InvalidIndexError
from client.aws import run_prediction
import pandas as pd
import os

class CompanyService:
    @staticmethod
    def get_company_by_id(id):
        df = pd.read_csv(os.path.join('data', 'companies.csv'))
        if id not in df.index:
            raise Exception(InvalidIndexError)
        company = df.iloc[id].to_dict()
        return company

    @staticmethod
    def get_companies(order_by: str, ascending: bool, page: int, row_count: int):
        df = pd.read_csv(os.path.join('data', 'companies.csv'))
        if order_by not in df.columns:
            order_by = 'location'
        df.sort_values(order_by, ascending=ascending, inplace=True)
        offset = (int(page) - 1) * int(row_count)
        companies = df.iloc[offset : offset + int(row_count)].to_dict('records')
        return companies
