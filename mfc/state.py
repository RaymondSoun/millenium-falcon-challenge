from copy import copy

from pydantic import BaseModel

from mfc.models import Empire, MilleniumFalcon
from mfc.routes import Routes


class Action(BaseModel):
    pass


class Wait(Action):
    pass


class Travel(Action):
    destination: str


class State:
    def __init__(
        self,
        current_planet: str,
        day: int,
        autonomy: int,
        mf: MilleniumFalcon,
        empire: Empire,
        routes: Routes,
    ):

        self.current_planet = current_planet
        self.day = day
        self.autonomy = autonomy
        self.mf = mf
        self.empire = empire
        self.routes = routes

    def __str__(self) -> str:
        return str(self.__dict__)

    def copy(self) -> "State":
        return copy(self)

    def apply_action(self, action: Action) -> None:
        match action:
            case Wait():
                self.autonomy = self.mf.autonomy
                self.day += 1
            case Travel(destination=destination):
                distance = self.routes.get_travel_time(self.current_planet, destination)
                self.autonomy -= distance
                self.day += distance
                self.current_planet = destination
            case _:
                raise Exception(f"Unknown action: {action}")

    def check_arrival(self) -> bool:
        return self.current_planet == self.mf.arrival

    def available_actions(self) -> list[Action]:
        available_actions = []
        if self.day >= self.empire.countdown or self.check_arrival():
            return []

        for destination in self.routes.get_possible_destinations(self.current_planet):
            distance = self.routes.get_travel_time(self.current_planet, destination)
            if self.autonomy >= distance and self.empire.countdown - self.day >= distance:
                available_actions.append(Travel(destination=destination))
        available_actions.append(Wait())

        return available_actions
