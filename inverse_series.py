#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    ind = list(s.index)
    val = s.values
    #print(ind, val)
    return pd.Series(list(s.index),s.values)

def main():
    s1 = pd.Series([1,2,3,4,5], index = list("abcde"))
    print(s1)
    print(inverse_series(s1))

if __name__ == "__main__":
    main()
