#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = a**2
    return np.abs(np.sqrt(a.sum(axis = 1)))

def main():
    a = np.arange(12).reshape(3,4)
    print(vector_lengths(a))
    pass

if __name__ == "__main__":
    main()
