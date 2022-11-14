import pytest
import sys
sys.path.append(r'c:/Users/AGordeyev/Program Files/Projects/tests_hometask')
from hometasks import delete_nonunique, dict_values_to_list
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
        3:['is', 'the', 'best']},
        ['HOMM', 'with', 'cheats', '=', 'lame', 'is', 'the', 'best']
    )        
]
FIXTURE_3 = [
    ([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Франция']},
    {'visit3': ['Владимир', 'Россия']}
    ],
            
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
    @pytest.mark.parametrize()    
    def test_find_visits_to_country():
        