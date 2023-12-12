from typing import List, Any
import pandas as pd
from model import SnowflakeModel


class StreamlitController:
    """This is controler for streamlit"""

    def __init__(self, credentials: Any) -> None:
        self.model = SnowflakeModel(credentials)

    def get_data(self, query: str) -> pd.DataFrame:
        """This function pulls data from database with the given query"""
        try:
            return self.model.load_data(query)
        except Exception as e:
            # Log the exception (or handle it as required)
            raise e

    def filter_data(
            self,
            data: pd.DataFrame,
            column: str,
            values: List[str] = None,
            range_data: tuple = None,
            inclusive: bool = True) -> pd.DataFrame:
        """This function filters the data based on the input selections"""
        if column not in data.columns:
            # Log warning or raise an error
            return data

        if range_data:
            return data[data[column].between(
                *range_data, inclusive='both' if inclusive else 'neither')]
        if values:
            return data[data[column].isin(values)]
        return data
