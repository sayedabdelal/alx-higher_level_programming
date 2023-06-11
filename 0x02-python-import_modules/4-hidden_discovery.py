#!/usr/bin/python3
import hidden_4

# Get the list of names defined in the module
module_names = dir(hidden_4)
# Iterate over each name in the module_names list
for name in module_names:
    # Check if the name starts with an underscore
    if not name.startswith('_'):
        print(name)
