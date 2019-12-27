#!/usr/bin/env python3
import numpy as np
from functools import reduce
import math

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    else:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        mul = reduce(fun, gen)
        
        if n > 0:
            return mul
        else:
            return np.linalg.inv(mul)

def main():
    a = np.array([[1,2],
                  [3,4]])
    print(matrix_power(a,4))

if __name__ == "__main__":
    main()
