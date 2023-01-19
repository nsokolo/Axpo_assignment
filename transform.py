from utils import DateRange
import pandas as pd
from typing import Union
from transformers import HoursContractsTransformer, PowerGenerationTransformer, BasicUnitsTransformer
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def transform_data(report: str, data: Union[pd.DataFrame, list[pd.DataFrame]], date_range: DateRange):
    if report == 'kontrakty_godzinowe':
        hct = HoursContractsTransformer(data=data, date_range=date_range)
        hct.transform()
        return hct.data
    elif report == 'generacja_mocy':
        pgt = PowerGenerationTransformer(data=data, date_range=date_range)
        pgt.transform()
        return pgt.data
    elif report == 'jednostki_podstawowe':
        but = BasicUnitsTransformer(data=data, date_range=date_range)
        but.transform()
        return but.data
