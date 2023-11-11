
from model import SnowflakeModel
import pandas as pd

class StreamlitController:
    def __init__(self, credentials):
        self.model = SnowflakeModel(credentials)

    def get_data(self, query):
        return self.model.load_data(query)

    def filter_data(self, data: pd.DataFrame, column: str, values: List[str], range_data: None) -> pd.DataFrame:
        if range_data and column in data.columns:
            return data[data[column].between(*range_data, inclusive='both')]
        elif values and column in data.columns:
            return data[data[column].isin(values)]
        else:
            return data
