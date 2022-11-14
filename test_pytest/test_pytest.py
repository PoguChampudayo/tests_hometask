import pytest
import sys
sys.path.append(r'c:/Users/AGordeyev/Program Files/Projects/tests_hometask')
from hometasks import delete_nonunique, dict_values_to_list, find_visits_to_country
FIXTURE_1 = [
    ([332, 211, 332, 332, 1, 2], [332, 211, 2, 1]),
    ([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
]
FIXTURE_2 = [ 
    ({
        1:['abc', 'dce', 'whatever'],
        2:[1, 2, 3],
        3:['end']}, 
        ['abc', 'dce', 'whatever', 1, 2, 3, 'end']
    ),    
    ({
        'cityoftroy':['HOMM', 'with', 'cheats', '=', 'lame'],
        3:['third', 'is', 'the', 'best']},
        ['HOMM', 'with', 'cheats', '=', 'lame', 'third', 'is', 'the', 'best']
    )        
]
FIXTURE_3 = [
    ([
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Франция']},
        {'visit3': ['Владимир', 'Россия']}
    ],
        'Франция',
    [
        {'visit2': ['Дели', 'Франция']}
    ]     
    ),
    ([  {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit6': ['Лиссабон', 'Португалия']}
    ],    
        'Россия',
    [
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']}
    ]
    )
]
class TestFunc():
    
    @pytest.mark.parametrize('_list, etalon',FIXTURE_1)
    def test_nonunique_deletion_1(self, _list, etalon):
        result = delete_nonunique(_list)
        assert result == etalon
        
    @pytest.mark.parametrize('_dict, etalon', FIXTURE_2)
    def test_dict_to_list(self, _dict, etalon):
        result = dict_values_to_list(_dict)
        assert result == etalon
    @pytest.mark.parametrize('geo_logs, country, etalon', FIXTURE_3)    
    def test_find_visits_to_country(self, geo_logs, country, etalon):
        result = find_visits_to_country(country, geo_logs)
        assert result == etalon