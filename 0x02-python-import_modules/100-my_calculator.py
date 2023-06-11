#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    from sys import argv

    len_argv = len(argv) - 1
    id = 1
    if len_argv != 3:
        print(" Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    opr = argv[2]
    # check operator exists or not
    if opr == '+':
        value = add(a, b)
    elif opr == '-':
        value = sub(a, b)
    elif opr == '*':
        value = mul(a, b)
    elif opr == '/':
        value = div(a, b)
    else:
        # operator not exists
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(value)


if __name__ == "__main__":
    main()
