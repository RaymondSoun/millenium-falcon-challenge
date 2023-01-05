from flask import Flask, request
from flask_cors import CORS
from pydantic import ValidationError

from mfc.models import Empire, MilleniumFalcon
from mfc.solve import Node, solve

ALLOWED_EXTENSIONS = {"json"}

app = Flask(__name__)
app.config.from_object(__name__)
# app.secret_key = b"J\x14bM,P\xa3\xc9\xf5#j%\xb8<\x1fav\xfa\xb2\xc2\x9fY\xcev"

CORS(app, resources={r"/*": {"origins": "*"}})
MILLENIUM_FALCON = MilleniumFalcon.parse_file("./data/millennium-falcon.json")


@app.route("/calculate", methods=["POST"])
def calculate_odds():
    empire_file = request.files.get("file")
    if not empire_file:
        return {"error": "Missing empire file"}, 400
    try:
        empire_data = Empire.parse_raw(empire_file.read())
    except ValidationError:
        return {"error": "Invalid empire file"}, 400

    best_path, proba = solve(MILLENIUM_FALCON, empire_data)
    return {
        "origin_planet": best_path[0].state.current_planet,
        "best_path": serialize_best_path(best_path),
        "probability": proba,
    }, 200


def serialize_best_path(path: list[Node]) -> list[dict]:
    serialized_path = []
    for node in path[1:]:
        serialized_node = node.action.dict()  # type: ignore
        serialized_node["type"] = type(node.action).__name__
        serialized_path.append(serialized_node)
    return serialized_path


if __name__ == "__main__":
    app.run()
