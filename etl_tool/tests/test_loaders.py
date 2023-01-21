from src.loaders import Loader
from tempfile import TemporaryDirectory
from src.utils import DateRange
import pandas as pd
import os


def test_load():
    test_columns = ['col1', 'col2']
    test_values = [[1, 2], [3, 4]]
    test_data = pd.DataFrame(test_values, columns=test_columns)

    start_date = '2010-01-01'
    end_date = '2010-01-03'

    start_date_pse_format = '20100101'
    end_date_pse_format = '20100103'
    reports = ["generacja_mocy", "wielkości_podstawowe", "kontrakty_godzinowe"]
    for report in reports:
        with TemporaryDirectory() as tmp_dir:
            loader = Loader(data=test_data, date_range=DateRange(start_date=start_date, end_date=end_date),
                            path_to_save=f"{tmp_dir}/", report=report)
            loader.load()
            expected_result_file = f"{tmp_dir}/{report}_{start_date_pse_format}-{end_date_pse_format}.csv"
            assert os.path.exists(expected_result_file)
            res_data = pd.read_csv(expected_result_file, index_col='Unnamed: 0')
            pd.testing.assert_frame_equal(res_data, test_data)
