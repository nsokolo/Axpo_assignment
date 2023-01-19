from utils import DateRange
import pandas as pd
from typing import Union
from extractors import HoursContractsExtractor, PowerGenerationExtractor, BasicUnitsExtractor
pd.set_option('display.max_columns', None)


def extract_data(report: str, date_range: DateRange) -> Union[pd.DataFrame, list[pd.DataFrame]]:
    if report == 'kontrakty_godzinowe':
        hce = HoursContractsExtractor(date_range=date_range)
        hce.extract()
        return hce.extracted_data
    elif report == 'generacja_mocy':
        pge = PowerGenerationExtractor(date_range=date_range)
        pge.extract()
        return pge.extracted_data
    elif report == 'wielkości_podstawowe':
        bue = BasicUnitsExtractor(date_range=date_range)
        bue.extract()
        return bue.extracted_data

