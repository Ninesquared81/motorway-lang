#!/usr/bin/env python3
import argparse

from src.main import InterpreterSession


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("file", nargs="?")
args = arg_parser.parse_args()
filename = args.file

session = InterpreterSession(filename)
session.start()
