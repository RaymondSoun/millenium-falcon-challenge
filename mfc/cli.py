import typer
from pathlib import Path
from mfc.models import MilleniumFalcon, Empire
from pydantic import ValidationError

app = typer.Typer()

@app.command()
def mfc(millenium_falcon_file : Path, empire_file : Path):
    if not millenium_falcon_file.is_file():
        raise typer.Exit(f"File: {millenium_falcon_file} does not exist")
    if not empire_file.is_file():
        raise typer.Exit(f"File: {empire_file} does not exist")
    
    try:
        mf = MilleniumFalcon.parse_file(millenium_falcon_file)
        print(mf)
    except ValidationError as err:
        print(err)
    
    try:
        empire = Empire.parse_file(empire_file)
        print(empire)
    except ValidationError as err:
        print(err)