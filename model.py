from typing import Optional, Dict, Any
from snowflake.snowpark import Session
import pandas as pd


class SnowflakeModel:
    def __init__(self, credentials: Dict[str, Any]):
        self.credentials = credentials
        self.session = self.create_session()

    def create_session(self) -> Session:
        try:
            session = Session.builder.configs(self.credentials).create()
            return session
        except:
            raise ValueError(f"Error occurred while creating session")

    def load_data(self, sql_query: str) -> Optional[pd.DataFrame]:
        try:
            if self.session:
                query = self.session.sql(sql_query).collect()
                return pd.DataFrame(query)
            return None
        except:
            raise ValueError(f"Error occurred while loading data")
