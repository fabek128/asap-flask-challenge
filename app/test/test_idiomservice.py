import unittest

from app.main import db
from app.main.service.idiom_service import save_new_idiom, get_a_idiom, get_all_idioms
from app.test.base import BaseTestCase
import json

class TestIdiomService(BaseTestCase):

    def test_save_new_idiom(self):        
        new = save_new_idiom(data=json.loads(self.idiomjson))
        self.assertEqual(new[0]['status'], 'success') 

    def test_get_all_words(self):        
        new = save_new_idiom(data=json.loads(self.idiomjson))
        all_idioms = get_all_idioms()
        self.assertEqual(len(all_idioms), 1)
        self.assertEqual(all_idioms[0].name, "test")     

    def test_get_a_word(self):        
        new = save_new_idiom(data=json.loads(self.idiomjson))
        idiom = get_a_idiom(1)
        self.assertEqual(idiom.name, "test")        

if __name__ == '__main__':
    unittest.main()