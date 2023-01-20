import datetime
from dateutil import relativedelta


class CustomException(Exception):
    pass


class DateRange:
    def __init__(self, start_date: str = datetime.datetime.now().date(),
                 end_date: str = datetime.datetime.now().date()):
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.__date_range = self.__get_date_range()

    @staticmethod
    def __convert_to_date_type(date: str) -> datetime.date:
        return datetime.datetime.strptime(date, "%Y-%m-%d")

    def __get_date_range(self) -> []:
        start_date = self.__convert_to_date_type(self.start_date)
        end_date = self.__convert_to_date_type(self.end_date)
        return [(start_date+datetime.timedelta(days=x)).strftime('%d-%m-%Y')  # '%Y-%m-%d'
                for x in range((end_date-start_date).days + 1)]

    @property
    def date_range(self):
        return self.__date_range

    def get_dates_in_specified_string_format(self, form: str) -> [str, str]:
        if form == 'pse':
            return [datetime.datetime.strftime(self.__convert_to_date_type(self.start_date), '%Y%m%d'),
                    datetime.datetime.strftime(self.__convert_to_date_type(self.end_date), '%Y%m%d')]
        else:
            raise CustomException(f"Invalid format: {form}")

    def date_range_longer_than_two_months(self):
        start_date = self.__convert_to_date_type(self.start_date)
        delta = relativedelta.relativedelta(start_date, datetime.datetime.now().date())
        res_months = delta.months + (delta.years * 12)
        return True if abs(res_months) > 2 else False
