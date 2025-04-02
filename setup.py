from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]
        return requirements


setup(
    name='Stock price prediction', 
    version='0.0.1',  
    author="Aman Raghav" ,
    author_email="amanraghav19722@gmail.com", 
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)
