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