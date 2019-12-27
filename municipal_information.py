#!/usr/bin/env python3

import pandas as pd

def main():
    ds = pd.read_csv("src/municipal.tsv", sep='\t')
    ds_shape = ds.shape
    print(f"Shape: {ds_shape[0]},{ds.shape[1]}")
    print("Columns:")
    for i in ds.columns:
        print(i)

if __name__ == "__main__":
    main()
