#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    # add number
    v_add = add(a, b)
    # subtraction
    v_sub = sub(a, b)
    # multiplication
    v_mul = mul(a, b)
    # division
    v_div = (a, b)

    print("{:d} + {:d} = {:d}".format(a, b, v_add))
    print("{:d} - {:d} = {:d}".format(a, b, v_sub))
    print("{:d} * {:d} = {:d}".format(a, b, v_mul))
    print("{:d} / {:d} = {:d}".format(a, b, v_div))


#  prevent it from being executed when imported
if __name__ == "__main__":
    main()
