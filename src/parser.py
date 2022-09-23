from . import motorways
from .exceptions import ParseError
from .m_token import Token, TokenType
from .validator import validate_number, RouteType, validate_route


def parse(tokens: list[Token]) -> list[motorways.Motorway]:
    if not tokens:
        return []

    commands: list[Token] = []
    route_types = [add_token_if_valid(token, commands) for token in tokens]

    for current_token, current_type, next_token in zip(tokens, route_types, tokens[:-1]):
        if not validate_route(current_token.value, current_type, next_token.value):
            raise ParseError(current_token, f"Cannot find route from {current_token.value} to {next_token.value}.")

    return parse_commands(commands)


def add_token_if_valid(token: Token, commands: list[Token]) -> RouteType:
    route_type = validate_number(token.value)
    if route_type == RouteType.INVALID:
        raise ParseError(token, f"Motorway {token.value} not part of network.")
    elif route_type == RouteType.COMMAND and token.token_type != TokenType.BRACKET:
        commands.append(token)
    return route_type


def parse_commands(commands: list[Token]) -> list[motorways.Motorway]:
    i = 0
    length = len(commands)
    route: list[motorways.Motorway] = []
    while i < length:
        i, motorway = parse_command(i, length, commands)
        route.append(motorway)
        i += 1
    return route


def parse_command(i: int, length: int, commands: list[Token]) -> tuple[int, motorways.Motorway]:
    command = commands[i]
    if command.value == "M25":
        i, motorway = parse_loop(i, length, commands)
    elif command.value == "M1":
        motorway = motorways.M1(command)
    elif command.value == "M4":
        motorway = motorways.M4(command)
    elif command.value == "M5":
        motorway = motorways.M5(command)
    elif command.value == "M6":
        motorway = motorways.M6(command)
    elif command.value == "M20":
        motorway = motorways.M20(command)
    elif command.value == "M40":
        motorway = motorways.M40(command)
    elif command.value == "M42":
        motorway = motorways.M42(command)
    elif command.value == "M48":
        motorway = motorways.M48(command)
    elif command.value == "M49":
        motorway = motorways.M49(command)
    elif command.value == "M60":
        motorway = motorways.M60(command)
    else:
        raise ParseError(command, "Not recognized.")
    return i, motorway


def parse_loop(i: int, length: int, commands: list[Token]) -> tuple[int, motorways.M25]:
    token = commands[i]
    body: list[motorways.Motorway] = []
    while i < length:
        command = commands[i]
        if command == "M62":
            break
        i, motorway = parse_command(i, length, commands)
        body.append(motorway)
        i += 1
    else:  # no break
        raise ParseError(token, "Loop body never closed.")

    return i, motorways.M25(token, body)
