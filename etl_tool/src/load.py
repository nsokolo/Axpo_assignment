from utils import DateRange
from loaders import Loader
import pandas as pd


def load_data(data: pd.DataFrame, report: str, date_range: DateRange):
    loader = Loader(data=data, date_range=date_range, report=report)
    loader.load()
