from etl_tool.src.extract import extract_data
from transform import transform_data
from load import load_data
from utils import DateRange


def main(start_date: str, end_date: str, report: str):
    date_range = DateRange(start_date=start_date, end_date=end_date)
    extracted_data = extract_data(report=report, date_range=date_range)
    transformed_data = transform_data(report=report, data=extracted_data, date_range=date_range)
    load_data(data=transformed_data, report=report, date_range=date_range)


if __name__ == "__main__":
    start_day = '2023-01-01'
    end_day = '2023-01-03'
    report_name = "wielkości_podstawowe"  # "generacja_mocy", "wielkości_podstawowe", 'kontrakty_godzinowe'
    main(start_date=start_day, end_date=end_day, report=report_name)