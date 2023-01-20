import pandas as pd
from src.utils import DateRange


class Loader:
    def __init__(self, report: str, date_range: DateRange, data: pd.DataFrame, path_to_save: str = ""):
        self.data = data
        self.date_range = date_range
        self.report = report
        self.path_to_save = path_to_save
        self.file_name = self.prepare_file_name()

    def prepare_file_name(self) -> str:
        [start_date, end_date] = self.date_range.get_dates_in_specified_string_format(form='pse')
        return f"{self.path_to_save}{self.report}_{start_date}-{end_date}.csv"

    def load(self):
        self.data.to_csv(self.file_name)
