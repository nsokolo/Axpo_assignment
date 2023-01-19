from extract import extract_data
from transform import transform_data
from utils import DateRange
date_range = DateRange(start_date='2023-01-01', end_date='2023-01-03')
extracted_data = extract_data(report="generacja_mocy", date_range=date_range)
transformed_data = transform_data(report='generacja_mocy', data=extracted_data, date_range=date_range)

