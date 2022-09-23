if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    Op = argv[2]

    if op == "+":
        print(f"{num1} + {num2} = {add(num1, num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {sub(num1, num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {mul(num1, num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {div(num1, num2}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
