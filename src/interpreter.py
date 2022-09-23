from fixedint import MutableUInt8

from . import motorways
from .exceptions import EmptyStackError


def check_stack(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            raise EmptyStackError
    return wrapper


class Interpreter(motorways.MotorwayVisitor):
    def __init__(self):
        self._stack: list[MutableUInt8] = []

    def interpret(self, route: list[motorways.Motorway]):
        pass

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
        self._stack.append(MutableUInt8(0))

    def visit_m20(self, motorway: motorways.M20):
        chars = input()
        for char in chars:
            self._stack.append(MutableUInt8(ord(char)))

    @check_stack
    def visit_m25(self, motorway: motorways.M25):
        while self._stack.pop():
            pass

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
