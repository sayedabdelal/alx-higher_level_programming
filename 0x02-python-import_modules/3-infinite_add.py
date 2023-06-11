#!/usr/bin/python3
def main():
    from sys import argv

    len_argv = len(argv)
    sum = 0
    if len_argv <= 1:
        print(sum)
    else:
        for i in range(1, len_argv):
            sum += int(argv[i])
        print(sum)


if __name__ == "__main__":
    main()
