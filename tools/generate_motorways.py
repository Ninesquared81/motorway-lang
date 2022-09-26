FILEPATH = "../src/motorways.py"


# this is a list of 3-tuples: (class (motorway) name, __init__() parameters (i.e. fields), class docstring)
motorways: list[tuple[str, str, str]] = [
    ("M1", "token: Token", '"""Increment top of stack."""'),
    ("M4", "token: Token", '"""Pop and print of stack to stdout (as a character)."""'),
    ("M5", "token: Token", '"""Pop top of stack."""'),
    ("M6", "token: Token", '"""Push new (zero-initialized) cell to top of stack."""'),
    ("M20", "token: Token", '"""Read a single character from stdin and push it to the top of the stack."""'),
    ("M25", "token: Token, body: list[Motorway]", '"""Pop top of stack. If zero, skip to matching \'M62\', otherwise, loop."""'),
    ("M40", "token: Token", '"""Duplicate top of stack."""'),
    ("M42", "token: Token", '"""Swap top two elements of stack."""'),
    ("M48", "token: Token", '"""Pop top of stack and add it to next element."""'),
    ("M49", "token: Token", '"""Pop top of stack and subtract from next element."""'),
    ("M60", "token: Token", '"""Rotate top three elements of stack like so: ... c b a --> ... b a c."""'),
]


lines: list[str] = [
    '"""',
    "Auto-generated file defining the AST.",
    "",
    "Classes:",
    "Motorway        -- base class for all motorways (commands).",
    "MotorwayVisitor -- interface to be implemented by the interpreter.",
    "Mx classes      -- individual classes representing each motorway.",
    '"""',
    "",
    "from __future__ import annotations",
    "import abc",
    "",
    "from .token import Token",
    "",
    "",
    "class Motorway(abc.ABC):",
    '    """',
    "    Abstract base class for all motorways to inherit from.",
    "",
    "    Methods:",
    "    accept(self, visitor: MotorwayVisitor) -- (abstract) accept a visitor to the motorway.",
    '    """',
    "",
    "    @abc.abstractmethod",
    "    def accept(self, visitor: MotorwayVisitor):",
    '        """Call the right method on the visitor."""',
    "",
]


def add_motorway_visitor():
    lines.extend([
        "",
        "class MotorwayVisitor(abc.ABC):",
        '    """Abstract base class to implement visitor pattern for visiting each motorway."""',
        "",
    ])
    for motorway, *_ in motorways:
        lines.extend([
            "    @abc.abstractmethod",
            f"    def visit_{motorway.lower()}(self, motorway: {motorway}):",
            f'        """Visit the {motorway} motorway."""',
            "",
        ])
    if not motorways:
        lines.append("    pass")


def add_motorway_classes():
    for motorway, values, docstring in motorways:
        lines.extend([
            "",
            f"class {motorway}(Motorway):",
            f"    {docstring}",
            "",
        ])
        lines.extend(get_init(values))
        lines.extend([
            "    def accept(self, visitor: MotorwayVisitor):",
            f"        return visitor.visit_{motorway.lower()}(self)",
            "",
        ])


def get_init(values: str):
    init: list[str] = [f"    def __init__(self, {values}):"]
    params = values.split(", ")
    for param in params:
        field, _ = param.split(": ")
        init.append(f"        self.{field} = {field}")
    init.append("")
    return init


add_motorway_visitor()
add_motorway_classes()


with open(FILEPATH, "w") as file:
    file.write("\n".join(lines))
