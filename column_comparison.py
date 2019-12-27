#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    length = a.shape[1]
    result = a[:,1] > a[:,-2]
    return a[result]
    
def main():
    a = np.array(([5, 6],
                  [8, 7],
                  [2, 8]))
    print(column_comparison(a))

if __name__ == "__main__":
    main()
