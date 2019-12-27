#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.plot([2,4,6,7], [4,3,5,1], [1,2,3,4], [4,2,3,1])
    plt.title("My first figure")  # Add a title to the figure
    plt.xlabel("My x-axis")       # Give a label to the x-axis
    plt.ylabel("My y-axis") 
    plt.show()
    
if __name__ == "__main__":
    main()
