from setuptools import find_packages,setup

setup(
    name="mlproject",
    version="0.0.1",
    author="saurabh shambharkar",
    author_email="saurabhshambharkar2@gmail.com",
    packages=find_packages(),
    indtall_requires = ["numpy","pandas","matplotlib","seabor"]
)