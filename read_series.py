#!/usr/bin/env python3
import pandas as pd
import numpy as np
import re

def read_series():
    ind = []
    val = []
    while True:
        a = input("Enter an Index and a Value:")
        if len(a) == 0:
            break
        else: 
            splitted = a.split()
            if len(splitted) < 2:
                raise Exception("Input of type [\w\d]+\s[\w\d]+")
            else:
                ind.append(splitted[0])
                val.append("".join(splitted[1:]))

            
    return pd.Series(val, ind)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
