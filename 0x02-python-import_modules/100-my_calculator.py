#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if argv[2] == '*':
        print('*')
        return
    len_argv = len(argv) - 1
    operators = {'+': add, '*': mul, '/': div, '-': sub}
    if len_argv != 3:
        print(" Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    opr = argv[2]
    # check operator exists or not
    if opr not in operators:
        # operator not exists
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, opr, b, operators[opr](a, b)))


if __name__ == "__main__":
    main()
