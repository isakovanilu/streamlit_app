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
    try:
        session = Session.builder.configs('your_credentials').create()
        return session
    except Exception as e:
        print(f"Error occurred while creating session: {e}")
        return None


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

    try:
        query = session.sql(sql_query).collect()
        return query
    except Exception as e:
        print(f"Error occurred while loading data: {e}")
        return None


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
    

def display_sidebar(data: pd.DataFrame):
    """
    Displays the sidebar filters for the given data.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
    """
    st.sidebar.header("Filters")
    columns_to_select = sorted(data['col1'].unique())
    selected_columns = st.sidebar.multiselect(
        "Selected Columns", columns_to_select, columns_to_select)
    # can be added multiple selection suck as slides
    return selected_columns


def main():
    """
    Main function to pull and display data.
    """
    set_page_config()

    # Load and display data
    # suppose you have the query here
    sql_query = """SELECT COL1, COL2 FROM TABLE1; """
    data = load_data(sql_query)
    # TODO add display functions
    selected_columns = display_sidebar(data)
    # Filter data with the given columns
    filtered_data = data.copy()
    filtered_data = filter_data(filtered_data, 'selected_columns', selected_columns, range_data=None)
    
    # write the title
    st.title("Data Display")
