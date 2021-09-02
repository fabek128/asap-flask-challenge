import datetime

from app.main import db
from app.main.model.dictionary import Dictionary
from typing import Dict, Tuple


def save_new_dictionary(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    data_check = Dictionary.query.filter_by(name=data['name']).first()
    if not data_check:
        new_dic = Dictionary(
            name=data['name'],
            created_on=data['created_on'],
            updated_on=data['updated_on'],
            idiom_id=data['idiom_id']
        )
        save_changes(new_dic)
        return ok(new_dic)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Dictionary already exists.',
        }
        return response_object, 409


def get_all_dictionaries():
    return Dictionary.query.all()


def get_a_dictionary(id):
    return Dictionary.query.filter_by(id=id).first()


def ok(dict: Dictionary) -> Tuple[Dict[str, str], int]:
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


def save_changes(data: Dictionary) -> None:
    db.session.add(data)
    db.session.commit()

