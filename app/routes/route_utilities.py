from flask import make_response, abort
from app.db import db
from constants import MESSAGE

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