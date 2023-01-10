from pathlib import Path
from typing import Type, TypeVar

import typer
from pydantic import BaseModel, ValidationError

from mfc.models import Empire, MilleniumFalcon
from mfc.server import app as flask_app
from mfc.solve import Node, solve
from mfc.state import Travel, Wait

app = typer.Typer()

Model = TypeVar("Model", bound=BaseModel)


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


def load_file(model: Type[Model], file_path: Path) -> Model:
    try:
        model_instance = model.parse_file(file_path)
    except ValidationError as err:
        print(err)
        raise typer.Exit(1)
    except FileNotFoundError as err:
        print(err)
        raise typer.Exit(1)

    return model_instance


def load_millenium_falcon_file(millenium_falcon_file: Path) -> MilleniumFalcon:
    mf = load_file(MilleniumFalcon, millenium_falcon_file)

    if not mf.routes_db.is_absolute():
        mf.routes_db = millenium_falcon_file.parent / mf.routes_db
    if not mf.routes_db.is_file():
        print(f"File: {mf.routes_db} does not exist")
        raise typer.Exit(1)

    return mf


@app.command(name="solve")
def solve_cmd(millenium_falcon_file: Path, empire_file: Path):
    """Calculate the optimal probability to reach the final planet."""
    mf = load_millenium_falcon_file(millenium_falcon_file)
    empire = load_file(Empire, empire_file)
    _, proba = solve(mf, empire)
    print(proba)


@app.command(name="serve")
def serve_cmd(millenium_falcon_file: Path):
    """Starts the http server"""
    mf = load_millenium_falcon_file(millenium_falcon_file)
    # os.environ["MILLENIUM"]
    flask_app.config["mf"] = mf
    flask_app.run(host="0.0.0.0")
