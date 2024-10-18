class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "Small, hot, fast", []),
    Planet(2, "Venus", "Thick atmosphere", []),
    Planet(3, "Earth", "Supports life, very watery", ["Moon"]),
    Planet(4, "Mars", "Red planet, biggest volcano", ["Phobos", "Deimos"])
]