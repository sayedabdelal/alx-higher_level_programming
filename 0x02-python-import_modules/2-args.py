#!/usr/bin/python3
def main():
    from sys import argv

    len_argv = len(argv) - 1
    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif len_argv == 1:
        print("{:d} argument.".format(0))
    else:
        print("{:d} arguments:".format(len_argv))
        for i in range(1, len_argv):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
