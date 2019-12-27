#!/usr/bin/env python3

import numpy as np

def diamond(n):
    side = n + (n - 1)
    a = np.concatenate((np.eye(n,n)[::-1],np.eye(n,n)), axis = 1)
    b = np.concatenate((np.eye(n,n),np.eye(n,n)[::-1]), axis = 1)
    result = np.concatenate((a,b))
    result = np.delete(result, n, 0)
    result = np.delete(result, n, 1)
    return result.astype('int')
    
def main():
    n = int(input("Size of side of Diamond: "))
    print(diamond(n))

if __name__ == "__main__":
    main()