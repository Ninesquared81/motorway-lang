import argparse
import sys

from src.lexer import lex
from src.parser import parse
from src.interpreter import Interpreter
from src import exceptions


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", nargs="?")
    args = arg_parser.parse_args()
    filename = args.file

    session = InterpreterSession(filename)
    session.start()


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
            if line.lower() == "quit":
                return
            self.run(line)

    def run_file(self, filename: str):
        with open(filename, "r") as file:
            source = file.read()
        self.run(source)

    def run(self, source: str):
        tokens = lex(source)
        route = parse(tokens)
        try:
            self.interpreter.interpret(route)
        except exceptions.MotorwayBaseError as error:
            token = error.token
            print(f"Error at {token.value} {token.location}", file=sys.stderr)


if __name__ == "__main__":
    main()
