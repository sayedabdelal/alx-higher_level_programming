#!/usr/bin/python3
def main():
    from add_0 import add

    a = 1
    b = 2
    value = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, value))


if __name__ == "__main__":
    main()
