import unittest
import sys
import os
sys.path.append(os.getcwd())
from yandex_api import get_YaDisk_headers, check_for_folder, create_YaDisk_folder

class TestYaAPI(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.correct_folder = 'test'
        self.wrong_folder = 'test//'
        
    def test_good_response(self):
        self.assertEqual(create_YaDisk_folder(self.correct_folder), 201)
        
        
    def test_bad_response(self):
        self.assertEqual(create_YaDisk_folder(self.wrong_folder), 404)
        
    def test_folder_creation(self):
        create_YaDisk_folder(self.correct_folder)
        self.assertTrue(check_for_folder(self.correct_folder).status_code == 200)