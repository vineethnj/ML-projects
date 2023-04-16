from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    #this function will return the list of requirement
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[ req.replace("\n","")  for req in requirement]#we are doing that we replaceing the the \n with blank


        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement   
    

setup(
name='mlproject',
version='0.0.1',
author='vineeth',
author_email='nvineeth672@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)


