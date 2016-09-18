#!/usr/bin/env python
import sys
import re

def str_to_numeric_tuplet(s):
    """Given a string, return a tuplet containing the quantity and item, e.g.
    input:  "42 ponies"
    output: (42, "ponies")
    If no quantity is present, the first element will be None.
    """
    quantity = re.findall(r'^\d+', s)
    quantity = quantity[0] if quantity else ""
    s = s.lstrip(quantity)
    return (int(quantity) if quantity is not "" else None, s)


if __name__ == "__main__":
    user_file = sys.argv[1]
    with open(user_file, "r") as f:
        # Read the file, strip training newlines, and turn each newline into an
        # item in a list.
        data = f.read().strip().split('\n')

    # Convert unordered list into two lists of tuplets
    ret = [str_to_numeric_tuplet(x) for x in data]
    # Items that do not start with integers
    ret_1 = [x for x in ret if x[0] is not None]
    # Everything else (i.e. items that *do* begin with integers
    ret_2 = [x for x in ret if x not in ret_1]

    # Sort items first by quantity, then alphabetically, irrespective of capitalization
    ret_1 = sorted(ret_1, key=lambda item: (item[0], item[1].lower()))
    ret_2 = sorted(ret_2, key=lambda item: (item[1].lower()))

    for x in ret_1:
        print("".join([str(y) for y in x]))
    for x in ret_2:
        print("".join([y for y in x if y]))
