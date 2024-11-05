from flask import make_response, abort
from app.db import db
from constants import MESSAGE

def create_model(cls, request_body):
    try:
        new_model = cls.from_dict(request_body)
        
    except KeyError as error:
        response = {'message': f'Invalid request: missing {error.args[0]}'}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return make_response(new_model.to_dict(), 201)

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response({MESSAGE: f"{cls.__name__} id {model_id} invalid"}, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        abort(make_response({MESSAGE: f"{cls.__name__} id {model_id} not found"}, 404))
    
    return model