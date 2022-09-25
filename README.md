# motorway-lang
An esoteric programming language based around the British motorway network.
## The Language
A Motorway program is a description of a route along the British (mainland) motorway network. Only motorways that form 
the main interconnected network are considered part of the program. Anything else (motorway or otherwise) is considered
a comment and ignored.

Certain motorways have special meanings, called **commands**. Other motorways merely serve to connect these commands.
A program is valid only if the route it describes is physically possible (i.e. each motorway visited must connect to
the next). The directionality of junctions is not considered when testing the validity of a route, nor is motorway
status (or lack thereof) of connections at junctions between two motorways (e.g. you con change between the M1 and M69,
even though in real life, this would involve leaving motorway restrictions and negotiating a roundabout before getting
onto the M69). A motorway corresponding to a command can be visited without invoking its effect by placing the route
number in brackets (e.g. `M6 (M1) M69` visits the M1 with no side effects).

A program has access to a data stack, which most of the commands manipulate. The stack comprises 8-bit unsigned cells,
which are mainly interpreted as ASCII characters.

### Commands
* M1 &ndash; increment top of stack.
* M4 &ndash; pop current character and print it to _stdout_.
* M5 &ndash; pop stack and discard the value.
* M6 &ndash; push new cell to stack, initialized to zero.
* M20 &ndash; read a string from _stdin_ and store on stack element-wise (i.e. the final character of the string will be at the top of the stack)
* M25 &ndash; if top of stack is zero, skip past matching `M62` token, else, continue to next motorway (i.e. loop start).
* M40 &ndash; duplicate top of stack.
* M42 &ndash; swap top two elements of stack.
* M48 &ndash; add top of stack to next element.
* M49 &ndash; subtract top of stack from next element.
* M60 &ndash; rotate top three elements of stack like so: `... c b a` -> `... b a c`.
* M62 &ndash; jump back to matching `M25` token (i.e. loop end).

### Other Motorways
* M3 &ndash; connects to M25, M27.
* M8 &ndash; connects to M9, M73, M74, M77, M80, M898, A8M.
* M9 &ndash; connects to M8, M80, M90, M876.
* M11 &ndash; connects to M25.
* M18 &ndash; connects to M1, M62, M180, A1M.
* M23 &ndash; connects to M25.
* M26 &ndash; connects to M20, M25.
* M27 &ndash; connects to M3.
* M32 &ndash; connects to M4.
* M45 &ndash; connects to M1.
* M50 &ndash; connects to M5.
* M53 &ndash; connects to M56.
* M54 &ndash; connects to M6.
* M55 &ndash; connects to M6.
* M56 &ndash; connects to M6, M53, M60.
* M57 &ndash; connects to M58, M62.
* M58 &ndash; connects to M6, M57.
* M61 &ndash; connects to M6, M60, M65, A666M.
* M65 &ndash; connects to M6, M61.
* M66 &ndash; connects to M60, M62.
* M67 &ndash; connects to M60.
* M69 &ndash; connects to M1, M6.
* M73 &ndash; connects to M8, M74, M80, A8M.
* M74 &ndash; connects to M8, M73, M77, A74M.
* M77 &ndash; connects to M8.
* M80 &ndash; connects to M8, M9, M73, M876.
* M90 &ndash; connects to M9, A823M.
* M180 &ndash; connects to M18, M181.
* M181 &ndash; connects to M180, A1077M.
* M271 &ndash; connects to M27.
* M275 &ndash; connects to M27.
* M602 &ndash; connects to M60, M62.
* M606 &ndash; connects to M62.
* M621 &ndash; connects to M1, M62.
* M876 &ndash; connects to M9, M80.
* M898 &ndash; connects to M8.
* A1M &ndash; connects to M1, M18, M25, M62, A66M, A194M, A195M.
* A8M &ndash; connects to M8, M73.
* A38M &ndash; connects to M6.
* A48M &ndash; connects to M4.
* A66M &ndash; connects to A1M.
* A74M &ndash; connects to M6, M74.
* A194M &ndash; connects to A1M.
* A195M &ndash; connects to A1M.
* A308M &ndash; connects to M4, A404M.
* A329M &ndash; connects to M4.
* A404M &ndash; connects to M4, A308M.
* A601M &ndash; connects to M6.
* A627M &ndash; connects to M62.
* A666M &ndash; connects to M61.
* A823M &ndash; connects to M90.
* A1077 &ndash; connects to M181.

## The Interpreter
This repository contains a Python implementation of the language. This relies on the third-party package
[fixedint](https://pypi.org/project/fixedint/) which must be installed before using the interpreter (e.g. using `pip`).
Of course, Python (3.9+) must also be installed on the system to use the interpreter.

With _fixedint_ installed, you can run the interpreter by running the script `motorway.py`:

    python motorway.py [file]

The argument `file`, if provided, determines the source code file to be interpreted. Alternatively, you can omit it to
enter an interactive REPL session. The recommended filename extension for Motorway files is `*.mway`, although any
extension may be used. The extension must be included when invoking the interpreter.

## Project Structure
Source code is (mainly) found in the `src` directory. A single script `motorway.py` is provided in the project root to
make it easier to use as a command line tool.

The network used to validate routes can be found in `data/network.json`.

The `tools` directory contains scripts used to automatically generate various parts of the project. These should not
need to be invoked in normal running of the interpreter (although running them shouldn't break anything either).

The contents of these subdirectories are described in more detail in their individual READMEs.
