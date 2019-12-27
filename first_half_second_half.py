#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    length = int(a.shape[1]/2)
    
    result = np.sum(a[:,0:length], axis=1) > np.sum(a[:,length:], axis=1)
    return a[result]                       

def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(first_half_second_half(a))
    
if __name__ == "__main__":
    main()
