from pydantic import BaseModel
from pathlib import Path

class MilleniumFalcon(BaseModel):
    autonomy: int
    departure : str
    arrival: str
    routes_db : Path

class Planet(BaseModel):
    planet: str
    day: int

class Empire(BaseModel):
    countdown: int
    bounty_hunters: list[Planet]