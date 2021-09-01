from .. import db, flask_bcrypt
import datetime
from sqlalchemy.orm import relationship
from ..config import key

class Word(db.Model):
    """ Word Model for storing word related details """
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(255), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("state.id"))
    state = relationship("State", backref=db.backref("words", lazy=False)) 
    dictionary_id = db.Column(db.Integer, db.ForeignKey("dictionary.id"))
    dictionary = relationship("Dictionary", backref=db.backref("words", lazy=False))      