
from .. import db, flask_bcrypt
import datetime
from sqlalchemy.orm import relationship
from ..config import key
from typing import Union


class Idiom(db.Model):
    """ Idiom Model for storing idiom related details """
    __tablename__ = "idiom"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)    