import pytest
from etl_tool.src.utils import DateRange, CustomException


def test_convert_to_date_type():
    start_date = '2010-12-30'
    end_date = '2011-01-03'

    date = DateRange(start_date=start_date, end_date=end_date)
    assert date.date_range == ['30-12-2010', '31-12-2010', '01-01-2011', '02-01-2011', '03-01-2011']


def test_get_dates_in_specified_string_format():
    start_date = '2010-12-30'
    end_date = '2011-01-03'

    date = DateRange(start_date=start_date, end_date=end_date)
    assert date.get_dates_in_specified_string_format(form='pse') == ['20101230', '20110103']
    assert date.date_range_longer_than_two_months()

    with pytest.raises(CustomException) as error:
        date.get_dates_in_specified_string_format(form='foo')
        assert error.value == "Invalid format: foo"
