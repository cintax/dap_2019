#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    index = list("abc")
    s1 = pd.Series(L1, index)
    s2 = pd.Series(L2, index)
    return (s1,s2)
    
def modify_series(s1, s2):
    s1["d"] = s2.loc["b"]
    del s2["b"]
    return (s1,s2)
    
def main():
    L1 = [2,4,6]
    L2 = [3,5,7]
    S1,S2 = create_series(L1,L2)
    S1,S2 = modify_series(S1,S2)
    print(S1+S2)
    
if __name__ == "__main__":
    main()
