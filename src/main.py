from src.extract import extract_data
from transform import transform_data
from load import load_data
from utils import DateRange

date_range = DateRange(start_date='2023-01-01', end_date='2023-01-03')
report = "wielkości_podstawowe"  # "generacja_mocy", "wielkości_podstawowe", 'kontrakty_godzinowe'
extracted_data = extract_data(report=report, date_range=date_range)
print(extracted_data)
transformed_data = transform_data(report=report, data=extracted_data, date_range=date_range)
print(transformed_data)
load_data(data=transformed_data, report=report, date_range=date_range)


