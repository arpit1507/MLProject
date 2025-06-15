import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Now you can import logger
from mlproject.logger import logging
from mlproject.exceptions import CustomException

logging.info("Logging is working from app.py!")
try:
    # Simulating an error to demonstrate CustomException
    a=1/0
except Exception as e:
    logging.info("CustomException has been raised and caught successfully!")
    raise CustomException(e, sys) from e