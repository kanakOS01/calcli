import argparse
from unittest import result
from calcli.calculator import Calculator

def main():
    calculator = Calculator()

    parser = argparse.ArgumentParser(
        description="A CLI Calculator Tool",
        epilog="Example calcli add 5 10"
    )
    parser.add_argument(
    "--precision", "-p", type=int, default=2, help="Number of decimal places"
    )

    subparsers = parser.add_subparsers(title="Operators", dest="operator")

    add_parser = subparsers.add_parser("add", help="Add 2 numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")

    sub_parser = subparsers.add_parser("sub", help="Subtract 2 numbers")
    sub_parser.add_argument("a", type=float, help="First number")
    sub_parser.add_argument("b", type=float, help="Second number")

    mul_parser = subparsers.add_parser("mul", help="Multiply 2 numbers")
    mul_parser.add_argument("a", type=float, help="First number")
    mul_parser.add_argument("b", type=float, help="Second number")

    div_parser = subparsers.add_parser("div", help="Divide 2 numbers")
    div_parser.add_argument("a", type=float, help="First number")
    div_parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    if args.operator == "add":
        result = round(calculator.add(args.a, args.b), args.precision)
        print(f"Result: {result}")
    elif args.operator == "sub":
        result = round(calculator.sub(args.a, args.b), args.precision)
        print(f"Result: {result}")
    elif args.operator == "mul":
        result = round(calculator.mul(args.a, args.b), args.precision)
        print(f"Result: {result}")
    elif args.operator == "div":
        try:
            result = round(calculator.div(args.a, args.b), args.precision)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()