# End to End Machine Learning Project

This project displays all the things that are needed to be covered and coded to create a Machine Learning Project. here we follow the following steps to create and setup the environment for a machine learning project

### Project Github And Code Setup

Here we start with creating a new project and initializing the github steps
```
git init
git add .
git commit -m "new project"
git remote add origin https://github.com/arpit1507/MLProject.git 
```

Now for setup.py file we need to impliment the following code
```
from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
    return requirements
setup(
    name='MLProject',
    version='0.1.0',
    author='Arpit Agrawal',
    author_email='arpitagrawal150701@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
```
The setup.py file is used to define package metadata and dependencies, making your project installable and shareable.

### Automating Project Structure Using Template.py
In a machine learning project, components are the individual steps like data preprocessing, feature engineering, model training, and evaluation, while a pipeline is the structured sequence that connects these components to ensure smooth, repeatable, and organized execution of the entire workflow from raw data to final predictions.

to create the structure of a machine learning project we can use the following code
```
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
```

#### Logging and run time error