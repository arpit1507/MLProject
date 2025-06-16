import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Now you can import modules
from mlproject.logger import logging
from mlproject.exceptions import CustomException
from mlproject.components.data_ingestion import DataIngestion  # ✅ Corrected import

logging.info("Logging is working from app.py!")

try:
    # Simulating an error to demonstrate CustomException
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logging.info("CustomException has been raised and caught successfully!")
    raise CustomException(e, sys) from e
