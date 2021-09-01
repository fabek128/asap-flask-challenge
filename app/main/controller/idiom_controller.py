from flask import request
from flask_restx import Resource

from ..util.dto import IdiomDto
from ..service.idiom_service import save_new_idiom, get_a_idiom, get_all_idioms
from typing import Dict, Tuple

api = IdiomDto.api
_idiom = IdiomDto.idiom


@api.route('/')
class IdiomList(Resource):
    @api.doc('list_of_idioms')
    @api.marshal_list_with(_idiom, envelope='data')
    def get(self):
        """List all idioms"""
        return get_all_idioms()

    @api.expect(_idiom, validate=True)
    @api.response(201, 'Idiom successfully created.')
    @api.doc('create a new idiom')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Idiom """
        data = request.json
        return save_new_idiom(data=data)


@api.route('/<id>')
@api.param('id', 'The idiom identifier')
@api.response(404, 'Idiom not found.')
class Idiom(Resource):
    @api.doc('get a idiom')
    @api.marshal_with(_idiom)
    def get(self, id):
        idiom = get_a_idiom(id)
        if not idiom:
            api.abort(404)
        else:
            return idiom
