from flask import request
from flask_restx import Resource

from ..util.dto import StateDto, WordDto
from ..service.wordservice import save_new_word, get_a_word, get_all_words
from typing import Dict, Tuple

api = WordDto.api
_word = WordDto.word

@api.route('/')
class WordList(Resource):
    @api.doc('list_of_word')
    @api.marshal_list_with(_word, envelope='data')
    def get(self):
        """List all word"""
        return get_all_words()

    @api.expect(_word, validate=True)
    @api.response(201, 'word successfully created.')
    @api.doc('create a new word')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new word """
        data = request.json
        return save_new_word(data=data)

@api.route('/<id>')
@api.param('id', 'The word identifier')
@api.response(404, 'word not found.')
class Word(Resource):
    @api.doc('get a word')
    @api.marshal_with(_word)
    def get(self, id):
        wd = get_a_word(id)
        if not wd:
            api.abort(404)
        else:
            return wd
