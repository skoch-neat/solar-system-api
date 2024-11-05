from app.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[int]
    description: Mapped[str]
    distance_from_planet: Mapped[int]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_to_dict = {
            "id": self.id, 
            "size": self.size,
            "description": self.description,
            "distance_from_planet": self.distance_from_planet   
        }

        if self.planet:
            moon_to_dict["planet"] = self.planet.name

        return moon_to_dict     

    @classmethod
    def from_dict(cls, moon_data):
        return cls(
            size=moon_data["size"],
            description=moon_data["description"],
            distance_from_planet=moon_data["distance_from_planet"],
            planet_id=moon_data.get("planet_id")
        )
