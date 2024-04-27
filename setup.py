from setuptools import find_packages, setup
#from typing import List

def get_requirements() -> List[str]:
    requirements_list =list[str]=[]
    return requirements_list
  
setup(
    name='livesensor',
    version='0.0.1',
    author='suraj pawar',
    author_email='surajpawar558@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()  #its call to function get_requirements()
)
