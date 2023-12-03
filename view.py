
from typing import List
import streamlit as st
import pandas as pd


def set_page_config() -> None:
    """This function sets the page configuration"""

    st.set_page_config(page_title="Streamlit App", page_icon=":bar_chart:",
                       layout="wide", initial_sidebar_state="expanded")
    st.markdown(
        "<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)


def add_header(text) -> None:
    """This function adds the header"""
    new_title = f'<h style="font-family:sans-serif; color:#6495ED; font-size: 35px;">{text}</h>'
    st.markdown(new_title, unsafe_allow_html=True)


def display_sidebar(data: pd.DataFrame) -> List[str]:
    st.sidebar.header("Filters")
    columns_to_select = sorted(data.columns)
    selected_columns = st.sidebar.multiselect(
        "Selected Columns", columns_to_select, columns_to_select[0])
    return selected_columns


def display_data_frame(data: pd.DataFrame) -> None:
    st.title("Data Display")
    st.write("Filtered Data")
    st.dataframe(data)
