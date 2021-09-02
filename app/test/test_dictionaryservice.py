import unittest

from app.main import db
from app.main.service.dservice import save_new_dictionary, get_a_dictionary, get_all_dictionaries, save_changes
from app.main.service.idiom_service import save_new_idiom
from app.test.base import BaseTestCase
import json

class TestDictService(BaseTestCase):

    def test_save_new_dictionary(self):                
        save_new_idiom(data=json.loads(self.idiomjson))
        new = save_new_dictionary(data=json.loads(self.dicjson))
        self.assertEqual(new[0]['status'], 'success') 

    def test_get_all_dictionaries(self):
        save_new_idiom(data=json.loads(self.idiomjson))        
        new = save_new_dictionary(data=json.loads(self.dicjson))
        all_dicts = get_all_dictionaries()
        self.assertEqual(len(all_dicts), 1)
        self.assertEqual(all_dicts[0].name, "string")     

    def test_get_a_word(self):
        save_new_idiom(data=json.loads(self.idiomjson))        
        new = save_new_dictionary(data=json.loads(self.dicjson))
        dict = get_a_dictionary(1)
        self.assertEqual(dict.name, "string")        

if __name__ == '__main__':
    unittest.main()