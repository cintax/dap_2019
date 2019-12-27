#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    pos_root = ((-b + math.sqrt((b**2)-(4*a*c)))/(2*a))
    neg_root = ((-b - math.sqrt((b**2)-(4*a*c)))/(2*a))
    return (pos_root,neg_root)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
