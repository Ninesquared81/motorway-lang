import sys

from fixedint import UInt8

from . import motorways
from .exceptions import EmptyStackError


def check_stack(func):
    def wrapper(interpreter, motorway, *args, **kwargs):
        try:
            func(interpreter, motorway, *args, **kwargs)
        except IndexError:
            raise EmptyStackError(motorway.token, "Tried to operate on empty stack.")
    return wrapper


class Interpreter(motorways.MotorwayVisitor):
    def __init__(self):
        self._stack: list[UInt8] = []

    def interpret(self, route: list[motorways.Motorway]):
        for motorway in route:
            motorway.accept(self)

    @check_stack
    def visit_m1(self, motorway: motorways.M1):
        self._stack[-1] += 1

    @check_stack
    def visit_m4(self, motorway: motorways.M4):
        element = self._stack.pop()
        print(chr(int(element)), end="")

    @check_stack
    def visit_m5(self, motorway: motorways.M5):
        self._stack.pop()

    def visit_m6(self, motorway: motorways.M6):
        self._stack.append(UInt8(0))

    def visit_m20(self, motorway: motorways.M20):
        char = sys.stdin.read(1)
        # treat EOF and EOT as zero
        val = 0 if not char or char == chr(4) else ord(char)
        self._stack.append(UInt8(val))

    @check_stack
    def visit_m25(self, motorway: motorways.M25):
        while self._stack.pop():
            self.interpret(motorway.body)

    @check_stack
    def visit_m40(self, motorway: motorways.M40):
        self._stack.append(self._stack[-1])

    @check_stack
    def visit_m42(self, motorway: motorways.M42):
        a = self._stack.pop()
        b = self._stack.pop()
        self._stack.append(a)
        self._stack.append(b)

    @check_stack
    def visit_m48(self, motorway: motorways.M48):
        top = self._stack.pop()
        self._stack[-1] += top

    @check_stack
    def visit_m49(self, motorway: motorways.M49):
        top = self._stack.pop()
        self._stack[-1] -= top

    @check_stack
    def visit_m60(self, motorway: motorways.M60):
        a = self._stack.pop()
        b = self._stack.pop()
        c = self._stack.pop()
        self._stack.append(b)
        self._stack.append(a)
        self._stack.append(c)

    def print_stack(self):
        print(self._stack)

    def clear_stack(self):
        while self._stack:
            self._stack.pop()
