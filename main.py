
import streamlit as st
from controller import StreamlitController
from view import set_page_config, display_sidebar, display_data_frame, add_header

SNOWFLAKE_CREDENTIALS = {
    # add your Snowflake credentials here
}

def main():
    set_page_config()

    controller = StreamlitController(SNOWFLAKE_CREDENTIALS)
    add_header("Welcome to the Streamlit App")
