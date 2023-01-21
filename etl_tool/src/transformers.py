from src.utils import DateRange
import pandas as pd
from typing import Union


class Transformer:
    def __init__(self, data: Union[pd.DataFrame, list[pd.DataFrame]], date_range: DateRange):
        self.date_range = date_range
        self.data = data

    def transform(self):
        pass

    @property
    def transformed_data(self):
        return self.data


class HoursContractsTransformer(Transformer):
    def __init__(self, data: list[pd.DataFrame], date_range: DateRange):
        super(HoursContractsTransformer, self).__init__(data, date_range)

    def transform(self):
        res_df = pd.DataFrame()
        for df, date in zip(self.data, self.date_range.date_range):
            df = df.drop(df.loc[df[('Unnamed: 0_level_0', 'Czas')].isin(['Min.', 'Maks.', 'Suma'])].index, axis=0)
            df['date'] = date
            res_df = pd.concat([res_df, df])

        res_df.replace({"-": None}, inplace=True)
        for column in res_df.columns:
            if 'Czas' not in column and 'date' not in column:
                res_df[column] = res_df[column].astype(float)
        res_df = res_df.reset_index(drop=True)
        res_df.loc['Min.', :] = res_df[[('FIXING I', 'Kurs (PLN/MWh)'), ('FIXING II', 'Kurs (PLN/MWh)'),
                                       ('Notowania ciągłe', 'Kurs (PLN/MWh)')]].min(axis=0)
        res_df.loc['Maks.', :] = res_df[[('FIXING I', 'Kurs (PLN/MWh)'), ('FIXING II', 'Kurs (PLN/MWh)'),
                                       ('Notowania ciągłe', 'Kurs (PLN/MWh)')]].max(axis=0)
        res_df.loc['Suma', :] = res_df[[('FIXING I',  'Wolumen (MWh)'), ('FIXING II',  'Wolumen (MWh)'),
                                       ('Notowania ciągłe',  'Wolumen (MWh)')]].sum(axis=0)
        self.data = res_df


class PowerGenerationTransformer(Transformer):
    def __init__(self, data: pd.DataFrame, date_range: DateRange):
        super(PowerGenerationTransformer, self).__init__(data, date_range)

    def transform(self):
        pass


class BasicUnitsTransformer(Transformer):
    def __init__(self, data: pd.DataFrame, date_range: DateRange):
        super(BasicUnitsTransformer, self).__init__(data, date_range)

    def transform(self):
        pass
