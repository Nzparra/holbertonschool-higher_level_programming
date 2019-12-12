#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        op = argv[2]
        if op not in{"+", "-", "*", "/"}:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            if op == "+":
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            if op == "-":
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            if op == "*":
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            if op == "-":
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
