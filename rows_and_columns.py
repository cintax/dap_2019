#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    result = [a[i,:] for i in range(0,a.shape[0])]
    return result    
    
def get_columns(a):
    result = [a[:,i] for i in range(0,a.shape[1])]
    return result

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
