from src.utils import DateRange, CustomException
import pandas as pd
from typing import Union
import time


class Extractor:
    url: str

    def __init__(self, date_range: DateRange):
        self.date_range: DateRange = date_range
        self._extracted_data: Union[pd.DataFrame, list[pd.DataFrame]] = pd.DataFrame()

    def extract(self):
        pass

    @property
    def extracted_data(self):
        return self._extracted_data


class HoursContractsExtractor(Extractor):
    url = "https://tge.pl/energia-elektryczna-rdn?dateShow="

    def __init__(self, date_range: DateRange):
        super(HoursContractsExtractor, self).__init__(date_range)

    def check_if_date_range_id_valid(self):
        if self.date_range.date_range_longer_than_two_months():
            raise CustomException("Date range is two long, only two moths ")

    def __load_data(self, date: str):
        print(f"Extracting data for date: {date}")
        try:
            return pd.read_html(f"{self.url}{date}", thousands=None, decimal=',')
        except ConnectionResetError:
            print(f"Connection reset by peer, retrying for date {date}...")
            time.sleep(5)
            return self.__load_data(date)

    def extract(self):
        extracted_data = []
        for date in self.date_range.date_range:
            dfs = self.__load_data(date)
            if dfs:
                extracted_data.append(dfs[2])
            else:
                print(f"Failed to extract 'Kontrakty godzinowe' for date {date}")
        self._extracted_data = extracted_data


class PowerGenerationExtractor(Extractor):
    url = "https://www.pse.pl/getcsv/-/export/csv/PL_GEN_MOC_JW_EPS/"

    def __init__(self, date_range: DateRange):
        super(PowerGenerationExtractor, self).__init__(date_range)
        self.prepare_full_url()

    def prepare_full_url(self):
        [start_date, end_date] = self.date_range.get_dates_in_specified_string_format(form='pse')
        self.url += f"data_od/{start_date}/data_do/{end_date}"

    def extract(self):
        self._extracted_data = pd.read_csv(self.url, sep=';', decimal=',', parse_dates=[0, 1],
                                           thousands=None, encoding='ISO-8859-2', engine='python')


class BasicUnitsExtractor(Extractor):
    url = "https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/"

    def __init__(self, date_range: DateRange):
        super(BasicUnitsExtractor, self).__init__(date_range)
        self.prepare_full_url()

    def prepare_full_url(self):
        [start_date, end_date] = self.date_range.get_dates_in_specified_string_format(form='pse')
        self.url += f"data_od/{start_date}/data_do/{end_date}"

    def extract(self):
        self._extracted_data = pd.read_csv(self.url, sep=';', decimal=',', parse_dates=[0, 1],
                                           thousands=None, encoding='ISO-8859-2', engine='python')
