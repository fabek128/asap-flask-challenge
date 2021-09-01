from flask_restx import Api
from flask import Blueprint

from .main.controller.idiom_controller import api as idiom_ns
from .main.controller.dictionary_controller import api as dict_ns
from .main.controller.state_controller import api as st_ns
from .main.controller.word_controller import api as wd_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='ASAP - Flask Rest Challenge',
    version='1.0',
    description='',
)

api.add_namespace(idiom_ns, path='/idiom')
api.add_namespace(dict_ns, path='/dictionary')
api.add_namespace(st_ns, path='/state')
api.add_namespace(wd_ns, path='/wd')



