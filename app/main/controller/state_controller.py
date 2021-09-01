from flask import request
from flask_restx import Resource

from ..util.dto import StateDto
from ..service.stateservice import save_new_state, get_a_state, get_all_states
from typing import Dict, Tuple

api = StateDto.api
_state = StateDto.state

@api.route('/')
class StatesList(Resource):
    @api.doc('list_of_states')
    @api.marshal_list_with(_state, envelope='data')
    def get(self):
        """List all states"""
        return get_all_states()

    @api.expect(_state, validate=True)
    @api.response(201, 'state successfully created.')
    @api.doc('create a new state')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new state """
        data = request.json
        return save_new_state(data=data)


@api.route('/<id>')
@api.param('id', 'The state identifier')
@api.response(404, 'state not found.')
class State(Resource):
    @api.doc('get a state')
    @api.marshal_with(_state)
    def get(self, id):
        st = get_a_state(id)
        if not st:
            api.abort(404)
        else:
            return st
