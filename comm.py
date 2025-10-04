import argparse
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("Number1", help="First Number")
    p.add_argument("Number2", help="Second Number")
    p.add_argument("Operation", help="Operation")
    args = p.parse_args()

    print(args.Number1)
    print(args.Number2)
    print(args.Operation)
    # now calculation
    n1 = int (args.Number1)
    n2 = int (args.Number2)
    result = None
    if args.Operation == "Add":
        result = n1 + n2
    elif args.Operation == "Subtract":
        result = n1 - n2
    elif args.Operation == "Multiply":
        result = n1 * n2
    print(result)