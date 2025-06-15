import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Now you can import logger
from mlproject.logger import logging

logging.info("Logging is working from app.py!")