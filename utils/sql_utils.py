import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy import text
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

    sql_query = f"SELECT * FROM log_data_table WHERE 1=1 {log_level_filter} {date_filter} LIMIT {page_size} OFFSET {offset}"


    results = session.execute(text(sql_query)).fetchall()
    
    list_of_dict=[]
    for index, value in enumerate(results):
        list_of_dict.append(dict(results[index]._asdict()))
    # df = pd.DataFrame(result, columns=column_names)
    # print(list_of_dict)
    return list_of_dict
