from pathlib import Path

import typer
from pydantic import ValidationError

from mfc.models import Empire, MilleniumFalcon
from mfc.server import app as flask_app
from mfc.solve import Node, solve
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


@app.command(name="solve")
def solve_cmd(millenium_falcon_file: Path, empire_file: Path):
    """Calculate the optimal probability to reach the final planet."""
    if not millenium_falcon_file.is_file():
        print(f"File: {millenium_falcon_file} does not exist")
        raise typer.Exit(1)
    if not empire_file.is_file():
        print(f"File: {empire_file} does not exist")
        raise typer.Exit(1)

    try:
        mf = MilleniumFalcon.parse_file(millenium_falcon_file)
        if not mf.routes_db.is_absolute():
            mf.routes_db = millenium_falcon_file.parent / mf.routes_db
        if not mf.routes_db.is_file():
            print(f"File: {mf.routes_db} does not exist")
            raise typer.Exit(1)
        empire = Empire.parse_file(empire_file)
        _, proba = solve(mf, empire)
        print(proba)
    except ValidationError as err:
        print(err)


@app.command(name="serve")
def serve_cmd():
    """Starts the http server"""
    flask_app.run()
