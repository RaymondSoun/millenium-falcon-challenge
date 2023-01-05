from pydantic import BaseModel, validator, parse_obj_as
from pathlib import Path
from collections import defaultdict

class MilleniumFalcon(BaseModel):
    autonomy: int
    departure : str
    arrival: str
    routes_db : Path

class BountyHunter(BaseModel):
    planet: str
    day: int

class Empire(BaseModel):
    countdown: int
    
    bounty_hunters: dict[str, list[int]]

    @validator("bounty_hunters", pre=True)
    def validate_bounty_hunters(cls, v: list[dict]):
        bounty_hunters = parse_obj_as(list[BountyHunter], v)
        new_bounty_hunters = defaultdict(set)

        for bounty_hunter in bounty_hunters:
            new_bounty_hunters[bounty_hunter.planet].add(bounty_hunter.day)

        return new_bounty_hunters