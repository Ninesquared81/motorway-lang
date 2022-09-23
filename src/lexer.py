from typing import Optional

from .m_token import Token, TokenType


def lex(source: str):
    tokens: list[Token] = []
    i = 0
    row = 1
    col = 1
    length = len(source)
    while i < length:
        char = source[i]
        current_token = ""
        current_type: Optional[TokenType] = None
        if char == "M" and i + 1 < length:
            i, current_token = match_mx(i + 1, length, source)
            current_type = TokenType.MX
        elif char == "A" and i + 1 < length:
            i, current_token = match_axm(i + 1, length, source)
            current_type = TokenType.AXM
        elif char == "(" and i + 2 < length:
            i, current_token = match_bracket(i + 1, length, source)
            current_type = TokenType.BRACKET
        elif char == "/n":
            row += 1
            col = 0

        if current_token:
            tokens.append(Token(current_type, current_token, (row, col)))

        col += 1
        i += 1

    return tokens


def match_axm(i: int, length: int, source: str) -> tuple[int, str]:
    current_token = "A"

    while i < length and (char := source[i]).isdigit():
        current_token += char
        i += 1
    if (char := source[i]) == "M":
        current_token += char
    else:
        current_token = ""

    return i, current_token


def match_mx(i: int, length: int, source: str) -> tuple[int, str]:
    current_token = "M"
    while i < length and (char := source[i]).isdigit():
        current_token += char
        i += 1

    return i, current_token


def match_bracket(i: int, length: int, source: str) -> tuple[int, str]:
    char = source[i]
    if char == "M":
        temp, current_token = match_mx(i + 1, length, source)
    elif char == "A":
        temp, current_token = match_axm(i + 1, length, source)
    else:
        temp = i + 1
        current_token = ""

    if source[temp] == ")":
        i = temp
    else:
        current_token = ""

    return i, current_token
