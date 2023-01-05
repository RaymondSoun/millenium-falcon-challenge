from mfc.models import MilleniumFalcon, Empire
from mfc.state import State, Action, Wait, Travel
from mfc.routes import Routes
from typing import Optional

class Node:
    def __init__(self, parent : Optional["Node"], children: list["Node"], state: State, action:Optional[Action]) -> None:
        self.parent = parent
        self.children = children
        self.state = state
        self.action = action

    def add_child(self, node : "Node"):
        self.children.append(node)

def get_path(node : Node) -> list[Node]:
    path = [node]
    while node.parent:
        path.append(node.parent)
        node = node.parent
    path.reverse()
    return path

def solve(mf: MilleniumFalcon, empire: Empire) -> list[list[Node]]:
    paths = []
    routes = Routes(mf.routes_db)
    initial_state = State(current_planet=mf.departure, day=0, autonomy=mf.autonomy, mf=mf, empire=empire, routes=routes)
    initial_node = Node(None, [], initial_state, None)

    stack = []
    discovered = set()
    stack.append(initial_node)
    while stack:
        node = stack.pop()
        if node not in discovered:
            discovered.add(node)
            
            available_actions = node.state.available_actions()
            if not available_actions:
                if node.state.current_planet == node.state.mf.arrival:
                    path = get_path(node)
                    paths.append(path)

            for action in available_actions:
                new_state = node.state.copy()
                new_state.apply_action(action)
                new_node = Node(node, [], new_state, action)
                node.add_child(new_node)
                stack.append(new_node)

    return paths

def get_number_of_encounters (path : list[Node]) -> int:
    nb_encounters = 0

    for node in path:
        days = node.state.empire.bounty_hunters.get(node.state.current_planet, [])

        if node.state.day in days :
            nb_encounters += 1

    return nb_encounters

def calculate_probability(nb_encounters : int) -> float:
    if nb_encounters == 0:
        return 100
    return round(
        (1 - sum((pow(9, i)) / (pow(10, i + 1)) for i in range(0, nb_encounters))) * 100, 2
    )

