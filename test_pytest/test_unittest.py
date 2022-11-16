import unittest
import sys
import os
sys.path.append(os.getcwd())
from yandex_api import get_YaDisk_headers, check_for_folder, create_YaDisk_folder

class TestYaAPI(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.folder = 'test'
        
    def test_response(self):
        self.assertEqual(create_YaDisk_folder(self.folder), 201)
        
    def test_folder_creation(self):
        self.assertTrue(check_for_folder(self.folder).status_code == 200)