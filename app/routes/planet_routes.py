from flask import Blueprint, abort, make_response, request, Response
from app.db import db 
from app.models.planet import Planet
from app.models.moon import Moon
from constants import MESSAGE, ID, NAME, DESCRIPTION, NUMBER_OF_MOONS, ORDER_BY, MIMETYPE_JSON
from app.routes.route_utilities import create_model, validate_model

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)

@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)

@bp.get("")
def get_all_planets():
    description_param = request.args.get(DESCRIPTION)
    number_of_moons_param = request.args.get(NUMBER_OF_MOONS)
    order_by_param = request.args.get(ORDER_BY)

    query = db.select(Planet)
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    if number_of_moons_param:
        try:
            number_of_moons_param = int(number_of_moons_param)
            query = query.where(Planet.number_of_moons == number_of_moons_param)
        except ValueError:
            abort(make_response({MESSAGE: f"{number_of_moons_param} expected int type"}, 400))

    if order_by_param:
        query = validate_order_by_param(query, order_by_param)
    else:
        query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    return [planet.to_dict() for planet in planets]

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    return validate_model(Planet, planet_id).to_dict()

@bp.get("/<planet_id>/moons")
def get_all_moons_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return [moon.to_dict() for moon in planet.moons]

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body[NAME]
    planet.description = request_body[DESCRIPTION]
    planet.number_of_moons = request_body[NUMBER_OF_MOONS]

    db.session.commit()

    return Response(status=204, mimetype=MIMETYPE_JSON)

@bp.delete("/<planet_id>")
def delete_planet( planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype=MIMETYPE_JSON)

def validate_order_by_param(query, order_by_param):
    try:
        return query.order_by(getattr(Planet, order_by_param))
    except AttributeError:
        abort(make_response({MESSAGE: f"{ORDER_BY} '{order_by_param}' invalid"}, 400))