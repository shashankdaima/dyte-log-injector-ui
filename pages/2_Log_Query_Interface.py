import pandas as pd
from datetime import datetime, time
import streamlit as st
from utils.sql_utils import get_engine_and_session, search_logs_in_postgres

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


def search_logs(query, log_level, start_timestamp, end_timestamp, page_size, page_no):
    engine, Session=get_engine_and_session()
    result=search_logs_in_postgres(Session(),query,log_level, start_timestamp, end_timestamp, page_size, page_no )
    search_result = pd.DataFrame(result)
    return search_result

def main():
    st.title("Log Search Interface")
    query, log_level = st.columns([6, 2])

    # Top row
    with query:
        query = st.text_input("Enter search query (@resourceId=server-1234 or @traceId=server-1234 or @spanId=span-456):", "", key="query")
    with log_level:
        log_level_options = ["All", "Error", "Info", "Debug"]  # Add other log levels as needed
        log_level = st.selectbox("Select log level:", log_level_options, key="log_level")

    start_date, start_time = st.columns([2, 2])

    # Date input
    with start_date:
        selected_date = st.date_input("Select a start date", datetime.today())

    # Time input
    with start_time:
        default_time = datetime.combine(datetime.today(), time(23, 59))
        selected_time = st.time_input("Select a start time", default_time.time())

    start_timestamp = datetime.combine(selected_date, selected_time)

    # Display the timestamp
    st.write("Selected start Timestamp:", start_timestamp)

    end_date, end_time = st.columns([2, 2])

    # Date input
    with end_date:
        selected_date = st.date_input("Select an end date", datetime.today())

    # Time input
    with end_time:
        default_time = datetime.combine(datetime.today(), time(23, 59))
        selected_time = st.time_input("Select an end time", default_time.time())

    end_timestamp = datetime.combine(selected_date, selected_time)

    # Display the timestamp
    st.write("Selected End Timestamp:", end_timestamp)

    # User inputs
    page_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Layout with three columns
    left_column, middle_column, right_column = st.columns([1, 4, 1])

  
    # Middle column: Empty space
    # (Middle column is 1/5th of the available space)
    # middle_column.text("")  # You can leave this empty or add any text you want

    # Right column: Page size dropdown and Page number input with minimum width
    with middle_column:
        l_col, r_col = st.columns([1,1])
        with l_col:
            page_size = st.selectbox("Choose Page Size:", page_sizes, index=0, key="page_size")
        with r_col:
            page_no = st.number_input("Enter Page Number:", min_value=1, value=1, key="page_no")
            page_no_count=page_no
    # Automatic search whenever input changes
    search_result = search_logs(query, log_level, start_timestamp, end_timestamp, page_size, page_no)
    # print(search_result)
    st.table(search_result)

if __name__ == "__main__":
    main()
