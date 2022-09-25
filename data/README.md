# data
This directory stores the data used by the interpreter.

## Files

### network.json
JSON file containing the network used by the interpreter to determine the validity of routes.

The data is structured with two keys at the top level, `"commands"` and `"connections"`. Motorways listed under the
former are those that correspond to commands, the latter being the other valid motorways used for route-finding. Each
motorway name is then a key corresponding to the list of motorways it connects to.

### README.md
This file. Summarises the contents of the data directory.
