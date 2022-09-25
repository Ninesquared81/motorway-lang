import json
from src import utils

NETWORK_PATH = utils.PROJECT_ROOT / "data" / "network.json"
OUT_PATH = utils.PROJECT_ROOT / "tools" / "connections_md.txt"

network: dict[str, dict[str, list[str]]]
with open(NETWORK_PATH, "r") as file:
    network = json.load(file)

motorways = network["connections"]
lines: list[str] = [f'* {motorway} &ndash; connects to {", ".join(connections)}.'
                    for motorway, connections in motorways.items()]

with open(OUT_PATH, "w") as file:
    file.write("\n".join(lines) + "\n")
