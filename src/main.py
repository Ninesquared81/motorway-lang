import sys

from src.lexer import lex
from src.parser import parse
from src.interpreter import Interpreter
from src import exceptions


class InterpreterSession:
    def __init__(self, filename):
        self.filename = filename
        self.interpreter = Interpreter()

    def start(self):
        if self.filename is None:
            try:
                self.run_prompt()
            except EOFError:
                pass
        else:
            self.run_file(self.filename)

    def run_prompt(self):
        # looks like the motorway sign (a wide version)
        prompt = "[.\u0336/\u0336|\u0336\\\u0336.\u0336]: "
        while True:
            line = input(prompt)
            if not line or line == chr(4) or line.lower() == "quit":
                return
            if line.startswith(":Debug"):
                debug(line.removeprefix(":Debug").lstrip(), self.interpreter)
            self.run(line)

    def run_file(self, filename: str):
        with open(filename, "r") as file:
            source = file.read()
        self.run(source)

    def run(self, source: str):
        tokens = lex(source)
        try:
            route = parse(tokens)
            self.interpreter.interpret(route)
        except exceptions.MotorwayBaseError as error:
            token = error.token
            print(f"Error at {token.value} {token.location}: {error.message}", file=sys.stderr)


def debug(line: str, interpreter: Interpreter):
    command = Debug.get_commands()
    for subcommand in line.split():
        try:
            command = command[subcommand]
        except KeyError:
            print("Unrecognised debug command:", line, file=sys.stderr)
            return
        if not isinstance(command, dict):
            break
    else:
        return
    # noinspection PyCallingNonCallable
    command(interpreter)


class Debug:
    @classmethod
    def get_commands(cls):
        return {
            "stack": {
                "print": cls.print_stack,
                "clear": cls.clear_stack,
                "dump": cls.dump_stack,
            }
        }

    @staticmethod
    def print_stack(interpreter: Interpreter):
        interpreter.print_stack()

    @staticmethod
    def clear_stack(interpreter: Interpreter):
        interpreter.clear_stack()

    @staticmethod
    def dump_stack(interpreter: Interpreter):
        interpreter.print_stack()
        interpreter.clear_stack()
