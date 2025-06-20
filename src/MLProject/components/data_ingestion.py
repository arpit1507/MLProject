import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from mlproject.logger import logging
from mlproject.exceptions import CustomException
from mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")
    train_data_path: str = os.path.join("artifacts", "train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("reading from Mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df=read_sql_data()
            logging.info("Data read successfully from MySQL database")
            logging.info("Saving raw data to CSV file")
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved successfully to CSV file")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Train and test data saved successfully to CSV files")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            logging.info("Exception occurred in data ingestion")
            raise CustomException(e, sys)