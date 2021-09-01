import uuid
import datetime

from app.main import db
from app.main.model.idiom import Idiom
from typing import Dict, Tuple


def save_new_idiom(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    data_check = Idiom.query.filter_by(name=data['name']).first()
    if not data_check:
        new_idiom = Idiom(            
            name=data['name'],
            created_on=data['created_on'],
            updated_on=data['updated_on']
        )
        save_changes(new_idiom)
        return ok(new_idiom)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Idiom already exists.',
        }
        return response_object, 409


def get_all_idioms():
    return Idiom.query.all()


def get_a_idiom(id):
    return Idiom.query.filter_by(id=id).first()


def ok(idiom: Idiom) -> Tuple[Dict[str, str], int]:
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


def save_changes(data: Idiom) -> None:
    db.session.add(data)
    db.session.commit()

