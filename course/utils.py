from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd


def load_pg_data(query):
    config = load_db_config()
    with get_db_connection(config) as conn:
        df = fetch_pg_data(conn, query)
    return df


def find_project_root(marker=".git"):
    """
    Traverse upward from the current file to find the project root.
    Includes the current file's directory in the search.
    """
    current_dir = Path.cwd().resolve()
    for directory in [current_dir] + list(current_dir.parents):
        if (directory / marker).exists():
            return directory
    raise RuntimeError("Project root not found. Please ensure a marker file exists.")


def load_db_config(env_path=None):
    if env_path is None:
        env_path = find_project_root()
    load_dotenv(dotenv_path=env_path / ".Renviron", override=True)
    return {
        "dbname": os.getenv("PGRDATABASE"),
        "user": os.getenv("PGRUSER"),
        "password": os.getenv("PGRPASSWORD"),
        "host": os.getenv("PGRHOST"),
        "port": os.getenv("PGRPORT"),
    }


def get_db_connection(config):
    return psycopg2.connect(**config)


def fetch_pg_data(conn, query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
    return pd.DataFrame(rows, columns=colnames)
