import pandas as pd
from src.transformers import HoursContractsTransformer
from src.utils import DateRange
from copy import deepcopy


def test_hours_contracts_transformer():
    start_date = '2010-01-01'
    end_date = '2010-01-03'
    columns = [('Unnamed: 0_level_0', 'Czas'), ('FIXING I', 'Kurs (PLN/MWh)'), ('FIXING II', 'Kurs (PLN/MWh)'),
               ('Notowania ciągłe', 'Kurs (PLN/MWh)'), ('FIXING I',  'Wolumen (MWh)'),
               ('FIXING II',  'Wolumen (MWh)'), ('Notowania ciągłe',  'Wolumen (MWh)')]
    values = [['1-2', 1, 1, 1, 1, 1, 1],
              ['2-3', 2, 2, 2, 2, 2, 2],
              ['Min.', 1, None, 1, None, 1, None],
              ['Maks.', 2, None, 2, None, 2, None],
              ['Suma', None, 3, None, 3, None, 3]]
    df = pd.DataFrame(values, columns=columns)
    test_data = [df, df, df]
    expected_result_columns = deepcopy(columns)
    expected_result_columns.append('date')
    expected_result_values = [
        ['1-2', 1, 1, 1, 1, 1, 1, '01-01-2010'],
        ['2-3', 2, 2, 2, 2, 2, 2, '01-01-2010'],
        ['1-2', 1, 1, 1, 1, 1, 1, '02-01-2010'],
        ['2-3', 2, 2, 2, 2, 2, 2, '02-01-2010'],
        ['1-2', 1, 1, 1, 1, 1, 1, '03-01-2010'],
        ['2-3', 2, 2, 2, 2, 2, 2,  '03-01-2010']]
    expected_result = pd.DataFrame(expected_result_values, columns=expected_result_columns)
    expected_result.loc['Min.'] = [None, 1, 1, 1, None, None, None, None]
    expected_result.loc['Maks.'] = [None, 2, 2, 2, None, None, None, None]
    expected_result.loc['Suma'] = [None, None, None, None, 9, 9, 9, None]

    hct = HoursContractsTransformer(data=test_data, date_range=DateRange(start_date=start_date, end_date=end_date))
    hct.transform()
    pd.testing.assert_frame_equal(hct.transformed_data, expected_result)
