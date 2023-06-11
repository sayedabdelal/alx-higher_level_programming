#!/usr/bin/python3
def main():
    import hidden_4

    # Get the list of names defined in the module
    module_names = dir(hidden_4)
    # Iterate over each name in the module_names list
    for name in module_names:
        # Check if the name starts with an underscore
        if name[:2] != "__":
            print(name)


if __name__ == "__main__":
    main()
