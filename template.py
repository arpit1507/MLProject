import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name = "MLProject"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    if not filedir.exists():
        logging.info(f"Creating directory: {filedir}")
        filedir.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        logging.info(f"Creating file: {filepath}")
        filepath.touch()
    else:
        logging.info(f"File already exists: {filepath}")

