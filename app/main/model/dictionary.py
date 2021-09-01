
from .. import db, flask_bcrypt
import datetime
from sqlalchemy.orm import relationship
from ..config import key
from typing import Union


class Dictionary(db.Model):
    """ Dictionary Model for storing dict related details """
    __tablename__ = "dictionary"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False) 
    idiom_id = db.Column(db.Integer, db.ForeignKey("idiom.id"))
    idiom = relationship("Idiom", backref=db.backref("dictionaries", lazy=False))    