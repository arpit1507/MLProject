import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Now you can import logger
from mlproject.logger import logging
from mlproject.exceptions import CustomException
import pandas as pd
# python dotenv
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")

def read_sql_data():
    logging.info("Reading data from MySQL database")
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("Connection to MySQL database established successfully",mydb)
        df=pd.read_sql("SELECT * FROM data_ingestion.synthetic_employee_burnout", mydb)
        logging.info("Data read successfully from MySQL database")
        return df
    except Exception as e:
        logging.error("Error occurred while reading data from MySQL database")
        raise CustomException(e, sys) from e


