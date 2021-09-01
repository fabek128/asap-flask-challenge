from flask import request
from flask_restx import Resource

from ..util.dto import DictionaryDto
from ..service.dservice import save_new_dictionary, get_a_dictionary, get_all_dictionaries
from typing import Dict, Tuple

api = DictionaryDto.api
_dictionary = DictionaryDto.dictionary


@api.route('/')
class DicitonaryList(Resource):
    @api.doc('list_of_dictionaries')
    @api.marshal_list_with(_dictionary, envelope='data')
    def get(self):
        """List all dictionaries"""
        return get_all_dictionaries()

    @api.expect(_dictionary, validate=True)
    @api.response(201, 'Dictionary successfully created.')
    @api.doc('create a new dictionary')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Dictionary """
        data = request.json
        return save_new_dictionary(data=data)


@api.route('/<id>')
@api.param('id', 'The dictionary identifier')
@api.response(404, 'Dictionary not found.')
class Dictionary(Resource):
    @api.doc('get a dictionary')
    @api.marshal_with(_dictionary)
    def get(self, id):
        dd = get_a_dictionary(id)
        if not dd:
            api.abort(404)
        else:
            return dd



