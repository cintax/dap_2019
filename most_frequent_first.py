#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    test = np.unique(a[:,c], axis = 0, return_counts=True)
    values, count = test
    count_sort = np.argsort(-count)
    value_sort = values[count_sort].reshape((1,-1))
    indxs = np.concatenate([np.where((a[:,c] == x))[0] for x in np.nditer(value_sort)])
    return a[indxs]
    
def main():
    np.random.seed(1)
    a = np.random.randint(0,10,(5,5))
    print(most_frequent_first(a, 3))

if __name__ == "__main__":
    main()
