#!/usr/bin/env python3

import sys

def extract_numbers(s):
    result = []
    for x in s.split():
        try:
            result.append(int(x))
        except ValueError:
            try:
                result.append(float(x))
            except ValueError:
                continue
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
