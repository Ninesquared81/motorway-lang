import enum
import dataclasses


TokenType = enum.Enum("TokenType", "AXM MX BRACKET")


@dataclasses.dataclass
class Token:
    token_type: TokenType
    value: str
    location: tuple[int, int]
