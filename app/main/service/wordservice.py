import datetime

from app.main import db
from app.main.model.word import Word
from typing import Dict, Tuple

def save_new_word(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    data_check = Word.query.filter_by(word=data['name']).first()
    if not data_check:
        new_word = Word(
            word=data['name'],
            created_on=data['created_on'],
            updated_on=data['updated_on']
        )
        save_changes(new_word)
        return ok(new_word)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Word already exists.',
        }
        return response_object, 409


def get_all_words():
    return Word.query.all()

def get_a_word(id):
    return Word.query.filter_by(id=id).first()


def ok(word: Word) -> Tuple[Dict[str, str], int]:
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


def save_changes(data: Word) -> None:
    db.session.add(data)
    db.session.commit()

