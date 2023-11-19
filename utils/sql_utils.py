import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy import text
import re
def get_engine_and_session():
    load_dotenv()
    
    db_config = {
        "user": os.environ.get("SQL_USERNAME"),
        "password": os.environ.get("SQL_PASSWORD"),
        "host": os.environ.get("SQL_HOST"),
        "port": int(os.environ.get("SQL_PORT")),  
        "database": os.environ.get("SQL_DB_NAME"),
    }

    DB_URL = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    # Create a SQLAlchemy engine
    engine = create_engine(DB_URL)

    # Create a session
    Session = sessionmaker(bind=engine)
    return engine, Session


def execute_query(engine, query):
    connection = engine.connect()
    result = connection.execute(query)
    connection.close()
    return result

def search_logs_in_postgres(session, query, log_level, start_timestamp, end_timestamp, page_size, page_no):
    # Replace this query with your actual search query
    # This is just a placeholder query
    print(query, log_level, start_timestamp, end_timestamp)
    
    log_level_filter = f"AND level = '{log_level.lower()}'" if log_level != 'All' else ''
    date_filter = f"AND timestamp BETWEEN '{start_timestamp}' AND '{end_timestamp}'"

    # Calculate the offset based on the page size and number
    offset = (page_no - 1) * page_size

    # Substring matching with the message column
    substr_filter = f"AND message ILIKE '%{query}%'"


    # Check for compound queries
    span_id_filter = ''
    trace_id_filter = ''
    resource_id_filter = ''

    if '@spanId' in query:
        span_id = query.split('=')[1]
        span_id_filter = f"AND span_id = '{span_id}'"
        substr_filter=""
    if '@traceId' in query:
        trace_id = query.split('=')[1]
        trace_id_filter = f"AND trace_id = '{trace_id}'"
        substr_filter=""

    if '@resourceId' in query:
        resource_id = query.split('=')[1]
        resource_id_filter = f"AND resource_id = '{resource_id}'"
        substr_filter=""


    # Check for regex query
    regex_match = re.match(r'^/([^/]+)/$', query)
    regex_filter = "" 
    if regex_match:
        regex_filter= f"AND message ~ '{regex_match.group(1)}'"
        resource_id_filter=""
        trace_id_filter=""
        span_id_filter=""
        


    sql_query = f"SELECT * FROM log_data_table WHERE 1=1 {log_level_filter} {date_filter} {substr_filter} {span_id_filter} {trace_id_filter} {resource_id_filter} {regex_filter} LIMIT {page_size} OFFSET {offset}"

    results = session.execute(text(sql_query)).fetchall()
    
    list_of_dict=[]
    for index, value in enumerate(results):
        list_of_dict.append(dict(results[index]._asdict()))
    # df = pd.DataFrame(result, columns=column_names)
    # print(list_of_dict)
    return list_of_dict
