import enum
import json
import pathlib


FILEPATH = pathlib.Path(__file__).parent.parent.joinpath("data/network.json")


RouteType = enum.Enum("RouteType", "INVALID COMMAND CONNECTION")


network: dict[str, dict[str, list[str]]]
with open(FILEPATH) as file:
    network = json.load(file)


def validate_number(value: str) -> RouteType:
    for route_type, motorways in network.items():
        for motorway in motorways:
            if motorway == value:
                return key_to_type(route_type)

    return RouteType.INVALID


def validate_route(start_road: str, start_type: RouteType, end_road: str) -> bool:
    return end_road in network[type_to_key(start_type)][start_road]


def type_to_key(route_type: RouteType) -> str:
    if route_type == RouteType.INVALID:
        return ""
    return route_type.name.lower() + "s"


def key_to_type(key: str) -> RouteType:
    return RouteType[key.removesuffix("s").upper()]
