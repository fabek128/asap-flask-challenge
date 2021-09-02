import datetime

from app.main import db
from app.main.model.state import State
from typing import Dict, Tuple

def save_new_state(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    data_check = State.query.filter_by(name=data['name']).first()
    if not data_check:
        new_state = State(
            name=data['name']
        )
        save_changes(new_state)
        return ok(new_state)
    else:
        response_object = {
            'status': 'fail',
            'message': 'State already exists.',
        }
        return response_object, 409


def get_all_states():
    return State.query.all()

def get_a_state(id):
    return State.query.filter_by(id=id).first()


def ok(state: State) -> Tuple[Dict[str, str], int]:
    try:
        response_object = {
            'status': 'success',
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: State) -> None:
    db.session.add(data)
    db.session.commit()