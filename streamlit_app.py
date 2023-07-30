from typing import List, Tuple
import pandas as pd
import plotly.express as px
import streamlit as st
import datetime as dt
import seaborn as sns
import sql_queries as sql
from datetime import date
from snowflake.snowpark import Session
import matplotlib.pyplot as plt



def set_page_config():
    """
    Sets the page configuration
    """
    st.set_page_config(
        page_title="Streamlit App",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        "<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)


def filter_data(data: pd.DataFrame, column: str, values: List[str], range_data: None) -> pd.DataFrame:
    """
    Filter data based on specified column and values.

    Args:
        data: The DataFrame to filter.
        column: The column name to filter on.
        values: The list of values to filter.
        range_data: The range of data to filter between the cols

    Returns:
        The filtered DataFrame.
    """
    if column in ('col1', 'col2', 'col3'):
        return data[data[column].between(*range_data, inclusive='both')] if range_data else data
    else:
        return data[data[column].isin(values)] if values else data


@st.cache_resource
# Cache the resource to create the session
def create_session():
    """
    Create a session object with Snowflake configuration.

    Returns:
        Session: Session object.
    """
    session = Session.builder.configs('your_credentials').create()
    return session

@st.cache_data
def load_data(sql_query):
    """
    Connects to Snowflake, creates a session, and pulls data with the given query.

    Parameters:
        sql_query (str): The SQL query to pull the data.

    Returns:
        query (object): The result of the query.
    """
    session = create_session()
    # pull the data with the given query
    query = session.sql(sql_query).collect()
    return query

def add_header(text):
    """
    Adds a header with given text to the Markdown content.

    Args:
        text (str): The text for the header.

    Returns:
        None
    """
    new_title = f'<h style="font-family:sans-serif; color:#6495ED; font-size: 35px;">{text}</h>'
    st.markdown(new_title, unsafe_allow_html=True)