# Axpo_assignment
This project contains simple command-line tool for running ETL process over three website data sources.

## Requirements
- Python 3.9

## Package structure 
```
Axpo_assignment/
├── README.md
├── etl_tool/  
│   └── __init__.py
│   └── etl
│   └── pyproject.toml
│   └── setup.py
│   └── requirements.txt
│   └── src/
│       ├── __init__.py  
│       └── extract.py  
│       └── load.py  
│       └── transform.py  
│       └── extract.ors.py  
│       └── loaders.py  
│       └── transformers.py  
│       └── util.py  
│   └── tests/
│       └── test_*.py  
 
```
The source code (**src/**) and unit tests (**tests/**) are located in **etl_tool/**. 
The same folder contains `setup.py`, `pyproject.toml`, `reqirements.txt` and `etl` executable.

## Installation
- create new virtual environment:
```sh
python3 -m venv venv
```
- activate it:
```sh
source venv/bin/activate
```
- run `pip install` to install package and its dependencies:
```sh
pip install ./etl_tool
``` 
To test if installation was successful run `etl test`. You should see the following output"
```
Yay! It works, you can go on with your etl now!
```

## Usage 

```
usage: etl run [-h] --report {generacja_mocy,wielkości_podstawowe,kontrakty_godzinowe} --start_date START_DATE --end_date END_DATE

optional arguments:
  -h, --help            show this help message and exit
  --report {generacja_mocy,wielkości_podstawowe,kontrakty_godzinowe}
                        Specify which report do you want to generate.
  --start_date START_DATE
                        Starting date of your report in 'yyyy-mm-dd' format
  --end_date END_DATE   Ending date of your report in 'yyyy-mm-dd' format
```
Example of usage:  
`etl run --report generacja_mocy --start_date 2023-01-01 --end_date 2023-01-03`  
will result with extracting data from https://www.pse.pl/dane-systemowe/funkcjonowanie-kse/raporty-dobowe-z-pracy-kse/generacja-mocy-jednostek-wytworczych
for days between **01-01-2023** and **03-01-2023**, apply appropriate transformation and save results into `generacja_mocy_20230101-20230103.csv` in main folder.

## Few comments

The main idea for this package is the separation of extract, transform and load logic. Each component inherits from 
general, semi-abstract class of given type to ensure that contract between components will be perceived. Adding new data 
sources will demand to add  extract and transform classes, without any changes in current logic.