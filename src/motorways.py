"""
Auto-generated file defining the AST.

Classes:
Motorway        -- base class for all motorways (commands).
MotorwayVisitor -- interface to be implemented by the interpreter.
Mx classes      -- individual classes representing each motorway.
"""

from __future__ import annotations
import abc

from .m_token import Token


class Motorway(abc.ABC):
    """
    Abstract base class for all motorways to inherit from.

    Methods:
    accept(self, visitor: MotorwayVisitor) -- (abstract) accept a visitor to the motorway.
    """

    @abc.abstractmethod
    def accept(self, visitor: MotorwayVisitor):
        """Call the right method on the visitor."""


class MotorwayVisitor(abc.ABC):
    """Abstract base class to implement visitor pattern for visiting each motorway."""

    @abc.abstractmethod
    def visit_m1(self, motorway: M1):
        """Visit the M1 motorway."""

    @abc.abstractmethod
    def visit_m4(self, motorway: M4):
        """Visit the M4 motorway."""

    @abc.abstractmethod
    def visit_m5(self, motorway: M5):
        """Visit the M5 motorway."""

    @abc.abstractmethod
    def visit_m6(self, motorway: M6):
        """Visit the M6 motorway."""

    @abc.abstractmethod
    def visit_m20(self, motorway: M20):
        """Visit the M20 motorway."""

    @abc.abstractmethod
    def visit_m25(self, motorway: M25):
        """Visit the M25 motorway."""

    @abc.abstractmethod
    def visit_m40(self, motorway: M40):
        """Visit the M40 motorway."""

    @abc.abstractmethod
    def visit_m42(self, motorway: M42):
        """Visit the M42 motorway."""

    @abc.abstractmethod
    def visit_m48(self, motorway: M48):
        """Visit the M48 motorway."""

    @abc.abstractmethod
    def visit_m49(self, motorway: M49):
        """Visit the M49 motorway."""

    @abc.abstractmethod
    def visit_m60(self, motorway: M60):
        """Visit the M60 motorway."""


class M1(Motorway):
    """Increment top of stack."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m1(self)


class M4(Motorway):
    """Pop and print of stack to stdout (as a character)."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m4(self)


class M5(Motorway):
    """Pop top of stack."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m5(self)


class M6(Motorway):
    """Push new (zero-initialized) cell to top of stack."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m6(self)


class M20(Motorway):
    """Read a string from stdin and place onto stack character-wise."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m20(self)


class M25(Motorway):
    """Pop top of stack. If zero, skip to matching 'M62', otherwise, loop."""

    def __init__(self, token: Token, body: list[Motorway]):
        self.token = token
        self.body = body

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m25(self)


class M40(Motorway):
    """Duplicate top of stack."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m40(self)


class M42(Motorway):
    """Swap top two elements of stack."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m42(self)


class M48(Motorway):
    """Pop top of stack and add it to next element."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m48(self)


class M49(Motorway):
    """Pop top of stack and subtract from next element."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m49(self)


class M60(Motorway):
    """Rotate top three elements of stack like so: ... c b a --> ... b a c."""

    def __init__(self, token: Token):
        self.token = token

    def accept(self, visitor: MotorwayVisitor):
        return visitor.visit_m60(self)
