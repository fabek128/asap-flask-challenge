import unittest

from app.main import db
from app.main.service.wordservice import save_new_word, get_a_word, get_all_words
from app.test.base import BaseTestCase
import json

class TestWordService(BaseTestCase):

    def test_save_new_word(self):        
        new = save_new_word(data=json.loads(self.wordjson))
        self.assertEqual(new[0]['status'], 'success') 

    def test_get_all_words(self):        
        new = save_new_word(data=json.loads(self.wordjson))
        all_words = get_all_words()
        self.assertEqual(len(all_words), 1)
        self.assertEqual(all_words[0].word, "string")     

    def test_get_a_word(self):        
        new = save_new_word(data=json.loads(self.wordjson))
        word = get_a_word(1)
        self.assertEqual(word.word, "string")        

if __name__ == '__main__':
    unittest.main()