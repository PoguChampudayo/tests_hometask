import pytest
import sys
import os
import test_fixtures
sys.path.append(os.getcwd())
from hometasks import delete_nonunique, dict_values_to_list, find_visits_to_country, get_percentage_of_query_by_words


class TestHometaskFunc():
    '''This test class contains 4 tests for each function in hometask.
    Fixtures are located in test_fixtures.py'''
    @pytest.mark.parametrize('_list, etalon',test_fixtures.FIXTURE_NONUNIQUE)
    def test_nonunique_deletion_1(self, _list:list, etalon:list):
        result = delete_nonunique(_list)
        assert result == etalon
        
    @pytest.mark.parametrize('_dict, etalon', test_fixtures.FIXTURE_DICT_TO_LIST)
    def test_dict_to_list(self, _dict, etalon):
        result = dict_values_to_list(_dict)
        assert result == etalon
        
    @pytest.mark.parametrize('geo_logs, country, etalon', test_fixtures.FIXTURE_GEO_LOGS)    
    def test_find_visits_to_country(self, geo_logs, country, etalon):
        result = find_visits_to_country(country, geo_logs)
        assert result == etalon
        
    @pytest.mark.parametrize('words_count, queries, etalon', test_fixtures.FIXTURE_QUERIES)    
    def test_get_query_percentage(self, words_count, queries, etalon):
        result = get_percentage_of_query_by_words(words_count, queries)
        assert result == etalon   