from pathlib import Path

import typer
from pydantic import ValidationError

from mfc.models import Empire, MilleniumFalcon
from mfc.solve import Node, calculate_probability, get_number_of_encounters, solve
from mfc.state import Travel, Wait

app = typer.Typer()


def print_path(path: list[Node]):
    for node in path:
        match node.action:
            case Wait():
                print("Wait", end=" ")
            case Travel(destination=destination):
                print(node.action, end=" ")
            case None:
                pass
            case _:
                raise Exception("Unknown action")


@app.command()
def mfc(millenium_falcon_file: Path, empire_file: Path):
    """Calculate the optimal probability to reach the final planet."""
    if not millenium_falcon_file.is_file():
        print(f"File: {millenium_falcon_file} does not exist")
        raise typer.Exit(1)
    if not empire_file.is_file():
        print(f"File: {empire_file} does not exist")
        raise typer.Exit(1)

    try:
        mf = MilleniumFalcon.parse_file(millenium_falcon_file)
        empire = Empire.parse_file(empire_file)
        paths = solve(mf, empire)
        max_proba = 0
        for path in paths:
            current_proba = calculate_probability(get_number_of_encounters(path))
            if max_proba < current_proba:
                max_proba = current_proba
        print(max_proba)
    except ValidationError as err:
        print(err)
