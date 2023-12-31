import os
import streamlit as st
from controller import StreamlitController
from view import set_page_config, display_sidebar, display_data_frame, add_header

SNOWFLAKE_CREDENTIALS = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT")
}
DEFAULT_QUERY = "SELECT COL1, COL2 FROM TABLE1;"

def main() -> None:
    """run the streamlit app."""
    set_page_config()
    controller = StreamlitController(SNOWFLAKE_CREDENTIALS)
    add_header("Welcome to the Streamlit App")

    sql_query = st.text_area("Enter your SQL query", DEFAULT_QUERY)

    try:
        data = controller.get_data(sql_query)
        if data is not None:
            selected_columns = display_sidebar(data)
            filtered_data = controller.filter_data(data, 'COL1', selected_columns)
            display_data_frame(filtered_data)
        else:
            st.error("No data returned from the query.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
