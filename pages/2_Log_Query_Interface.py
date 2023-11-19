# app.py

import streamlit as st
import pandas as pd
from datetime import datetime, time
from dateutil import parser
from streamlit_pagination import pagination_component


# Sample JSON data
json_data = {
    "level": "error",
    "message": "Failed to connect to DB",
    "resourceId": "server-1234",
    "timestamp": "2023-09-15T08:00:00Z",
    "traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}

PAGE_NO=1
PAGE_SIZE=10

def main():
    st.title("Log Search Interface")
    query, log_level = st.columns([6, 2])

    # Top row
    with query:
        query = st.text_input("Enter search query:", "", key="query")
    with log_level:
        log_level_options = ["All", "Error", "Info", "Debug"]  # Add other log levels as needed
        log_level = st.selectbox("Select log level:", log_level_options, key="log_level")

   
    start_date, start_time = st.columns([2, 2])

    # Date input
    with start_date:
        selected_date = st.date_input("Select an start date", datetime.today())

    # Time input
    with start_time:
        # Set the default time to 23:59 (11:59 PM)
        default_time = datetime.combine(datetime.today(), time(23, 59))

        # Time input with default value
        selected_time = st.time_input("Select an start time", default_time.time())

    # Combine date and time to create a timestamp
    start_timestamp = datetime.combine(selected_date, selected_time)

    # Display the timestamp
    st.write("Selected start Timestamp:", start_timestamp)

    end_date, end_time = st.columns([2, 2])

    # Date input
    with end_date:
        selected_date = st.date_input("Select an end date", datetime.today())

    # Time input
    with end_time:
        # Set the default time to 23:59 (11:59 PM)
        default_time = datetime.combine(datetime.today(), time(23, 59))

        # Time input with default value
        selected_time = st.time_input("Select an end time", default_time.time())

    # Combine date and time to create a timestamp
    end_timestamp = datetime.combine(selected_date, selected_time)

    # Display the timestamp
    st.write("Selected End Timestamp:", end_timestamp)

    if st.button("Search"):
        print(f"{query}, {log_level}, {start_timestamp}, {end_timestamp}")
    
    
    # Create a DataFrame with a single row
    df = pd.DataFrame([json_data])

    # Display the table
    st.table(df)
    # User inputs
    page_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Layout with three columns
    left_column, middle_column, right_column = st.columns([4, 1, 4])

    # Left column: Text "Showing 1 out of 15 pages"
    left_column.text("Showing 1 out of 15 pages")

    # Middle column: Empty space
    # (Middle column is 1/5th of the available space)
    middle_column.text("")  # You can leave this empty or add any text you want

    # Right column: Page size dropdown and Page number input with minimum width
    with right_column:
        l_col, r_col = st.columns([1,1])
        with l_col:
            page_size = st.selectbox("Choose Page Size:", page_sizes, index=0, key="page_size")
        with r_col:
            page_no = st.number_input("Enter Page Number:", min_value=1, value=1, key="page_no")


if __name__ == "__main__":
    main()
