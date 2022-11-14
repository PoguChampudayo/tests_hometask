import pytest
import sys
sys.path.append(r'c:/Users/AGordeyev/Program Files/Projects/tests_hometask')
from hometasks import delete_nonunique
FIXTURE = [
    ([332, 211, 332, 332, 1, 2], [332, 211, 2, 1]),
    ([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], [5, 4, 3, 2, 1])
]
class TestFunc():
    @pytest.mark.parametrize('_list, etalon',FIXTURE)
    def test_nonunique_deletion(self, _list, etalon):
        result = delete_nonunique(_list)
        assert result == etalon