from snowflake.snowpark import Session
import pandas as pd
from typing import Optional, Dict, Any


class SnowflakeModel:
    def __init__(self, credentials: Dict[str, Any]):
        self.credentials = credentials
        self.session = self.create_session()

    def create_session(self):
        try:
            session = Session.builder.configs(self.credentials).create()
            return session
        except Exception as e:
            print(f"Error occurred while creating session: {e}")
            return None

    def load_data(self, sql_query: str) -> Optional[pd.DataFrame]:
        try:
            if self.session:
                query = self.session.sql(sql_query).collect()
                return pd.DataFrame(query)
            else:
                return None
        except Exception as e:
            print(f"Error occurred while loading data: {e}")
            return None