import pytest
from src.extractors import BasicUnitsExtractor, HoursContractsExtractor, PowerGenerationExtractor
from src.utils import DateRange, CustomException
from unittest import mock
import pandas as pd
import datetime


@mock.patch("pandas.read_csv")
def test_basic_units_extractor(mock_read_csv: mock.Mock):
    test_columns = ['col1', 'col2']
    test_values = [[1, 2], [3, 4]]
    test_data = pd.DataFrame(test_values, columns=test_columns)
    mock_read_csv.return_value = test_data

    start_date = '2010-01-01'
    end_date = '2010-01-03'
    expected_url = "https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/20100101/data_do/20100103"

    bue = BasicUnitsExtractor(date_range=DateRange(start_date=start_date, end_date=end_date))
    bue.extract()

    assert bue.url == expected_url
    pd.testing.assert_frame_equal(bue.extracted_data, test_data)


@mock.patch("pandas.read_csv")
def test_power_generation_extractor(mock_read_csv: mock.Mock):
    test_columns = ['col1', 'col2']
    test_values = [[1, 2], [3, 4]]
    test_data = pd.DataFrame(test_values, columns=test_columns)
    mock_read_csv.return_value = test_data

    start_date = '2010-01-01'
    end_date = '2010-01-03'
    expected_url = "https://www.pse.pl/getcsv/-/export/csv/PL_GEN_MOC_JW_EPS/data_od/20100101/data_do/20100103"

    pge = PowerGenerationExtractor(date_range=DateRange(start_date=start_date, end_date=end_date))
    pge.extract()

    assert pge.url == expected_url
    pd.testing.assert_frame_equal(pge.extracted_data, test_data)


@mock.patch("pandas.read_html")
def test_hours_contract_extractor_valid_date_range(mock_read_html: mock.Mock):
    days = 2
    test_columns = ['col1', 'col2']
    test_values = [[1, 2], [3, 4]]
    test_data = [pd.DataFrame(), pd.DataFrame(), pd.DataFrame(test_values, columns=test_columns)]
    mock_read_html.return_value = test_data

    expected_results = [test_data[2] for i in range(days + 1)]

    start_date = datetime.datetime.strftime(datetime.datetime.now().date() - datetime.timedelta(days=days), '%Y-%m-%d')
    end_date = datetime.datetime.strftime(datetime.datetime.now().date(), '%Y-%m-%d')

    hce = HoursContractsExtractor(date_range=DateRange(start_date=start_date, end_date=end_date))
    hce.extract()
    assert isinstance(hce.extracted_data, list)
    assert hce.extracted_data == expected_results


def test_hours_contract_extractor_invalid_date_range():
    start_date = '2010-01-01'
    end_date = '2010-01-03'
    with pytest.raises(CustomException) as error:
        _ = HoursContractsExtractor(date_range=DateRange(start_date=start_date, end_date=end_date))
    assert str(error.value) == "Date range is two long, data for only two months back are available"

