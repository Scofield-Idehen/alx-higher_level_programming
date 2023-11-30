#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
