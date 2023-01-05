import typer
from pathlib import Path
from mfc.models import MilleniumFalcon, Empire
from pydantic import ValidationError
from mfc.solve import solve, Node, get_number_of_encounters, calculate_probability
from mfc.state import Wait, Travel

app = typer.Typer()

def print_path(path : list[Node]):
    for node in path:
        match node.action:
            case Wait():
                print ("Wait", end= " ")
            case Travel(destination=destination):
                print(node.action, end= " ")
            case None:
                pass
            case _:
                raise Exception("Unknown action")

@app.command()
def mfc(millenium_falcon_file : Path, empire_file : Path):
    '''Calculate the optimal probability to reach the final planet.'''
    if not millenium_falcon_file.is_file():
        raise typer.Exit(f"File: {millenium_falcon_file} does not exist")
    if not empire_file.is_file():
        raise typer.Exit(f"File: {empire_file} does not exist")
    
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
    

    