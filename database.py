# utils/database.py
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from sqlalchemy.exc import SQLAlchemyError

def get_mysql_db_connection(user, password, host, port, db_name):
    """Establishes a connection to a MySQL database and returns a SQLDatabase object."""
    try:
        from urllib.parse import quote_plus
        # Properly encode the password to handle special characters
        encoded_password = quote_plus(password)
        db_uri = f"mysql+mysqlconnector://{user}:{encoded_password}@{host}:{port}/{db_name}"
        db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=2)
        return db
    except SQLAlchemyError as e:
        # Re-raise with a more user-friendly message
        raise ConnectionError(f"Failed to connect to MySQL: {e}")
    except Exception as e:
        raise ConnectionError(f"An unexpected error occurred during MySQL connection: {e}")


def create_db_from_dataframe(df: pd.DataFrame, table_name: str = "data_table"):
    """Creates an in-memory SQLite database from a pandas DataFrame."""
    try:
        # Use a file-based SQLite DB in memory by pointing to a specific URI
        # This is a more stable way to handle in-memory DBs with Streamlit
        engine = create_engine(f"sqlite:///{table_name}.db?mode=memory&cache=shared", echo=False)
        df.to_sql(table_name, engine, index=False, if_exists="replace")
        db = SQLDatabase(engine=engine, sample_rows_in_table_info=2, include_tables=[table_name])
        # Return both the db object AND the engine
        return db, engine
    except Exception as e:
        raise RuntimeError(f"Failed to create in-memory database: {e}")