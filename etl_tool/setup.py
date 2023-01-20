import setuptools
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="etl_tool",
    version="1.0.0",
    author="Natalia Sokolowska",
    author_email="sokolowska.natalia.anna@gmail.com",
    description="ETL tool for Axpo assignment needs",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    scripts=['etl'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)