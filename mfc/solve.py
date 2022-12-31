from mfc.models import MilleniumFalcon, Empire
from pathlib import Path
from mfc.routes import Routes
from pydantic import BaseModel

class Action:
    pass

class Wait(Action):
    pass

class Travel(Action):
    def __init__(self, destination: str):
        self.destination = destination

class State():
    current_planet : str
    day : int
    autonomy : int
    mf : MilleniumFalcon
    routes : Routes

    def __init__(self, 
        current_planet : str,
        day : int,
        autonomy : int,
        mf : MilleniumFalcon,
        routes : Routes):

        self.current_planet = current_planet
        self.day = day
        self.autonomy = autonomy
        self.mf = mf
        self.routes = routes
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def apply_action(self, action: Action) -> None:
        match action:
            case Wait():
                self.autonomy = self.mf.autonomy
                self.day += 1
            case Travel(destination=destination):
                print("Travel", destination)
                distance = self.routes.get_travel_time(self.current_planet, destination)
                self.autonomy -= distance
                self.day += distance
                self.current_planet = destination
            case _:
                print("Unknown action")

def solve(mf: MilleniumFalcon, empire: Empire) -> float:
    routes = Routes(mf.routes_db)
    print(routes.get_travel_time("Tatooine", "Dagobah"))

    s = State(current_planet="Tatooine", day=0, autonomy=mf.autonomy, mf=mf, routes=routes)
    print(s)
    s.apply_action(Travel("Dagobah"))
    print(s)
    s.apply_action(Wait())
    print(s)








