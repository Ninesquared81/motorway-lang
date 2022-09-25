# src
This directory contains the source code of the interpreter.

## Files

### \__init\__.py
Empty. Used to allow `src` to be treated as a package by Python.

### exceptions.py
Contains custom exceptions used by the interpreter.

### interpreter.py
Contains the class `Interpreter` which is interprets the validated AST.

### lexer.py
Contains the function `lex` which is used to convert the source code into a list of tokens.

### m_token.py
Contains the definition of the `Token` dataclass and `TokenType` enum.

### main.py
Contains the class `InterpreterSession`, which represents the runtime of the interpreter.

### motorways.py
Contains the classes for the syntax tree nodes (all the command motorways, bar M62, which is rolled into the M25 node),
as well as the `Motorway` abstract base class from which they all inherit and the `MotorwayVisitor` interface (ABC).

### parser.py
Contains the function `parse`, which converts a list of tokens into a list of `Motorway`. The validity of the route is
also checked at this stage.

### README.md
This file. Summarises the contents of the src directory.

### utils.py
Contains utilities used by the project.

### validator.py
Contains the functions `validate_number` to check that a given motorway token is on the network, and `validate_route`
to check that two motorways are directly connected.
