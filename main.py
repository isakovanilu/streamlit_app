
import streamlit as st
import os
from controller import StreamlitController
from view import set_page_config, display_sidebar, display_data_frame, add_header

SNOWFLAKE_CREDENTIALS = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT")
}

def main():
    set_page_config()

    controller = StreamlitController(SNOWFLAKE_CREDENTIALS)
    add_header("Welcome to the Streamlit App")

    # suppose you have the query here
    sql_query = """SELECT COL1, COL2 FROM TABLE1; """
    data = controller.get_data(sql_query)

    if data is not None:
        # display the sidebar and get the selected columns
        selected_columns = display_sidebar(data)
        
        # filter data based on the sidebar selection
        filtered_data = controller.filter_data(data, 'COL1', selected_columns)
        
        # display the filtered data
        display_data_frame(filtered_data)
    else:
        st.error("Failed to load data.")

if __name__ == "__main__":
    main()
