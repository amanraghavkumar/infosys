01. First create a environment using "conda create -p venv python==3.8 -p" and activate the environment using this command "conda activate venv/" you can replace venv with any name you want. 

02. create a requirements.txt file with the following content:
 in this file and install it using pip install -r requirements.txt and create a README.md file

03. create a folder named src and create a file named __init__.py inside it. This is a python package.

04. again create a setup.py file with the following content:

from setuptools import setup, find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]
        return requirements

setup(
    name='Stock price prediction',                       #replace with your package name
    version='1.0',  
    author="Aman Raghav",                                # replace with your name
    author_email="amanraghav19722@gmail.com",            # replace with your email
    packages=find_packages(), 
    install_requires=get_requirements.txt('requirements.txt')
)

and run the following command to build the package: python setup.py install

05. create a file named .gitignore ans first write in this file "inenv" (your environment).

06. going to your github account and create a repo. and .... 
git init
git add .
git status    # dekhte hai kya kya add hua
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/amanraghavkumar/infosys.git
git push -u origin main

past one by one this command on the terminal of vscode and you will be able to upload your project on github.

07. 