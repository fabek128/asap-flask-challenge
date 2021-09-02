import unittest

from app.main import db
from app.main.service.stateservice import save_new_state, save_changes, get_a_state, get_all_states
from app.test.base import BaseTestCase
import json

class TestStateService(BaseTestCase):

    def test_save_new_state(self):        
        new = save_new_state(data=json.loads(self.statejson))
        self.assertEqual(new[0]['status'], 'success') 

    def test_get_all_states(self):        
        new = save_new_state(data=json.loads(self.statejson))
        allst = get_all_states()
        self.assertEqual(len(allst), 1)
        self.assertEqual(allst[0].name, "string")     

    def test_get_a_state(self):        
        new = save_new_state(data=json.loads(self.statejson))
        st = get_a_state(1)
        self.assertEqual(st.name, "string")        

if __name__ == '__main__':
    unittest.main()