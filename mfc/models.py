from pydantic import BaseModel, validator, parse_obj_as
from pathlib import Path

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
    
    bounty_hunters: dict[str, int]

    @validator("bounty_hunters", pre=True)
    def validate_bounty_hunters(cls, v: list[dict]):
        bounty_hunters = parse_obj_as(list[BountyHunter], v)
        return {
            bounty_hunter.planet: bounty_hunter.day for bounty_hunter in bounty_hunters
        }