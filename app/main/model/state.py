
from .. import db, flask_bcrypt
import datetime
from ..config import key
from typing import Union


class State(db.Model):
    """ State Model for storing state related details """
    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)