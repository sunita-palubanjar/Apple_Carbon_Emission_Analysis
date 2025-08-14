# Imports and file paths
# --- Imports ---
import pandas as pd         # For reading CSVs and working with DataFrames
import os                   # For file and directory operations
from sqlalchemy import create_engine  # For database connection
import logging              # For creating logs of the ingestion process
import time

# --- Logging configuration ---
logging.basicConfig(
    filename="logs/ingestion_db.log",  # Path where the log file will be stored
    level=logging.DEBUG,               # Capture all log levels from DEBUG and above
    format='%(asctime)s - %(levelname)s - %(message)s',  # Include timestamp, severity, and message
    filemode="a"                        # Append logs to file instead of overwriting
)

engine = create_engine('sqlite:///emission.db')

# scripting
def ingest_db(df, table_name, engine):  # this function will ingest dataframe into datbase table"
    df.to_sql(table_name, con=engine, if_exists = 'replace', index = False)

def load_raw_data():
    start = time.time()
    for file in os.listdir('apple_emissions'):
        if file.endswith('.csv'):
            df = pd.read_csv(f"apple_emissions/{file}", delimiter=';')
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('------------Ingestion Complete-------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

if __name__== '__main__':
    load_raw_data()