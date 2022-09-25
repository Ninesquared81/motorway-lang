# tools
This directory contains scripts used to generate other parts of the project, as well as output from them without any
specific destination.

## Subdirectories

### out
Stores generic output from scripts without a specific destination.

## Files

### generate_connections.py
Generates a markdown list of motorways and their connections and stores it in `out/generate_connections_md.py`.
Used to write the project README.

### generate_motorways.py
Generates the file `src/motorways.py`, which defines the AST nodes (commands).

### README.md
This file. Summarises the contents of the tools directory. 