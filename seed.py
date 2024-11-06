from app.models.moon import Moon
from app.models.planet import Planet
from app.db import db

def seed_data():
    # Original planets with descriptions and moon counts
    mercury = Planet(name="Mercury", description="The smallest planet in our solar system.", number_of_moons=0)
    venus = Planet(name="Venus", description="Hottest planet in the solar system.", number_of_moons=0)
    earth = Planet(name="Earth", description="The only planet known to support life.", number_of_moons=1)
    mars = Planet(name="Mars", description="Known as the Red Planet.", number_of_moons=2)
    jupiter = Planet(name="Jupiter", description="Largest planet with a prominent storm.", number_of_moons=79)

    # Add planets to the session and commit to generate IDs
    db.session.add_all([mercury, venus, earth, mars, jupiter])
    db.session.commit()  # Commit planets first to generate their IDs

    # Moons with references to their planets
    moon_earth = Moon(size=3474, description="Earth's only natural satellite", distance_from_planet=384400, planet_id=earth.id)
    phobos = Moon(size=22, description="One of Mars' two moons", distance_from_planet=9377, planet_id=mars.id)
    deimos = Moon(size=12, description="The smaller moon of Mars", distance_from_planet=23460, planet_id=mars.id)
    ganymede = Moon(size=5268, description="Largest moon in the solar system", distance_from_planet=1070400, planet_id=jupiter.id)
    europa = Moon(size=3122, description="One of Jupiter's four Galilean moons", distance_from_planet=671000, planet_id=jupiter.id)

    # Add moons to the session and commit
    db.session.add_all([moon_earth, phobos, deimos, ganymede, europa])
    db.session.commit()