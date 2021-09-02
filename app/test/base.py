from app.main import db
from manage import app
from flask_testing import TestCase


class BaseTestCase(TestCase):
    wordjson = '{ "name": "string", "created_on": "2021-09-02", "updated_on": "2021-09-02", "state_id": 0, "dictionary_id": 0}'
    idiomjson = '{ "name": "test", "created_on": "2021-09-01T00:00:00", "updated_on": "2021-09-01T00:00:00" }'
    dicjson = '{ "name": "string",  "created_on": "2021-09-02",  "updated_on": "2021-09-02",  "idiom_id": 1 }'
    statejson = '{ "name": "string" }'
      
    def create_app(self):
        app.config.from_object('app.main.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()