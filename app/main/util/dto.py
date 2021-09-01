from flask_restx import Namespace, fields

class IdiomDto:
    api = Namespace('idiom', 'idiom related operations')
    idiom = api.model('idiom', {
        'name': fields.String(required=True, description='name of idiom'),
        'created_on': fields.DateTime(required=True, description='creation date'),
        'updated_on': fields.DateTime(required=True, description='modification date')
    })


class DictionaryDto:
    api = Namespace('dictionary', 'dictionary related operations')
    dictionary = api.model('dictionary', {
        'word': fields.String(required=True, description='word'),
        'created_on': fields.DateTime(required=True, description='creation date'),
        'updated_on': fields.DateTime(required=True, description='modification date'),
        'idiom_id': fields.Integer(required=True, description='idiom id')
    })

class WordDto:
    api = Namespace('word', 'word related operations')
    word = api.model('word', {
        'name': fields.String(required=True, description='name of dictionary'),
        'created_on': fields.DateTime(required=True, description='creation date'),
        'updated_on': fields.DateTime(required=True, description='modification date'),
        'state_id': fields.Integer(required=True, description='state, id'),
        'dictionary_id': fields.Integer(required=True, description='dictionary id')
    })    

class StateDto:
    api = Namespace('state', 'state related operations')
    state = api.model('state', {
        'name': fields.String(required=True, description='name of state')
    })  

